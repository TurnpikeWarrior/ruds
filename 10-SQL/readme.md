## 10-SQL Homework Assignment 

1a. `select * from actor`  
1b. `select concat(first_name, ' ', last_name) as 'Actor Name' from actor;`

2a. `select actor_id, first_name, last_name from actor where first_name like "%Joe%"`  
2b. `select last_name, first_name from actor where last_name like "%GEN%"`  
2c. `select last_name, first_name from actor where last_name like "%LI%" order by last_name asc, first_name asc`  
2d. `select country_id, country from country where country in ('Afghanistan', 'Bangladesh', 'China')`  

3a. `alter table actor add middle_name varchar(45) after first_name;`  
3b. `alter table actor modify column middle_name blob;`  
3c. `alter table actor drop middle_name`  

4a. `select count(actor_id), last_name from actor group by last_name`  

4b. 
```  
select last_name, count(*) as cnt  
from actor  
group by last_name  
having cnt >= 2
```  
4c. 
```  
UPDATE actor  
SET first_name = 'HARPO'  
WHERE actor_id = 172;
```  
4d. 
```
update actor 
set first_name = 'GROUCHO'
where actor_id = 172;
```

5a. `show tables;`  

6a. 
```
select staff.first_name, staff.last_name, address.address 
from staff 
inner join address on staff.address_id = address.address_id;
```

6b.  

6c. 

6d. `select count(film_id) from inventory where film_id = 439;`  

6e.

7a. `select title from film where (title like "K%" OR title like "Q%") AND language_id = 1;`  

7b. 
```
select first_name, last_name 
from actor 
where actor_id in 
(
	select actor_id 
	from film_actor 
	where film_id in
	(
		select film_id 
		from film 
		where title = 'Alone Trip'
	)
);
```

7c. 

7d.

7e.

7f.

7g.

7h.

8a. 

8b. 

8c. 