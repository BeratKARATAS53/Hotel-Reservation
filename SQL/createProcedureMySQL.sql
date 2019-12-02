create table if not exists balance(
	id int auto_increment primary key,
   	money float,
   	balance_date date
);

create table if not exists hotel(
   	id int auto_increment primary key,
   	name varchar(200) unique not null,
   	address varchar(255) not null,
   	telephone varchar(20) unique not null,
   	hotel_info varchar(255) not null,
   	star int,
   	hotel_type varchar(150) not null,
   	balance_id int references balance(id)
);

create table if not exists person(
   	id int auto_increment primary key,
   	firstname varchar (100) not null,
   	lastname varchar (100) not null,
   	passwrd varchar (255) not null,
   	email varchar (255) unique not null,
   	address varchar (255) not null,
   	telephone varchar (20) unique not null,
   	balance_id int references balance(id)
);

create table if not exists manager(
   	id int auto_increment primary key,
   	salary float,
   	hotel_id int references hotel(id),
   	person_id int references person(id)
);

create table if not exists employee(
   	id int auto_increment primary key,
   	salary float,
   	hotel_id int references hotel(id),
   	person_id int references person(id)
);

create table if not exists customer(
	id int auto_increment primary key,
   	age int not null,
   	username varchar(100) unique not null,
   	person_id int references person(id)
);

create table if not exists organization(
   	id int auto_increment primary key,
   	name varchar(255) not null,
   	org_info varchar(255) not null,
  	price float not null,
   	hotel_id int references hotel(id)
);

create table if not exists room(
   	id int auto_increment primary key,
   	room_info varchar(255) not null,
   	room_price float not null,
   	room_number varchar(10) not null,
   	status varchar(255) not null,
   	capacity int not null,
   	hotel_id int references hotel(id)
);

create table if not exists reservation(
   	id int auto_increment primary key,
   	reservation_date date not null,
   	total_day int not null,
   	total_night int not null,
   	price float not null,
   	customer_id int references customer(id)
);

create table if not exists room_reservation (
   	room_id int references room(id),
   	reservation_id int references reservation(id)
);

create table if not exists specialroom(
   	id int auto_increment primary key,
   	feature varchar(255) not null,
   	room_id int references room(id)
);

create table if not exists standartroom(
   	id int auto_increment primary key,
   	room_id int references room(id)
);

create table if not exists extraservice (
   	id int auto_increment primary key,
   	service varchar(255) not null,
   	service_price float not null,
   	service_point int
);

create table if not exists room_extraservice (
   	room_id int references room(id),
   	service_id int references extraservice(id)
);

create table if not exists foodservice (
   	id int auto_increment primary key,
   	food_detail varchar(255) not null,
   	service_id int references extraservice(id)
);

drop procedure if exists addbalance;
delimiter $$
create procedure addbalance(in balance_money float, in balance_date date)
begin
	insert into balance(money, balance_date) values(balance_money, balance_date); 
end;
delimiter ;
/*call addbalance(money '255', date '2019-12-01');*/

drop procedure if exists addhotel;
delimiter $$
create procedure addhotel(in name varchar(200), in address varchar(255), in telephone varchar(20), in hotel_info varchar(255),
	in star int, in hotel_type varchar(150))
begin
	select 'eklemeden önce' AS '';
	call addbalance(null, curdate());
	insert into hotel(name, address, telephone, hotel_info, star, hotel_type, balance_id)
	values(name, address, telephone, hotel_info, star, hotel_type,  (select count(*) from balance));  
	select 'eklemeden sonra' AS '';
end
delimiter ;
call addhotel('hilton', 'tunali', '5555555', 'ultra zengin', 5, 'luks otel');

drop procedure if exists addperson;
delimiter $$
create procedure addperson(in firstname varchar(100), in lastname varchar(100), in passwrd varchar(255), in mail varchar(255),
	in address varchar(255), in phone varchar(20), in age integer, in salary float, in username varchar(150), in hotel_id int,
	in person_type varchar(20))
begin
	declare id INT DEFAULT 0;
	if not exists (select * from person p where p.email = mail or p.telephone = phone) then
	   	case person_type
	   	when 'customer' then
	   		begin
		   		call addbalance(salary, curdate());
	   			insert into person(firstname, lastname, passwrd, email, address, telephone, balance_id)
	   			values(firstname, lastname, passwrd, mail, address, phone, (select count(*) from balance));
				select p.id into id from person p where p.email = mail;
	    		insert into customer(age, username, person_id) values(age, username, id); 
			end;
		when 'employee' then
			begin
		   		call addbalance(salary, curdate());
	   			insert into person(firstname, lastname, passwrd, email, address, telephone, balance_id)
	   			values(firstname, lastname, passwrd, mail, address, phone, (select count(*) from balance));
				select p.id into id from person p where p.email = mail;
				insert into employee(salary, hotel_id, person_id) values(salary, hotel_id, id);
			end;
		when 'manager' then
			begin
		   		call addbalance(salary, curdate());
	   			insert into person(firstname, lastname, passwrd, email, address, telephone, balance_id)
	   			values(firstname, lastname, passwrd, mail, address, phone, (select count(*) from balance));
				select p.id into id from person p where p.email = mail;
				insert into manager(salary, hotel_id, person_id) values(salary, hotel_id, id);
			end;
		end case;
	end if;
