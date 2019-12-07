/*---TABLES---*/
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
   	balance_id int not null,
   	foreign key (balance_id) references balance(id) on update cascade
);

create table if not exists person(
   	id int auto_increment primary key,
   	firstname varchar (100) not null,
   	lastname varchar (100) not null,
   	passwrd varchar (255) not null,
   	email varchar (255) unique not null,
   	address varchar (255) not null,
   	telephone varchar (20) unique not null,
   	balance_id int not null,
   	foreign key (balance_id) references balance(id) on update cascade
);

create table if not exists manager(
   	id int auto_increment primary key,
   	salary float,
   	hotel_id int not null,
   	person_id int not null,
   	foreign key (hotel_id) references hotel(id) on delete cascade on update cascade,
   	foreign key (person_id) references person(id) on delete cascade on update cascade
);

create table if not exists employee(
   	id int auto_increment primary key,
   	salary float,
   	hotel_id int not null,
   	person_id int not null,
   	foreign key (hotel_id) references hotel(id) on delete cascade on update cascade,
   	foreign key (person_id) references person(id) on delete cascade on update cascade
);

create table if not exists customer(
	id int auto_increment primary key,
   	age int not null,
   	username varchar(100) unique not null,
   	person_id int,
   	foreign key (person_id) references person(id) on delete cascade on update cascade
);

create table if not exists organization(
   	id int auto_increment primary key,
   	name varchar(255) not null,
   	org_info varchar(255) not null,
  	price float not null,
   	hotel_id int,
   	foreign key (hotel_id) references hotel(id) on delete cascade on update cascade
);

create table if not exists room(
   	id int auto_increment primary key,
   	room_info varchar(255) not null,
   	room_price float not null,
   	room_number varchar(10) not null,
   	status varchar(255) not null,
   	capacity int not null,
   	hotel_id int,
   	foreign key (hotel_id) references hotel(id) on delete cascade on update cascade
);

create table if not exists reservation(
   	id int auto_increment primary key,
   	reservation_date date not null,
   	total_day int not null,
   	total_night int not null,
   	price float not null,
   	customer_id int,
   	foreign key (customer_id) references customer(id) on delete cascade on update cascade
);

create table if not exists room_reservation (
	room_id int,	
	reservation_id int,
   	foreign key (room_id) references room(id),
   	foreign key (reservation_id) references reservation(id)
);

create table if not exists specialroom(
   	id int auto_increment primary key,
   	feature varchar(255) not null,
   	room_id int,
   	foreign key (room_id) references room(id) on delete cascade on update cascade
);

create table if not exists standartroom(
   	id int auto_increment primary key,
   	room_id int,
   	foreign key (room_id) references room(id) on delete cascade on update cascade
);

create table if not exists extraservice (
   	id int auto_increment primary key,
   	service varchar(255) not null,
   	service_price float not null,
   	service_point int
);

create table if not exists room_extraservice (
	room_id int,	
	service_id int,
   	foreign key (room_id) references room(id),
   	foreign key (service_id) references extraservice(id)
);

create table if not exists foodservice (
   	id int auto_increment primary key,
   	food_detail varchar(255) not null,
   	service_id int,
   	foreign key (service_id) references extraservice(id) on delete cascade on update cascade
);

/*---PROCEDURES---*/
drop procedure if exists addbalance;
delimiter $$
create procedure addbalance(in balance_money float, in balance_date date, out balance_id integer)
begin
	insert into balance(money, balance_date) values(balance_money, balance_date);
	set balance_id := (select max(id) from balance);
end;
delimiter ;

drop procedure if exists updatebalance;
delimiter $$
create procedure updatebalance(in balance_id integer, in balance_money float, in balance_date date)
begin
	if exists(select * from balance where id=balance_id) then 
		update balance set balance.money=money, balance.balance_date=balance_date where balance.id=balance_id; 
	end if;
end;
delimiter ;

drop procedure if exists deletebalance;
delimiter $$
create procedure deletebalance(in balance_id integer)
begin
	if exists(select * from balance where id=balance_id) then 
		delete from balance where id=balance_id;
	end if;
end;
delimiter ;

