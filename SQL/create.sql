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

create table if not exists hotel_deleted(
   	id int auto_increment primary key,
   	name varchar (100) not null,
   	address varchar (100) not null,
   	date_time timestamp
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
   	p_role varchar(50) not null,
   	image varchar (255),
   	foreign key (balance_id) references balance(id) on update cascade
);

create table if not exists person_deleted(
   	id int auto_increment primary key,
   	firstname varchar (100) not null,
   	lastname varchar (100) not null,
   	email varchar (255) unique not null,
   	date_time timestamp
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
   	image varchar(255),
   	foreign key (hotel_id) references hotel(id) on delete cascade on update cascade
);

create table if not exists rent_organization(
	customer_id int,	
	organization_id int,
   	foreign key (customer_id) references customer(id) on delete cascade,
   	foreign key (organization_id) references organization(id) on delete cascade
);

create table if not exists room(
   	id int auto_increment primary key,
   	room_info varchar(255) not null,
   	room_price float not null,
   	room_number varchar(10) not null,
   	status varchar(255) not null,
   	capacity int not null,
   	image varchar(255),
   	hotel_id int,
   	foreign key (hotel_id) references hotel(id) on delete cascade on update cascade
);

create table if not exists room_deleted(
   	id int auto_increment primary key,
   	hotel_id int,
   	room_number varchar(10),
   	date_time timestamp
);

create table if not exists reservation(
   	id int auto_increment primary key,
   	start_date date not null,
   	finish_date date not null,
   	price float,
   	customer_id int,
   	foreign key (customer_id) references customer(id) on delete cascade on update cascade
);

create table if not exists room_reservation (
	room_id int,	
	reservation_id int,
   	foreign key (room_id) references room(id) on delete cascade,
   	foreign key (reservation_id) references reservation(id) on delete cascade
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
   	service_point int,
   	hotel_id int not null
);

create table if not exists extraservice_deleted (
   	id int auto_increment primary key,
   	service varchar(255) not null,
   	hotel_id int not null,
   	date_time timestamp
);

create table if not exists room_extraservice (
	room_id int,
	service_id int,
	service_price float not null,
   	foreign key (room_id) references room(id),
   	foreign key (service_id) references extraservice(id) on delete cascade on update cascade
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
		call addbalance(0, curdate(), @balance_id);
		insert into hotel(name, address, telephone, hotel_info, star, hotel_type, balance_id)
		values(name, address, telephone, hotel_info, star, hotel_type, (select @balance_id));
	end if;
end
delimiter ;

drop procedure if exists updatehotel;
delimiter $$
create procedure updatehotel(in hotel_id integer, in name varchar(200), in address varchar(255), in telephone varchar(20),
	in hotel_info varchar(255), in star int, in hotel_type varchar(150))
begin
	if exists (select * from hotel where id=hotel_id) then
		update hotel set hotel.name=name, hotel.address=address, hotel.telephone=telephone, hotel.hotel_info=hotel_info, hotel.star=star,
			hotel.hotel_type=hotel_type where hotel.id=hotel_id;
	end if;
end
delimiter ;

drop procedure if exists deletehotel;
delimiter $$
create procedure deletehotel(in hotel_id integer)
begin
	declare balance INT DEFAULT 0;
	if exists (select * from hotel where id=hotel_id) then
		select balance_id into balance from hotel h where h.id=hotel_id; 
		delete from hotel where id=hotel_id;
		call deletebalance(balance);
	end if;
end
delimiter ;

drop procedure if exists addperson;
delimiter $$
create procedure addperson(in firstname varchar(100), in lastname varchar(100), in passwrd varchar(255), in mail varchar(255),
	in address varchar(255), in phone varchar(20), in age integer, in salary float, in username varchar(150),
	in hotel_name varchar(200), in image varchar(255), in person_type varchar(50))
begin
	declare id INT DEFAULT 0;
	if not exists (select * from person p where p.email = mail or p.telephone = phone) then
	   	case person_type
	   	when 'customer' then
	   		begin
		   		call addbalance(salary, curdate(), @balance_id);
	   			insert into person(firstname, lastname, passwrd, email, address, telephone, balance_id, p_role, image)
	   			values(firstname, lastname, MD5(passwrd), mail, address, phone, (select @balance_id), person_type, image);
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
				if exists (select * from hotel where hotel.name=hotel_name) then
			   		call addbalance(salary, curdate(), @balance_id);
		   			insert into person(firstname, lastname, passwrd, email, address, telephone, balance_id, p_role, image)
		   			values(firstname, lastname, MD5(passwrd), mail, address, phone, (select @balance_id), person_type, image);
					select distinct p.id into id from person p where p.email = mail;
					select distinct h.id into hotel_id from hotel h where h.name = hotel_name;
					insert into employee(salary, hotel_id, person_id) values(salary, hotel_id, id);
					if not exists (select * from employee e where e.person_id=id) then
						delete from person p where p.id=id;
						delete from balance b where b.id=(select @balance_id);
					end if;
				end if;
			end;
		when 'manager' then
			begin
		   		declare hotel_id INT DEFAULT 0;
				if exists (select * from hotel where hotel.name=hotel_name) then
			   		call addbalance(salary, curdate(), @balance_id);
		   			insert into person(firstname, lastname, passwrd, email, address, telephone, balance_id, p_role, image)
		   			values(firstname, lastname, MD5(passwrd), mail, address, phone, (select @balance_id), person_type, image);
					select distinct p.id into id from person p where p.email = mail;
					select distinct h.id into hotel_id from hotel h where h.name = hotel_name;
					insert into manager(salary, hotel_id, person_id) values(salary, hotel_id, id);
					if not exists (select * from manager m where m.person_id=id) then
						delete from person p where p.id=id;
						delete from balance b where b.id=(select @balance_id);
					end if;
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
	in hotel_name varchar(200), in person_type varchar(20))