end
delimiter ;

drop procedure if exists deleteperson;
delimiter $$
create procedure deleteperson(in person_id integer)
begin
	if exists (select * from person p where p.id = person_id) then
	   	delete from person where id = person_id;
	end if;
end
delimiter ;

drop procedure if exists updateperson;
delimiter $$
create procedure updateperson(in firstname varchar(100), in lastname varchar(100), in passwrd varchar(255), in mail varchar(255),
	in address varchar(255), in phone varchar(20), in age integer, in salary float, in username varchar(150), in hotel_id int,
	in person_type varchar(20))
begin
	declare person_id INT DEFAULT 0;
	declare id INT DEFAULT 0;
	declare balance INT DEFAULT 0;
	if exists (select * from person p where p.email=mail or p.telephone=phone) then
	   	case person_type
	   	when 'customer' then
	   		begin
		   		select p.id into person_id from person p where p.email=mail;
		   		select c.id into id from customer c where c.username=username;
				select b.id into balance from balance b, person p where p.balance_id=b.id and p.id=person_id;
	    		update person set person.firstname=firstname, person.lastname=lastname, person.passwrd=passwrd,
	    			person.email=mail, person.address=address, person.telephone=phone where person.id=person_id;
	    		update customer set customer.age=age, customer.username=username where customer.id=id;
	    		update balance set balance.balance_date=curdate(), balance.money=money where balance.id=balance;
			end;
		when 'employee' then
			begin
		   		select p.id into person_id from person p where p.email=mail;
		   		select e.id into id from employee e where e.person_id=person_id;
				select b.id into balance from balance b, person p where p.balance_id=b.id and p.id=person_id;
	    		update person set person.firstname=firstname, person.lastname=lastname, person.passwrd=passwrd,
	    			person.email=mail, person.address=address, person.telephone=phone where person.id=person_id;
	    		update employee set employee.salary=salary where employee.id=id;
	    		update balance set balance.balance_date=curdate(), balance.money=money where balance.id=balance;
			end;
		when 'manager' then
			begin
		   		select p.id into person_id from person p where p.email=mail;
		   		select e.id into id from employee e where e.person_id=person_id;
				select b.id into balance from balance b, person p where p.balance_id=b.id and p.id=person_id;
	    		update person set person.firstname=firstname, person.lastname=lastname, person.passwrd=passwrd,
	    			person.email=mail, person.address=address, person.telephone=phone where person.id=person_id;
	    		update manager set manager.salary=salary where manager.id=id;
	    		update balance set balance.balance_date=curdate(), balance.money=money where balance.id=balance;
			end;
		end case;
	end if;
end
delimiter ;
call addperson('ali0', 'veli', '123', '0@g.c', 'mamk', '555', 21, null, 'aliveli', null, 'customer');
call addperson('ali1', 'veli', '123', '1@g.c', 'mamk', '111', 21, 222.22, null, 1, 'employee');
call addperson('ali2', 'veli', '123', '5@g.c', 'mamk', '555', 21, null, 'aliveli', 1, 'employee');
call addperson('ali3', 'veli', '123', '1@g.c', 'mamk', '111', 21, 222.22, 'veliali', null, 'customer');
call addperson('ali4', 'veli', '123', '2@g.c', 'mamk', '222', 21, 222.22, null, 1, 'manager');
call addperson('ali6', 'veli', '123', '4@g.c', 'mamk', '131', 21, 222.22, null, 1, 'employee');

call updateperson('ali0-u', 'veli', '123', '0@g.c', 'mamk', '555', 21, null, 'aliveli', null, 'customer');
call updateperson('ali4-u', 'veli', '123', '2@g.c', 'mamk', '222', 21, 222.22, null, 1, 'manager');
call updateperson('ali6-u', 'veli', '123', '4@g.c', 'mamk', '131', 21, 222.22, null, 1, 'employee');

call deleteperson(3);

drop procedure if exists addroom;
delimiter $$
create procedure addroom(in room_info varchar(255), in room_price float, in room_number varchar(10), in status varchar(255),
	in capacity integer, in feature varchar(255), in hotel_id integer, in room_type varchar(25))