drop procedure if exists addhotel;
delimiter $$
create procedure addhotel(in name varchar(200), in address varchar(255), in telephone varchar(20), in hotel_info varchar(255),
	in star int, in hotel_type varchar(150))
begin
	if not exists (select * from hotel where hotel.name=name) then
		call addbalance(null, curdate(), @balance_id);
		insert into hotel(name, address, telephone, hotel_info, star, hotel_type, balance_id)
		values(name, address, telephone, hotel_info, star, hotel_type, (select @balance_id));
	end if;
end
delimiter ;

drop procedure if exists updatehotel;
delimiter $$
create procedure updatehotel(in hotel_id integer, in name varchar(200), in address varchar(255), in telephone varchar(20),
	in hotel_info varchar(255), in star int, in hotel_type varchar(150), in balance_money float)
begin
	if exists (select * from hotel where id=hotel_id) then
		update hotel set hotel.address=address, hotel.telephone=telephone, hotel.hotel_info=hotel_info, hotel.star=star,
			hotel.hotel_type=hotel_type where hotel.id=hotel_id;
		update balance set balance.money=balance_money, balance.balance_date=curdate()
			where (select balance_id from hotel where id=hotel_id);
	end if;
end
delimiter ;

drop procedure if exists deletehotel;
delimiter $$
create procedure deletehotel(in hotel_id integer)
begin
	if exists (select * from hotel where id=hotel_id) then
		delete from hotel where id=hotel_id;
	end if;
end
delimiter ;

drop procedure if exists addperson;
delimiter $$
create procedure addperson(in firstname varchar(100), in lastname varchar(100), in passwrd varchar(255), in mail varchar(255),
	in address varchar(255), in phone varchar(20), in age integer, in salary float, in username varchar(150),
	in hotel_name varchar(200), in person_type varchar(20))
begin
	declare id INT DEFAULT 0;
	if not exists (select * from person p where p.email = mail or p.telephone = phone) then
	   	case person_type
	   	when 'customer' then
	   		begin
		   		call addbalance(salary, curdate(), @balance_id);
	   			insert into person(firstname, lastname, passwrd, email, address, telephone, balance_id)
	   			values(firstname, lastname, passwrd, mail, address, phone, (select @balance_id));
				select p.id into id from person p where p.email = mail;
	    		insert into customer(age, username, person_id) values(age, username, id); 
				if not exists (select * from customer c where c.person_id=id) then
					delete from person p where p.id=id;
					delete from balance b where b.id=(select @balance_id);
				end if;
			end;
		when 'employee' then
			begin
				declare hotel_id INT DEFAULT 0;
		   		call addbalance(salary, curdate(), @balance_id);
	   			insert into person(firstname, lastname, passwrd, email, address, telephone, balance_id)
	   			values(firstname, lastname, passwrd, mail, address, phone, (select @balance_id));
				select distinct p.id into id from person p where p.email = mail;
				select distinct h.id into hotel_id from hotel h where h.name = hotel_name;
				insert into employee(salary, hotel_id, person_id) values(salary, hotel_id, id);
				if not exists (select * from employee e where e.person_id=id) then
					delete from person p where p.id=id;
					delete from balance b where b.id=(select @balance_id);
				end if;
			end;
		when 'manager' then
			begin
		   		declare hotel_id INT DEFAULT 0;
		   		call addbalance(salary, curdate(), @balance_id);
	   			insert into person(firstname, lastname, passwrd, email, address, telephone, balance_id)
	   			values(firstname, lastname, passwrd, mail, address, phone, (select @balance_id));
				select distinct p.id into id from person p where p.email = mail;
				select distinct h.id into hotel_id from hotel h where h.name = hotel_name;
				insert into manager(salary, hotel_id, person_id) values(salary, hotel_id, id);
				if not exists (select * from manager m where m.person_id=id) then
					delete from person p where p.id=id;
					delete from balance b where b.id=(select @balance_id);
				end if;
			end;
		end case;
	end if;
end
delimiter ;

drop procedure if exists updateperson;
delimiter $$
create procedure updateperson(in person_id integer, in firstname varchar(100), in lastname varchar(100), in passwrd varchar(255),
	in mail varchar(255), in address varchar(255), in phone varchar(20), in age integer, in salary float, in username varchar(150),
	in person_type varchar(20))