begin
	declare id INT DEFAULT 0;
	declare balance INT DEFAULT 0;
	if exists (select * from person p where p.id=person_id and p.email=mail) then
	   	case person_type
	   	when 'customer' then
	   		begin
		   		select c.id into id from customer c where c.username=username;
				select b.id into balance from balance b, person p where p.balance_id=b.id and p.id=person_id;
	    		update person set person.firstname=firstname, person.lastname=lastname, person.passwrd=MD5(passwrd),
	    			person.email=mail, person.address=address, person.telephone=phone where person.id=person_id;
	    		update customer set customer.age=age, customer.username=username where customer.id=id;
	    		update balance set balance.balance_date=curdate(), balance.money=salary where balance.id=balance;
			end;
		when 'employee' then
			begin
		   		select e.id into id from employee e where e.person_id=person_id;
				select b.id into balance from balance b, person p where p.balance_id=b.id and p.id=person_id;
	    		update person set person.firstname=firstname, person.lastname=lastname, person.passwrd=MD5(passwrd),
	    			person.email=mail, person.address=address, person.telephone=phone where person.id=person_id;
	    		update employee set employee.salary=salary where employee.id=id;
	    		update balance set balance.balance_date=curdate(), balance.money=salary where balance.id=balance;
			end;
		when 'manager' then
			begin
		   		select e.id into id from employee e where e.person_id=person_id;
				select b.id into balance from balance b, person p where p.balance_id=b.id and p.id=person_id;
	    		update person set person.firstname=firstname, person.lastname=lastname, person.passwrd=MD5(passwrd),
	    			person.email=mail, person.address=address, person.telephone=phone where person.id=person_id;
	    		update manager set manager.salary=salary where manager.id=id;
	    		update balance set balance.balance_date=curdate(), balance.money=salary where balance.id=balance;
			end;
		end case;
	end if;
end
delimiter ;

drop procedure if exists deleteperson;
delimiter $$
create procedure deleteperson(in person_id integer)
begin
	declare balance INT DEFAULT 0;
	if exists (select * from person p where p.id = person_id) then
		select balance_id into balance from person p where p.id=person_id; 
		delete from person p where p.id=person_id;
		call deletebalance(balance);
	end if;
end
delimiter ;

drop procedure if exists addroom;
delimiter $$
create procedure addroom(in room_info varchar(255), in room_price float, in room_number varchar(10), in status varchar(255),
	in capacity integer, in image varchar(255), in feature varchar(255), in hotel_name varchar(200), in room_type varchar(25))
