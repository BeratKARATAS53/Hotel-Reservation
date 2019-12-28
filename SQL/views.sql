drop view if exists customer_view,employee_view,person_balance,customer_reservation,hotel_view,manager_view,reservation_view,organization_view;

create view customer_view as
	select p.id,p.firstname,p.lastname,c.username,p.passwrd,c.id as customer_id
	from customer c,person p
	where c.person_id=p.id;

create view employee_view as
	select p.id,p.firstname,p.lastname,e.hotel_id,p.balance_id,p.passwrd
	from employee e,person p 
	where e.person_id=p.id;

create view manager_view as
	select p.id,p.firstname,p.lastname,p.balance_id,p.passwrd
	from manager m,person p 
	where m.person_id=p.id;

create view organization_view as
	select hotel_id,name,price
	from organization o;

create view person_balance as
	select p.id,p.firstname,p.lastname,p.passwrd,b.money,b.balance_date
	from person p,balance b
	where p.balance_id=b.id;

create view hotel_view as
	select h.id,h.name,h.address,h.telephone,h.hotel_info,h.star,h.hotel_type,b.money
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

	