begin
	declare id INT DEFAULT 0;
	declare balance INT DEFAULT 0;
	if exists (select * from person p where p.id=person_id) then
	   	case person_type
	   	when 'customer' then
	   		begin
		   		select c.id into id from customer c where c.username=username;
				select b.id into balance from balance b, person p where p.balance_id=b.id and p.id=person_id;
	    		update person set person.firstname=firstname, person.lastname=lastname, person.passwrd=passwrd,
	    			person.email=mail, person.address=address, person.telephone=phone where person.id=person_id;
	    		update customer set customer.age=age, customer.username=username where customer.id=id;
	    		update balance set balance.balance_date=curdate(), balance.money=money where balance.id=balance;
			end;
		when 'employee' then
			begin
		   		select e.id into id from employee e where e.person_id=person_id;
				select b.id into balance from balance b, person p where p.balance_id=b.id and p.id=person_id;
	    		update person set person.firstname=firstname, person.lastname=lastname, person.passwrd=passwrd,
	    			person.email=mail, person.address=address, person.telephone=phone where person.id=person_id;
	    		update employee set employee.salary=salary where employee.id=id;
	    		update balance set balance.balance_date=curdate(), balance.money=money where balance.id=balance;
			end;
		when 'manager' then
			begin
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

drop procedure if exists deleteperson;
delimiter $$
create procedure deleteperson(in person_id integer)
begin
	declare balance_id INT DEFAULT 0;
	if exists (select * from person p where p.id = person_id) then
		select b.id into balance_id from balance b where b.id = (select balance_id from person p where p.id = person_id);
		delete from person where id = person_id;
	   	delete from balance where id = balance_id;
	end if;
end
delimiter ;

drop procedure if exists addroom;
delimiter $$
create procedure addroom(in room_info varchar(255), in room_price float, in room_number varchar(10), in status varchar(255),
	in capacity integer, in feature varchar(255), in hotel_name varchar(200), in room_type varchar(25))
begin
	declare room_id INT DEFAULT 0;
	declare hotel_id INT DEFAULT 0;
	if exists (select * from hotel h where h.name = hotel_name) then
		select distinct h.id into hotel_id from hotel h where h.name = hotel_name;
	   	case room_type
	   	when 'special' then
	   		begin
				if not exists (select * from room r where r.room_number=concat(hotel_id, '-1-', room_number) and r.hotel_id=hotel_id) then 
					insert into room(room_info, room_price, room_number, status, capacity, hotel_id)
					values(room_info, room_price, concat(hotel_id, '-1-', room_number), status, capacity, hotel_id);
					select distinct r.id into room_id from room r where r.hotel_id=hotel_id and r.room_number=concat(hotel_id, '-1-', room_number);
					insert into specialroom(feature, room_id) values(feature, room_id);
				end if;
		   	end;
	   	when 'standart' then
	   		begin
				if not exists (select * from room r where r.room_number=concat(hotel_id, '-0-', room_number) and r.hotel_id=hotel_id) then
					insert into room(room_info, room_price, room_number, status, capacity, hotel_id)
					values(room_info, room_price, concat(hotel_id, '-0-', room_number), status, capacity, hotel_id);
					select distinct r.id into room_id from room r where r.hotel_id=hotel_id and r.room_number=concat(hotel_id, '-0-', room_number);
					insert into standartroom(room_id) values(room_id);
				end if;
		   	end;
		end case;
	end if;
end
delimiter ;

drop procedure if exists updateroom;
delimiter $$
create procedure updateroom(in room_id integer, in room_info varchar(255), in room_price float, in status varchar(255),
	in capacity integer, in feature varchar(255), in room_type varchar(25))
begin
	if exists (select * from room r where r.id=room_id) then
	   	case room_type
	   	when 'special' then
	   		begin
	    		update room set room.room_info=room_info, room.room_price=room_price, room.status=status, room.capacity=capacity where room.id=room_id;
				update specialroom set specialroom.feature=feature where specialroom.room_id=room_id;
		   	end;
	   	when 'standart' then
	   		begin
				update room set room.room_info=room_info, room.room_price=room_price, room.status=status, room.capacity=capacity where room.id=room_id;
		   	end;
		end case;
	end if;