begin
	declare room_id INT DEFAULT 0;
	declare hotel_id INT DEFAULT 0;
	if exists (select * from hotel h where h.name = hotel_name) then
		select distinct h.id into hotel_id from hotel h where h.name = hotel_name;
	   	case room_type
	   	when 'special' then
	   		begin
				if not exists (select * from room r where r.room_number=concat(hotel_id, '-1-', room_number) and r.hotel_id=hotel_id) then 
					insert into room(room_info, room_price, room_number, status, capacity, image, hotel_id)
					values(room_info, room_price, concat(hotel_id, '-1-', room_number), status, capacity, image, hotel_id);
					select distinct r.id into room_id from room r where r.hotel_id=hotel_id and r.room_number=concat(hotel_id, '-1-', room_number);
					insert into specialroom(feature, room_id) values(feature, room_id);
				end if;
		   	end;
	   	when 'standart' then
	   		begin
				if not exists (select * from room r where r.room_number=concat(hotel_id, '-0-', room_number) and r.hotel_id=hotel_id) then
					insert into room(room_info, room_price, room_number, status, capacity, image, hotel_id)
					values(room_info, room_price, concat(hotel_id, '-0-', room_number), status, capacity, image, hotel_id);
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
create procedure addreservation(in start_date date, in finish_date date, in customer_id integer, in room_number varchar(10), in total_price float)
begin
	declare reservation_id INT DEFAULT 0;
	declare room_id INT DEFAULT 0;
	declare balanceId INT DEFAULT 0;
	declare person_money FLOAT DEFAULT 0;
	if exists (select * from room rm where rm.room_number=room_number) then
		if(strcmp((select status from room rm where rm.room_number=room_number),'available') = 0) then
			select id into room_id from room rm where rm.room_number=room_number;
			if exists (select * from customer c where c.id=customer_id) then
				if not exists (select * from room_reservation rr, reservation r where rr.reservation_id=r.id and rr.room_id=room_id
					and r.start_date=start_date and r.finish_date=finish_date) then
					select balance_id into balanceId from person p, customer c where p.id=c.person_id and c.id=customer_id;
					select money into person_money from balance where id=balanceId;
					if(person_money >= total_price) then
						insert into reservation(start_date, finish_date, price, customer_id)
						values(start_date, finish_date, total_price, customer_id);
						select max(id) into reservation_id from reservation re where re.start_date=start_date and re.finish_date=finish_date;
						insert into room_reservation(room_id, reservation_id) values(room_id, reservation_id);
						update balance set balance.money=person_money-total_price, balance.balance_date=curdate() where balance.id=balanceId;
						update hotel_balance set money=money+total_price where id=(select hotel_id from room where id=room_id);
						delete from room_extraservice res where res.room_id=room_id;
					end if;
				end if;
			end if;
		end if;
	end if;
end
delimiter ;

drop procedure if exists updatereservation;
delimiter $$
create procedure updatereservation(in reservation_id integer, in start_date date, in finish_date date, in customer_id integer,
	in room_number varchar(10))
begin
	declare room_id INT DEFAULT 0;
	declare balanceId INT DEFAULT 0;
	declare person_money FLOAT DEFAULT 0;
	declare room_service_money FLOAT DEFAULT 0;
	declare room_money FLOAT DEFAULT 0;
	declare reservation_money INT DEFAULT 0;
	declare diff_day INT DEFAULT 0;
	declare total_price FLOAT DEFAULT 0;
	set diff_day := (select day(finish_date) - day(start_date));
	if exists (select * from reservation r where r.id=reservation_id) then
		if exists (select * from room rm where rm.room_number=room_number) then
			if(strcmp((select status from room rm where rm.room_number=room_number),'available') = 0) then
				select id into room_id from room rm where rm.room_number=room_number;
				if not exists (select * from room_reservation rr, reservation res where rr.reservation_id=res.id and rr.room_id=room_id
					and res.start_date=start_date and res.finish_date=finish_date) then
					select balance_id into balanceId from person p, customer c where p.id=c.person_id and c.id=customer_id;
					select money into person_money from balance where id=balanceId;
					if exists (select * from room_extraservice roomex where roomex.room_id=room_id) then
						select sum(service_price) into room_service_money from room_extraservice re where re.room_id=room_id;
					end if;
					select room_price into room_money from room where id=room_id;
					set person_money := (select person_money+reservation_money);
					set total_price := (select ((diff_day*room_money)+room_service_money));
					if(person_money >= total_price) then
						delete from reservation r where r.id=reservation_id;
						insert into reservation(start_date, finish_date, price, customer_id)
						values(start_date, finish_date, total_price, customer_id);
						select max(id) into reservation_id from reservation re where re.start_date=start_date and re.finish_date=finish_date;
						insert into room_reservation(room_id, reservation_id) values(room_id, reservation_id);
						update balance set balance.money=person_money-total_price, balance.balance_date=curdate() where balance.id=balanceId;
						delete from room_extraservice res where res.room_id=room_id;
					end if;
				end if;
			end if;
		end if;
	end if;
