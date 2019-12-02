drop table if exists person, customer, manager, employee, registeredcustomer, balance, hotel, organization,
	room, reservation, room_reservation, specialroom, standartroom, extraservice, room_extraservice, foodservice cascade;

create table balance(
	id serial primary key,
   	money money,
   	date date
);

create table hotel(
   	id serial primary key,
   	name varchar(200) unique not null,
   	address varchar(255) not null,
   	telephone varchar(20) unique not null,
   	hotel_info varchar(255) not null,
   	star int,
   	hotel_type varchar(150) not null,
   	balance_id int references balance(id)
);

create table person(
   	id serial primary key,
   	firstname varchar (100) not null,
   	lastname varchar (100) not null,
   	password varchar (255) not null,
   	email varchar (255) unique not null,
   	address varchar (255) not null,
   	telephone varchar (20) unique not null,
   	balance_id int references balance(id)
);

create table manager(
   	id serial primary key,
   	salary money,
   	hotel_id int references hotel(id)
) inherits (person);

create table employee(
   	id serial primary key,
   	salary money,
   	hotel_id int references hotel(id)
) inherits (person);

create table customer(
   	id serial primary key,
   	age int not null,
   	username varchar(100) not null
) inherits (person);

create table registeredcustomer(
   	id serial primary key,
   	username varchar(100) not null,
   	customer_id int references customer(id)
) inherits (customer);

create table organization(
   	id serial primary key,
   	name varchar(255) not null,
   	org_info varchar(255) not null,
  	price money not null,
   	hotel_id int references hotel(id)
);

create table room(
   	id serial primary key,
   	room_info varchar(255) not null,
   	room_price money not null,
   	number int not null,
   	status varchar(255) not null,
   	capacity int not null,
   	hotel_id int references hotel(id)
);

create table reservation(
   	id serial primary key,
   	reservation_date date not null,
   	total_day int not null,
   	total_night int not null,
   	price money not null,
   	room_id int references room(id),
   	customer_id int references customer(id)
);

create table room_reservation (
   	room_id int references room(id),
   	reservation_id int references reservation(id)
);

create table specialroom(
   	id serial primary key,
   	feature varchar(255) not null,
   	room_id int references room(id)
) inherits (room);

create table standartroom(
   	id serial primary key,
   	room_id int references room(id)
) inherits (room);

create table extraservice (
   	id serial primary key,
   	service varchar(255) not null,
   	service_price money not null,
   	point int
);

create table room_extraservice (
   	room_id int references room(id),
   	service_id int references extraservice(id)
);

create table foodservice (
   	id serial primary key,
   	food varchar(255) not null,
   	food_price money not null,
   	service_id int references extraservice(id)
) inherits (extraservice);

create or replace procedure addbalance(balance_money money, balance_date date)
language 'plpgsql'
as $$
	begin
	    insert into balance(money, date) values(balance_money, balance_date);   
	end
$$;
/*call addbalance(money '255', date '2019-12-01');*/

create or replace procedure addperson(firstname varchar, lastname varchar, password varchar, mail varchar,
	address varchar, phone varchar, age integer, salary money, username varchar, hotel_id int, type varchar)
language 'plpgsql'
as $$
	begin
	   	if not exists (select * from person p where p.email = mail or p.telephone = phone) then
	   		case type
	   		when 'customer' then
	   			begin
	   				insert into balance(money, date) values(salary, now()::date);
	    			insert into customer(firstname, lastname, password, email, address, telephone, balance_id, age, username)
	   				values(firstname, lastname, password, mail, address, phone, (select count(*) from balance), age, username); 
				end;
			when 'employee' then
				begin
	   				insert into balance(money, date) values(salary, now()::date);
					insert into employee(firstname, lastname, password, email, address, telephone, balance_id, salary)
	   				values(firstname, lastname, password, mail, address, phone, (select count(*) from balance), salary);
				end;
			when 'manager' then
				begin
	   				insert into balance(money, date) values(salary, now()::date);
					insert into manager(firstname, lastname, password, email, address, telephone, balance_id, salary)
	   				values(firstname, lastname, password, mail, address, phone, (select count(*) from balance), salary);
				end;
			end case;
		else
			begin
				raise notice 'Email or Telephone are also reserved!';
			end;
		end if;
	end
$$;
create or replace procedure updateperson(firstname varchar, lastname varchar, password varchar, mail varchar,
	address varchar, phone varchar, age integer, salary money, username varchar, type varchar)