end
delimiter ;

drop procedure if exists deleteroom;
delimiter $$
create procedure deleteroom(in room_id integer)
begin
	if exists (select * from room where id = room_id) then
	   	delete from room where id = room_id;
	end if;
end
delimiter ;

drop procedure if exists addreservation;
delimiter $$
create procedure addreservation(in reservation_date date, in total_day integer, in total_night integer, in price float,
	in customer_id integer, in room_id integer)
begin
	declare reservation_id INT DEFAULT 0;
	if not exists (select * from reservation r where r.reservation_date=reservation_date and r.total_day=total_day
		and r.total_night=total_night) then
		if exists (select * from customer c where c.id=customer_id) then
			if exists (select * from room r where r.id=room_id) then
				insert into reservation(reservation_date, total_day, total_night, price, customer_id)
				values(reservation_date, total_day, total_night, price, customer_id);
				select id into reservation_id from reservation r where r.reservation_date=reservation_date
					and r.total_day=total_day and r.total_night=total_night;
				insert into room_reservation(room_id, reservation_id) values(room_id, reservation_id);
			end if;
		end if;
	end if;
end
delimiter ;

drop procedure if exists updatereservation;
delimiter $$
create procedure updatereservation(in reservation_id integer, in reservation_date date, in total_day integer,
	in total_night integer, in price float, in room_id integer)
begin
	declare reservation_id INT DEFAULT 0;
	if exists (select * from reservation r where r.id=reservation_id) then
		update reservation set reservation.reservation_date=reservation_date, reservation.total_day=total_day,
			reservation.total_night=total_night, reservation.price=price where reservation.id=reservation_id;
		update room_reservation set room_reservation.reservation_id=reservation_id, room_reservation.room_id=room_id;
	end if;
end
delimiter ;

drop procedure if exists deletereservation;
delimiter $$
create procedure deletereservation(in reservation_id integer)
begin
	if exists (select * from reservation r where r.id=reservation_id) then
		delete from reservation r where r.id=reservation_id;
	end if;
end
delimiter ;

drop procedure if exists addorganization;
delimiter $$
create procedure addorganization(in name varchar(255), in org_info varchar(255), in price float, in hotel_name varchar(200))
begin
	declare hotel_id INT DEFAULT 0;
	if not exists (select * from organization o where o.name=name and o.org_info=org_info) then
		if exists (select * from hotel h where h.name=hotel_name) then
			select distinct h.id into hotel_id from hotel h where h.name = hotel_name;
			insert into organization(name, org_info, price, hotel_id) values(name, org_info, price, hotel_id);
		end if;
	end if;
end
delimiter ;

drop procedure if exists updateorganization;
delimiter $$
create procedure updateorganization(in organization_id integer, in name varchar(255), in org_info varchar(255), in price float)
begin
	if exists (select * from organization o where o.id=organization_id) then
		update organization set organization.name=name, organization.org_info=org_info, organization.price=price where organization.id=organization_id;
	end if;
end
delimiter ;

drop procedure if exists deleteorganization;
delimiter $$
create procedure deleteorganization(in organization_id integer)
begin
	if exists (select * from organization o where o.id=organization_id) then
		delete from organization o where o.id=organization_id;
	end if;
end
delimiter ;

drop procedure if exists addextraservice;
delimiter $$
create procedure addextraservice(in service varchar(255), in service_price float, in service_point integer, in room_id integer,
	out service_id integer)
begin
	if not exists (select * from extraservice e, room_extraservice re where e.id=re.service_id and re.room_id=room_id and e.service=service) then
		if exists (select * from room r where r.id=room_id) then
			insert into extraservice(service, service_price, service_point) values(service, service_price, service_point);
			set service_id := (select MAX(id) from extraservice);
			insert into room_extraservice(room_id, service_id) values(room_id, (select MAX(id) from extraservice));
		end if;
	end if;
end
delimiter ;

drop procedure if exists updateextraservice;
delimiter $$
create procedure updateextraservice(in service_id integer, in service varchar(255), in service_price float,
	in service_point integer, in room_id integer)