end
delimiter ;

drop procedure if exists deletereservation;
delimiter $$
create procedure deletereservation(in reservation_id integer)
begin
	declare customerId INT default 0;
	declare balanceId INT default 0;
	declare person_money INT default 0;
	declare reservation_price INT default 0;
	if exists (select * from reservation r where r.id=reservation_id) then
		select customer_id into customerId from reservation r where r.id=reservation_id;
		select balance_id into balanceId from person p, customer c where p.id=c.person_id and c.id=customerId;
		select money into person_money from balance b where b.id=balanceId;
		select price into reservation_price from reservation r where r.id=reservation_id;
		delete from reservation r where r.id=reservation_id;
		update balance set balance.money=person_money+reservation_price where balance.id=balanceId;
	end if;
end
delimiter ;

drop procedure if exists addorganization;
delimiter $$
create procedure addorganization(in name varchar(255), in org_info varchar(255), in price float, in image varchar(255), in hotel_name varchar(200))
begin
	declare hotel_id INT DEFAULT 0;
	if not exists (select * from organization o where o.name=name and o.org_info=org_info) then
		if exists (select * from hotel h where h.name=hotel_name) then
			select distinct h.id into hotel_id from hotel h where h.name = hotel_name;
			insert into organization(name, org_info, price, hotel_id, image) values(name, org_info, price, hotel_id, image);
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

drop procedure if exists addrentorganization;
delimiter $$
create procedure addrentorganization(in customer_id integer, in organization_id integer)
begin
	declare balanceId INT default 0;
	declare balance_money INT default 0;
	declare organization_price INT default 0;
	if not exists (select * from rent_organization ro where ro.customer_id=customer_id and ro.organization_id=organization_id) then
		if exists (select * from organization o where o.id=organization_id) then
			if exists (select * from customer c where c.id=customer_id) then
				select balance_id into balanceId from person p, customer c where p.id=c.person_id and c.id=customer_id;
				select money into balance_money from balance where id=balanceId;
				select price into organization_price from organization where id=organization_id;
				if(balance_money > organization_price) then
					insert into rent_organization(customer_id, organization_id) values(customer_id, organization_id);
					update balance set balance.money=balance_money-organization_price, balance.balance_date=curdate() where balance.id=balanceId;
				end if;
			end if;
		end if;
	end if;
end
delimiter ;

drop procedure if exists deleterentorganization;
delimiter $$
create procedure deleterentorganization(in customer_id integer, in organization_id integer)
begin
	declare balanceId INT default 0;
	declare balance_money INT default 0;
	declare organization_price INT default 0;
	if exists (select * from rent_organization r where r.customer_id=customer_id and r.organization_id=organization_id) then
		select balance_id into balanceId from person p, customer c where p.id=c.person_id and c.id=customer_id;
		select money into balance_money from balance where id=balanceId;
		select price into organization_price from organization where id=organization_id;
		delete from rent_organization r where r.customer_id=customer_id and r.organization_id=organization_id;
		update balance set balance.money=balance_money+organization_price, balance.balance_date=curdate() where balance.id=balanceId;
	end if;
end
delimiter ;

drop procedure if exists addextraservice;
delimiter $$
create procedure addextraservice(in service varchar(255), in service_price float, in service_point integer, in hotel_id int,
	out service_id integer)
