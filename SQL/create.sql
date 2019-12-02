DROP TABLE IF EXISTS PERSON, CUSTOMER, MANAGER, EMPLOYEE, REGISTEREDCUSTOMER, BALANCE, HOTEL, ORGANIZATION,
	ROOM, RESERVATION, ROOM_RESERVATION, SPECIALROOM, STANDARTROOM, EXTRASERVICE, ROOM_EXTRASERVICE, FOODSERVICE CASCADE;

CREATE TABLE BALANCE(
	ID INT PRIMARY KEY,
   	MONEY MONEY,
   	DATE DATE
);

CREATE TABLE PERSON(
   	ID INT PRIMARY KEY,
   	FIRSTNAME VARCHAR (100) NOT NULL,
   	LASTNAME VARCHAR (100) NOT NULL,
   	PASSWORD VARCHAR (255) NOT NULL,
   	EMAIL VARCHAR (255) UNIQUE NOT NULL,
   	ADDRESS VARCHAR (255) NOT NULL,
   	TELEPHONE VARCHAR (20) UNIQUE NOT NULL,
   	BALANCE_ID INT REFERENCES BALANCE(ID)
);

CREATE TABLE MANAGER(
   	ID INT PRIMARY KEY,
   	SALARY MONEY
) INHERITS (PERSON);

CREATE TABLE EMPLOYEE(
   	ID INT PRIMARY KEY,
   	SALARY MONEY
) INHERITS (PERSON);

CREATE TABLE CUSTOMER(
   	ID INT PRIMARY KEY,
   	AGE INT NOT NULL
) INHERITS (PERSON);

CREATE TABLE REGISTEREDCUSTOMER(
   	ID INT PRIMARY KEY,
   	USERNAME VARCHAR(100) NOT NULL
) INHERITS (CUSTOMER);

CREATE TABLE HOTEL(
   	ID INT PRIMARY KEY,
   	NAME VARCHAR(200) UNIQUE NOT NULL,
   	ADDRESS VARCHAR(255) NOT NULL,
   	TELEPHONE VARCHAR(20) UNIQUE NOT NULL,
   	HOTEL_INFO VARCHAR(255) NOT NULL,
   	STAR INT,
   	HOTEL_TYPE VARCHAR(150) NOT NULL,
   	BALANCE_ID INT REFERENCES BALANCE(ID)
);

CREATE TABLE ORGANIZATION(
   	ID INT PRIMARY KEY,
   	NAME VARCHAR(255) NOT NULL,
   	ORG_INFO VARCHAR(255) NOT NULL,
  	PRICE MONEY NOT NULL,
   	HOTEL_ID INT REFERENCES HOTEL(ID)
);

CREATE TABLE ROOM(
   	ID INT PRIMARY KEY,
   	ROOM_INFO VARCHAR(255) NOT NULL,
   	ROOM_PRICE MONEY NOT NULL,
   	NUMBER INT NOT NULL,
   	STATUS VARCHAR(255) NOT NULL,
   	CAPACITY INT NOT NULL,
   	HOTEL_ID INT REFERENCES HOTEL(ID)
);

CREATE TABLE RESERVATION(
   	ID INT PRIMARY KEY,
   	RESERVATION_DATE DATE NOT NULL,
   	TOTAL_DAY INT NOT NULL,
   	TOTAL_NIGHT INT NOT NULL,
   	PRICE MONEY NOT NULL,
   	ROOM_ID INT REFERENCES ROOM(ID),
   	CUSTOMER_ID INT REFERENCES CUSTOMER(ID)
);

CREATE TABLE ROOM_RESERVATION (
   	ROOM_ID INT REFERENCES ROOM(ID),
   	RESERVATION_ID INT REFERENCES RESERVATION(ID)
);

CREATE TABLE SPECIALROOM(
   	ID INT PRIMARY KEY,
   	FEATURE VARCHAR(255) NOT NULL
) INHERITS (ROOM);

CREATE TABLE STANDARTROOM(
   	ID INT PRIMARY KEY
) INHERITS (ROOM);

CREATE TABLE EXTRASERVICE (
   	ID INT PRIMARY KEY,
   	SERVICE VARCHAR(255) NOT NULL,
   	SERVICE_PRICE MONEY NOT NULL,
   	POINT INT
);

