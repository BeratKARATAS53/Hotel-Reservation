drop view if exists customer_view,employee_view,person_balance,hotel_balance,customer_reservation,manager_view,reservation_view,organization_view,customer_all_info,employee_all_info,manager_all_info;

create view customer_view as
	select p.id,p.firstname,p.lastname,p.passwrd,p.email,p.telephone,p.address,p.balance_id,c.id as customer_id,c.username,c.age
	from customer c,person p
	where c.person_id=p.id;

create view employee_view as
	select p.id,p.firstname,p.lastname,p.passwrd,p.email,p.telephone,p.address,p.balance_id,e.hotel_id,e.id as employee_id,e.salary
	from employee e,person p 
	where e.person_id=p.id;

create view manager_view as
	select p.id,p.firstname,p.lastname,p.passwrd,p.email,p.telephone,p.address,p.balance_id,m.id as manager_id ,m.hotel_id,m.salary
	from manager m,person p 
	where m.person_id=p.id;

create view organization_view as
	select hotel_id,name,price
	from organization o;

create view person_balance as
	select p.id,p.firstname,p.lastname,p.passwrd,b.money,b.balance_date
	from person p,balance b
	where p.balance_id=b.id;

create view hotel_balance as 
	select h.id,h.name,h.address,h.telephone,h.hotel_info,h.star,h.hotel_type,h.balance_id,b.money,b.balance_date
	from hotel h,balance b
	where h.balance_id=b.id;
	
create view customer_reservation as 
	select cv.id as customer_id,cv.firstname,cv.lastname,cv.username,r.id as reservation_id,r.price,r.start_date,r.finish_date
	from customer_view cv,reservation r
	where cv.customer_id=r.customer_id;

create view reservation_view as 
	select r.id as room_id,r.hotel_id,r.room_price,re.customer_id,re.id, re.start_date,re.finish_date
	from room r,reservation re,room_reservation rr 
	where r.id=rr.room_id and rr.reservation_id=re.id;

create view customer_all_info as 
	select cv.id,cv.firstname,cv.lastname,cv.passwrd,cv.email,cv.telephone,cv.address,cv.balance_id,cv.customer_id,cv.username,cv.age,b.balance_date,b.money
	from customer_view cv,balance b
	where cv.balance_id=b.id;
	
create view employee_all_info as 
	select ev.id,ev.firstname,ev.lastname,ev.passwrd,ev.email,ev.telephone,ev.address,ev.balance_id,ev.employee_id,ev.hotel_id,ev.salary,b.balance_date,b.money
	from employee_view ev,balance b
	where ev.balance_id=b.id;

create view manager_all_info as 
	select ev.id,ev.firstname,ev.lastname,ev.passwrd,ev.email,ev.telephone,ev.address,ev.balance_id,ev.manager_id,ev.hotel_id,ev.salary,b.balance_date,b.money
	from manager_view ev,balance b
	where ev.balance_id=b.id;