begin
	if not exists (select * from extraservice e where e.service=service and e.hotel_id=hotel_id) then
		if exists (select * from hotel h where h.id=hotel_id) then
			insert into extraservice(service, service_price, service_point, hotel_id) values(service, service_price, service_point, hotel_id);
			set service_id := (select MAX(id) from extraservice);
		end if;
	end if;
end
delimiter ;

drop procedure if exists updateextraservice;
delimiter $$
create procedure updateextraservice(in service_id integer, in service varchar(255), in service_price float, in service_point integer,
	in hotel_id int)
begin
	if exists (select * from extraservice e where e.service=service and e.hotel_id=hotel_id) then
		update extraservice set extraservice.service=service, extraservice.service_point=service_point, 
			extraservice.service_price=service_price where extraservice.id=service_id;
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
	in hotel_id int)
begin
	if not exists (select * from extraservice e where e.service=service and e.hotel_id=hotel_id) then
		call addextraservice(service, service_price, service_point, hotel_id, @service_id);
		insert into foodservice(food_detail, service_id) values(food_detail, (select @service_id));
	end if;
end
delimiter ;

drop procedure if exists updatefoodservice;
delimiter $$
create procedure updatefoodservice(in food_id integer, in service varchar(255), in service_price float, in service_point integer,
	in food_detail varchar(255), in hotel_id int)
begin
	declare serviceId INT default 0;
	if exists (select * from foodservice f where f.id=food_id) then
		select service_id into serviceId from foodservice f where f.id=food_id;
		call updateextraservice(serviceId, service, service_price, service_point, hotel_id);
		update foodservice set foodservice.food_detail=food_detail where foodservice.id=food_id;
	end if;
end
delimiter ;

drop procedure if exists deletefoodservice;
delimiter $$
create procedure deletefoodservice(in food_id integer)
begin
	declare serviceId INT DEFAULT 0;
	if exists (select * from foodservice f where f.id=food_id) then
		select service_id into serviceId from foodservice f where f.id=food_id;
		call deleteextraservice(serviceId);
	end if;
end
delimiter ;

drop procedure if exists addroom_extraservice;
delimiter $$
create procedure addroom_extraservice(in room_id integer, in service_id integer)
begin
	declare service_money FLOAT DEFAULT 0;
	if not exists (select * from room_extraservice re where re.room_id=room_id and re.service_id=service_id) then
		if(strcmp((select hotel_id from extraservice e where e.id=service_id),(select substring_index(room_number,'-',1) from room where id=room_id)) = 0) then
			select service_price into service_money from extraservice e where e.id=service_id;
			insert into room_extraservice(room_id, service_id, service_price) values(room_id, service_id, service_money);
		end if;
	end if;
end
delimiter ;

drop procedure if exists deleteroom_extraservice;
delimiter $$
create procedure deleteroom_extraservice(in room_id integer, in service_id integer)
begin
	declare service_money FLOAT DEFAULT 0;
	if exists (select * from room_extraservice re where re.room_id=room_id and re.service_id=service_id) then
		delete from room_extraservice re where re.room_id=room_id and re.service_id=service_id;
	end if;
end
delimiter ;


/*----TRIGGERS----*/
drop trigger if exists hotel_deleted
delimiter $$
create trigger hotel_deleted after delete on hotel for each row
begin
	insert into hotel_deleted(name, address, date_time) values (old.name, old.address, current_timestamp());
end
delimiter ;

drop trigger if exists person_deleted
delimiter $$
create trigger person_deleted after delete on person for each row
begin
	insert into person_deleted(firstname, lastname, email, date_time) values (old.firstname, old.lastname, old.email, current_timestamp());
end
delimiter ;

drop trigger if exists room_deleted
delimiter $$
create trigger room_deleted after delete on room for each row
begin
	insert into room_deleted(hotel_id, room_number, date_time) values (old.hotel_id, old.room_number, current_timestamp());
end
delimiter ;

drop trigger if exists extraservice_deleted
delimiter $$
create trigger extraservice_deleted after delete on extraservice for each row
begin
	insert into extraservice_deleted(service, hotel_id, date_time) values (old.service, old.hotel_id, current_timestamp());
end
delimiter ;