CREATE TABLE ROOM_EXTRASERVICE (
   	ROOM_ID INT REFERENCES ROOM(ID),
   	SERVICE_ID INT REFERENCES EXTRASERVICE(ID)
);

CREATE TABLE FOODSERVICE (
   	ID INT PRIMARY KEY,
   	FOOD VARCHAR(255) NOT NULL,
   	FOOD_PRICE MONEY NOT NULL,
   	SERVICE_ID INT REFERENCES EXTRASERVICE(ID)
) INHERITS (EXTRASERVICE);

/*BALANCE TABLE PROCEDURES*/
CREATE OR REPLACE PROCEDURE AddBalance(id integer, balance_money money, balance_date date)
LANGUAGE 'plpgsql'
AS $$
	BEGIN
	    INSERT INTO BALANCE(ID, MONEY, DATE) VALUES(id, balance_money, balance_date);   
	END
$$;
CREATE OR REPLACE PROCEDURE UpdateBalance(balance_id integer, balance_money money, balance_date date)
LANGUAGE 'plpgsql'
AS $$
	BEGIN
		DELETE FROM BALANCE b WHERE b.id = balance_id;
	    INSERT INTO BALANCE(ID, MONEY, DATE) VALUES(balance_id, balance_money, balance_date);
	END
$$;
CREATE OR REPLACE PROCEDURE DeleteBalance(balance_id integer)
LANGUAGE 'plpgsql'
AS $$
	BEGIN
		DELETE FROM BALANCE b WHERE b.id = balance_id; 
	END
$$;
CALL AddBalance(1, money '255', date '2019-12-01');
CALL AddBalance(2, money '55', date '2019-12-01');
CALL AddBalance(3, money '5', date '2019-12-01');
CALL AddBalance(4, money '2', date '2019-12-01');

/*PERSON TABLE PROCEDURES
CREATE OR REPLACE PROCEDURE AddPerson(id integer, firstname varchar, lastname varchar, password varchar, email varchar,
	address varchar, telephone varchar, balance_id integer)
LANGUAGE 'plpgsql'
AS $$
	BEGIN
	    INSERT INTO PERSON(ID, FIRSTNAME, LASTNAME, PASSWORD, EMAIL, ADDRESS, TELEPHONE, BALANCE_ID)
	   	VALUES(id, firstname, lastname, password, email, address, telephone, balance_id);   
	END
$$;

CALL AddPerson(1, 'ali', 'VELÝ', '123', '1@g.c', 'mamak', '111', 1);
CALL AddPerson(2, 'ali', 'VELÝ', '123', '2@g.c', 'mamak', '222', 2);
CALL AddPerson(3, 'ali', 'VELÝ', '123', '3@g.c', 'mamak', '333', 3);
CALL AddPerson(4, 'ali', 'VELÝ', '123', '4@g.c', 'mamak', '444', 4);
*/
CREATE OR REPLACE PROCEDURE AddCustomer(id integer, firstname varchar, lastname varchar, password varchar, email varchar,
	address varchar, telephone varchar, balance_id integer, age integer)
LANGUAGE 'plpgsql'
AS $$
	BEGIN
		INSERT INTO CUSTOMER(ID, FIRSTNAME, LASTNAME, PASSWORD, EMAIL, ADDRESS, TELEPHONE, BALANCE_ID, AGE)
	   	VALUES(id, firstname, lastname, password, email, address, telephone, balance_id, age);   
	END
$$;
CALL AddCustomer(1, 'ali', 'VELÝ', '123', '0@g.c', 'mamak', '555', 1, 21);
CALL AddCustomer(2, 'al2', 'VELÝ2', '1232', '02@g.c', 'mamak2', '5552', 2, 14);
/*
CREATE OR REPLACE PROCEDURE AddRegisteredCustomer(id integer, firstname varchar, lastname varchar, password varchar, email varchar,
	address varchar, telephone varchar, balance_id integer, age integer, username varchar, person_id integer)
LANGUAGE 'plpgsql'
AS $$
	BEGIN
	    INSERT INTO REGISTEREDCUSTOMER(ID, FIRSTNAME, LASTNAME, PASSWORD, EMAIL, ADDRESS, TELEPHONE, BALANCE_ID, AGE, USERNAME, PERSON_ID)
	   	VALUES(id, firstname, lastname, password, email, address, telephone, balance_id, age, username, person_id);   
	END
$$;
CALL AddRegisteredCustomer(1, 'ali', 'VELÝ', '123', '0@g.c', 'mamak', '555', 1, 21, 'aliVeli', 1);
*/
CREATE OR REPLACE PROCEDURE AddEmployee(id integer, firstname varchar, lastname varchar, password varchar, email varchar,
	address varchar, telephone varchar, balance_id integer, salary money)