language 'plpgsql'
as $$
	begin
	   	if exists (select * from person p where p.email = mail or p.telephone = phone) then
	   		case type
	   		when 'customer' then
	   			begin
		   			int balance_id = select balance_id from customer where email = mail;
	   				call deleteperson(select id from customer where email = mail);
	    			insert into customer(firstname, lastname, password, email, address, telephone, balance_id, age, username)
	   				values(firstname, lastname, password, mail, address, phone, (select count(*) from balance), age, username); 
				end;
			when 'employee' then
				begin
	   				insert into balance(money, date) values(salary, now()::date);
					insert into employee(firstname, lastname, password, email, address, telephone, balance_id, salary)
	   				values(firstname, lastname, password, mail, address, phone, (select count(*) from balance), salary);
				end;
			when 'manager' then
				begin
	   				insert into balance(money, date) values(salary, now()::date);
					insert into manager(firstname, lastname, password, email, address, telephone, balance_id, salary)
	   				values(firstname, lastname, password, mail, address, phone, (select count(*) from balance), salary); 
				end;
			end case;
		else
			begin
				raise notice 'Email or Telephone are also reserved!';
			end;
		end if;
	end
$$;
create or replace procedure deleteperson(person_id integer, type varchar)
language 'plpgsql'
as $$
	begin
	   	if exists (select * from person p where p.id = person_id) then
	   		case type
	   		when 'customer' then
	   			delete from customer where id = person_id; 
			when 'employee' then
	   			delete from employee where id = person_id; 
			when 'manager' then
	   			delete from manager where id = person_id; 
			end case;
		else
			raise notice 'Cannot Find Person';
		end if;
	end
$$;
call addperson('ali0', 'veli', '123', '0@g.c', 'mamk', '555', 21, null, 'aliveli', 'customer');
call addperson('ali1', 'veli', '123', '1@g.c', 'mamk', '111', 21, money '222', null, 'employee');
call addperson('ali2', 'veli', '123', '0@g.c', 'mamk', '555', 21, null, 'aliveli', 'employee');
call addperson('ali3', 'veli', '123', '1@g.c', 'mamk', '111', 21, money '222', null, 'customer');
call addperson('ali4', 'veli', '123', '2@g.c', 'mamk', '222', 21, money '222', null, 'manager');
call addperson('ali5', 'veli', '123', '3@g.c', 'mamk', '525', 21, null, 'aliveli', 'customer');
call addperson('ali6', 'veli', '123', '4@g.c', 'mamk', '131', 21, money '222', null, 'employee');
call deleteperson(5, 'customer');

create or replace procedure addhotel(name varchar, address varchar, telephone varchar, hotel_info varchar, star int,
	hotel_type varchar)
language 'plpgsql'
as $$
	begin
	   	insert into balance(money, date) values(null, null);
	    insert into hotel(name, address, telephone, hotel_info, star, hotel_type, balance_id)
	   	values(name, address, telephone, hotel_info, star, hotel_type,  (select count(*) from balance));   
	end
$$;
call addhotel('hilton', 'kızılay', '5555555', 'ultra zengin', 5, 'lüks otel');
call addhotel('hilton2', 'kızılay', '1111111', 'ultra zengin', 5, 'lüks otel');

create or replace procedure addroom(room_info varchar, room_price money, number integer, status varchar, capacity integer,
	hotel_id integer)
language 'plpgsql'
as $$
	begin
	    insert into room(room_info, room_price, number, status, capacity, hotel_id)
	   	values(room_info, room_price, number, status, capacity, hotel_id);   
	end
$$;
call addroom('hilton', money '5555', 5, 'uygun', 4, 1);
call addroom('hilton', money '5555', 5, 'uygun', 4, 2);

create or replace procedure addspecialroom(room_info varchar, room_price money, number integer, status varchar, capacity integer,
	feature varchar, room_id integer)
language 'plpgsql'
as $$
	
	begin
	    insert into specialroom(room_info, room_price, number, status, capacity, hotel_id, feature, room_id)
	   	values(room_info, room_price, number, status, capacity, (select distinct r.hotel_id from room r where r.id=room_id),
	   		feature, room_id);   
	end
$$;
call addspecialroom('hilton', money '5555', 5, 'uygun', 4, 'ekstra pahalı', 1);

create or replace procedure addstandartroom(room_info varchar, room_price money, number integer, status varchar, capacity integer,
	room_id integer)
language 'plpgsql'
as $$
	begin
	    insert into standartroom(room_info, room_price, number, status, capacity, hotel_id, room_id)
	   	values(room_info, room_price, number, status, capacity, (select distinct r.hotel_id from room r where r.id=room_id), room_id);   
	end
$$;
call addstandartroom('hilton', money '5555', 5, 'uygun', 4, 1);