begin
	if exists (select * from extraservice e, room_extraservice re where e.id=re.service_id and re.room_id=room_id and e.service=service) then
		update extraservice set extraservice.service=service, extraservice.service_point=service_point, 
			extraservice.service_price=service_price where extraservice.id=service_id;
		update room_extraservice set room_extraservice.service_id=service_id where room_extraservice.room_id=room_id;
	end if;
end
delimiter ;

drop procedure if exists deleteextraservice;
delimiter $$
create procedure deleteextraservice(in service_id integer)
begin
	if exists (select * from extraservice e where e.id=service_id) then
		delete from extraservice e where e.id=service_id;
	end if;
end
delimiter ;

drop procedure if exists addfoodservice;
delimiter $$
create procedure addfoodservice(in service varchar(255), in service_price float, in service_point integer, in food_detail varchar(255),
	in room_id integer)
begin
	if not exists (select * from extraservice e, foodservice f where e.id=f.service_id and e.service=service
		and f.food_detail=food_detail) then
		if exists (select * from room r, specialroom s where r.id=s.room_id and r.id=room_id) then
			call addextraservice(service, service_price, service_point, room_id, @service_id);
			insert into foodservice(food_detail, service_id) values(food_detail, (select @service_id));
		end if;
	end if;
end
delimiter ;

drop procedure if exists updatefoodservice;
delimiter $$
create procedure updatefoodservice(in food_id integer, in service varchar(255), in service_price float, in service_point integer,
	in food_detail varchar(255), in room_id integer)
begin
	if exists (select * from foodservice f where f.id=food_id) then
		call updateextraservice(food_id, service, service_price, service_point, room_id);
		update foodservice set foodservice.food_detail=food_detail where foodservice.id=food_id;
	end if;
end
delimiter ;

drop procedure if exists deletefoodservice;
delimiter $$
create procedure deletefoodservice(in food_id integer)
begin
	if exists (select * from foodservice f where f.id=food_id) then
		delete from foodservice f where f.id=food_id;
	end if;
end
delimiter ;

/*---insert---*/

/*call addbalance(:balance_money, :balance_date)*/
/*call updatebalance(:balance_id, :balance_money, :balance_date)*/
/*call deletebalance(:balance_id)*/

/*call addhotel(:name, :address, :telephone, :hotel_info, :star, :hotel_type)*/
call addhotel('hilton', 'tunali', '5555555', 'ultra zengin', 5, 'lüks otel');
/*call updatehotel(:hotel_id, :name, :address, :telephone, :hotel_info, :star, :hotel_type, :balance_money)
call updatehotel(1, 'hilton', 'kýzýlay', '5555555', 'ultra zengin', 5, 'ultra lüks otel', 1);
call deletehotel(:hotel_id)
call deletehotel(5)*/

/*call addperson(:firstname, :lastname, :passwrd, :mail, :address, :phone, :age, :salary, :username, :hotel_id, :person_type)*/
call addperson('Berat', 'Karataþ', '53937', 'bk@g.c', 'Bursa', '2222', 22, 2214.5, null, 'hilton', 'employee');
call addperson('ali6', 'veli', '123', 'ai@g.c', 'mamak', '131', 21, 222.22, null, 'hilton', 'employee');
call addperson('Ali', 'Veli', '4950', 'av@g.c', 'Ankara', '1111', 20, null, 'aliveli', null, 'customer');
call addperson('Ahmet', 'Iþýk', '0246', 'ai@g.c', 'Amasya', '4444', 18, 50, 'ahmetýþýk', null, 'customer');
call addperson('Mert', 'Mert', '53937', 'mm@g.c', 'Bursa', '1231', 22, 2214.5, null, 'hilton', 'manager');
call addperson('ali4', 'veli', '123', '2@g.c', 'mamak', '3333', 21, 222.22, null, 'hilton', 'manager');
call addperson('Berat2', 'Karataþ2', '53937', 'bk2@g.c', 'Bursa', '22222', 22, 2214.5, null, 'hilton', 'employee');
/*call updateperson(:person_id, :firstname, :lastname, :passwrd, :mail, :address, :phone, :age, :salary, :username, :person_type)
call updateperson(1, 'Ali-U', 'Veli', '4950', 'av@g.c', 'Ankara', '1111', 28, null, 'aliveli', 'customer');
call updateperson(2, 'Berat-U', 'Karataþ', '53937', 'bk@g.c', 'Bursa', '2222', 22, 2214.5, null, 'employee');
call updateperson(3, 'Mert-U', 'Pek', '15995', 'mp@g.c', 'Mersin', '3333', 21, null, null, 'manager');
call deleteperson(:person_id)
call deleteperson(1);*/