LANGUAGE 'plpgsql'
AS $$
	BEGIN
	    INSERT INTO EMPLOYEE(ID, FIRSTNAME, LASTNAME, PASSWORD, EMAIL, ADDRESS, TELEPHONE, BALANCE_ID, SALARY)
	   	VALUES(id, firstname, lastname, password, email, address, telephone, balance_id, salary); 
	END
$$;
CALL AddEmployee(2, 'ali', 'VELÝ', '123', '0@g.c', 'mamak', '555', 2, money '2555');

CREATE OR REPLACE PROCEDURE AddManager(id integer, firstname varchar, lastname varchar, password varchar, email varchar,
	address varchar, telephone varchar, balance_id integer, salary money)
LANGUAGE 'plpgsql'
AS $$
	BEGIN
	    INSERT INTO MANAGER(ID, FIRSTNAME, LASTNAME, PASSWORD, EMAIL, ADDRESS, TELEPHONE, BALANCE_ID, SALARY)
	   	VALUES(id, firstname, lastname, password, email, address, telephone, balance_id, salary); 
	END
$$;
CALL AddManager(3, 'ali', 'VELÝ', '123', '0@g.c', 'mamak', '555', 3, money '21');

CREATE OR REPLACE PROCEDURE AddHotel(id integer, name varchar, address varchar, telephone varchar, hotel_info varchar, star int,
	hotel_type varchar, balance_id integer)
LANGUAGE 'plpgsql'
AS $$
	BEGIN
	    INSERT INTO HOTEL(ID, NAME, ADDRESS, TELEPHONE, HOTEL_INFO, STAR, HOTEL_TYPE, BALANCE_ID)
	   	VALUES(id, name, address, telephone, hotel_info, star, hotel_type, balance_id);   
	END
$$;
CALL AddHotel(1, 'hilton', 'kýzýlay', '5555555', 'ultra zengin', 5, 'lüks otel', 4);

CREATE OR REPLACE PROCEDURE AddRoom(id integer, room_info varchar, room_price money, number integer, status varchar,
	capacity integer)
LANGUAGE 'plpgsql'
AS $$
	BEGIN
	    INSERT INTO ROOM(ID, ROOM_INFO, ROOM_PRICE, NUMBER, STATUS, CAPACITY)
	   	VALUES(id, room_info, room_price, number, status, capacity);   
	END
$$;
CALL AddRoom(1, 'hilton', money '5555', 5, 'uygun', 4);

CREATE OR REPLACE PROCEDURE AddSpecialRoom(id integer, room_info varchar, room_price money, number integer, status varchar,
	capacity integer, feature varchar)
LANGUAGE 'plpgsql'
AS $$
	
	BEGIN
	    INSERT INTO SPECIALROOM(ID, ROOM_INFO, ROOM_PRICE, NUMBER, STATUS, CAPACITY, FEATURE)
	   	VALUES(id, room_info, room_price, number, status, capacity, feature);   
	END
$$;
CALL AddSpecialRoom(1, 'hilton', money '5555', 5, 'uygun', 4, 'ekstra pahalý');

CREATE OR REPLACE PROCEDURE AddStandartRoom(id integer, room_info varchar, room_price money, number integer, status varchar,
	capacity integer)
LANGUAGE 'plpgsql'
AS $$
	BEGIN
	    INSERT INTO STANDARTROOM(ID, ROOM_INFO, ROOM_PRICE, NUMBER, STATUS, CAPACITY)
	   	VALUES(id, room_info, room_price, number, status, capacity);   
	END
$$;
CALL AddStandartRoom(1, 'hilton', money '5555', 5, 'uygun', 4);