begin
	declare room_id INT DEFAULT 0;
	if exists (select * from hotel h where h.id = hotel_id) then
	   	case room_type
	   	when 'special' then
	   		begin
				if not exists (select * from room r where r.room_number=concat('0-', hotel_id, room_number) and r.hotel_id=hotel_id) then 
					insert into room(room_info, room_price, room_number, status, capacity, hotel_id)
					values(room_info, room_price, concat('0-', hotel_id, room_number), status, capacity, hotel_id);
					select distinct r.id into room_id from room r where r.hotel_id=hotel_id and r.room_number=concat('0-', hotel_id, room_number);
					insert into specialroom(feature, room_id) values(feature, room_id);
				end if;
		   	end;
	   	when 'standart' then
	   		begin
				if not exists (select * from room r where r.room_number=concat('1-', hotel_id, room_number) and r.hotel_id=hotel_id) then
					insert into room(room_info, room_price, room_number, status, capacity, hotel_id)
					values(room_info, room_price, concat('1-', hotel_id, room_number), status, capacity, hotel_id);
					select distinct r.id into room_id from room r where r.hotel_id=hotel_id and r.room_number=concat('1-', hotel_id, room_number);
					insert into standartroom(room_id) values(room_id);
				end if;
		   	end;
		end case;
	end if;
end
delimiter ;
call addroom('hilton', 5555, 5, 'uygun', 4, 'ekstra pahali', 1, 'special');
call addroom('hilton', 5555, 5, 'uygun', 4, 'ekstra ucuz', 1, 'special');
call addroom('hilton', 555, 5, 'uygun', 4, null, 1, 'standart');
call addroom('hilton', 5555, 6, 'uygun', 4, 'ekstra yemekli', 1, 'special');
call addroom('hilton', 555, 52, 'uygun', 4, null, 1, 'standart');

drop procedure if exists addreservation;
delimiter $$
create procedure addreservation(in reservation_date date, in total_day integer, in total_night integer, in price float,
	in customer_id integer, in room_id integer)
begin
	declare reservation_id INT DEFAULT 0;
	if not exists (select * from reservation r where r.reservation_date=reservation_date and r.total_day=total_day and r.total_night=total_night) then
		if exists (select * from customer c where c.id=customer_id) then
			if exists (select * from room r where r.id=room_id) then
				insert into reservation(reservation_date, total_day, total_night, price, customer_id)
				values(reservation_date, total_day, total_night, price, customer_id);
				select id into reservation_id from reservation r where r.reservation_date=reservation_date and r.total_day=total_day and r.total_night=total_night;
				insert into room_reservation(room_id, reservation_id) values(room_id, reservation_id);
			end if;
		end if;
	end if;
end
delimiter ;
call addreservation(curdate(), 8, 8, 1589, 1, 1);

drop procedure if exists addorganization;
delimiter $$
create procedure addorganization(in name varchar(255), in org_info varchar(255), in price float, in hotel_id integer)
begin
	if not exists (select * from organization o where o.name=name and o.org_info=org_info) then
		if exists (select * from hotel h where h.id=hotel_id) then
			insert into organization(name, org_info, price, hotel_id) values(name, org_info, price, hotel_id);
		end if;
	end if;
end
delimiter ;
call addorganization('Murat Boz', 'Ünlü sanaçtý Murat Boz bizlerle', 125, 1);

drop procedure if exists addextraservice;
delimiter $$
create procedure addextraservice(in service varchar(255), in service_price float, in service_point integer, in room_id integer)
begin
	declare service_id INT DEFAULT 0;
	if not exists (select * from extraservice e where e.service=service and e.service_price=service_price) then
		if exists (select * from room r where r.id=room_id) then
			insert into extraservice(service, service_price, service_point) values(service, service_price, service_point);
			select id into service_id from extraservice e where e.service=service and e.service_price=service_price;
			insert into room_extraservice(room_id, service_id) values(room_id, service_id);
		end if;
	end if;
end
delimiter ;
call addextraservice('temizlik', 55, 0, 1);

drop procedure if exists addfoodservice;
delimiter $$
create procedure addfoodservice(in service varchar(255), in service_price float, in service_point integer, in food_detail varchar(255),
	in room_id integer)
begin
	declare service_id INT DEFAULT 0;
	if not exists (select * from extraservice e, foodservice f where e.id=f.service_id and e.service=service and f.food_detail=food_detail) then
		if exists (select * from room r where r.id=room_id) then
			insert into extraservice(service, service_price, service_point) values(service, service_price, service_point);
			select id into service_id from extraservice e where e.service=service and e.service_price=service_price;
			insert into foodservice(food_detail, service_id) values(food_detail, service_id);
		end if;
	end if;
end
delimiter ;
call addfoodservice('kahvaltý', 55, 0, 'açýk büfe kahvaltý', 1);