/*call addroom(:room_info, :room_price, :room_number, :status, :capacity, :feature, :hotel_name, :room_type)*/
call addroom('hilton', 5555, 5, 'uygun', 4, 'ekstra pahali', 'hilton', 'special');
call addroom('hilton', 5555, 5, 'uygun', 4, 'ekstra ucuz', 'hilton', 'special');
call addroom('hilton', 555, 5, 'uygun', 4, null, 'hilton', 'standart');
call addroom('hilton', 5555, 6, 'uygun', 4, 'ekstra yemekli', 'hilton', 'special');
call addroom('hilton', 555, 52, 'uygun', 4, null, 'hilton', 'standart');
/*call updateperson(:firstname, :lastname, :passwrd, :mail, :address, :phone, :age, :salary, :username, :hotel_name, :person_type)
call updateroom(1, 'hilton', 555, 5, 'uygun', 4, 'ekstra ucuz', 1, 'special');
call updateroom(2, 'hilton', 5555, 6, 'uygun', 4, 'ekstra yemeksiz', 1, 'special');
call updateroom(3, 'hilton', 555, 52, 'uygun', 4, null, 1, 'standart');
call deleteroom(:room_id)
call deleteroom(2);*/

/*call addreservation(:reservation_date, :total_day, :total_night, :price, :customer_id, :room_id)*/
call addreservation(curdate(), 8, 10, 1589, 2, 10);
call addreservation(curdate(), 5, 4, 1589, 2, 11);
/*call updatereservation(:reservation_id, :reservation_date, :total_day, :total_night, :price, :customer_id, :room_id)
call updatereservation(1, curdate(), 8, 8, 1589, 1, 3);
call deletereservation(:reservation_id)
call deletereservation(2);*/

/*call addorganization(:name, :org_info, :price, :hotel_name)*/
call addorganization('Murat Boz', 'Ünlü sanaçtý Murat Boz bizlerle', 125, 'hilton');
call addorganization('Murat Koz', 'Ünlü sanaçtý Murat Koz bizlerle', 124, 'hilton');
call addorganization('Murat Kuzu', 'Ünlü sanaçtý Murat Kuzu bizlerle', 123, 'hilton');
/*call updateorganization(:organization_id, :name, :org_info, :price, :hotel_name)
call updateorganization(1, 'Murat Boz', 'Ünlü sanaçtý Murat Boz bizlerle', 1255, 'hilton');
call updateorganization(2, 'Murat Köz', 'Ünlü sanaçtý Murat Köz bizlerle', 1215, 'hilton');
call deleteorganization(:organization_id)
call deleteorganization(2);*/

/*call addextraservice(:service, :service_price, :service_point, :room_id)*/
call addextraservice('temizlik', 55, 0, 11, @service_id);
call addextraservice('taþýma', 55, 3, 12, @service_id);
/*call updateextraservice(:service_id, :service, :service_price, :service_point, :room_id)
call updateextraservice(1, 'temizlik', 55, 2, 1);
call deleteextraservice(:service_id)
call deleteextraservice(2);*/

/*call addfoodservice(:service, :service_price, :service_point, :food_detail, :room_id)*/
call addfoodservice('kahvaltý', 55, 0, 'açýk büfe kahvaltý', 10);
call addfoodservice('akþam yemeði', 155, 4, '4 çeþit yemek', 12);
/*call updatefoodservice(:food_id, :service, :service_price, :service_point, :food_detail, :room_id)
call updatefoodservice(1, 'kahvaltý', 55, 0, 'dolu dolu anadolu kahvaltý', 1);
call deletefoodservice(:food_id)
call deletefoodservice(1);*/