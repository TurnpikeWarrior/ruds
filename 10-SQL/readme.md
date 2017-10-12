## 10-SQL Homework Assignment 

1a. `select * from actor`  
1b. ``

2a. `select actor_id, first_name, last_name from actor where first_name like "%Joe%"`  
2b. `select last_name, first_name from actor where last_name like "%GEN%"`  
2c. `select last_name, first_name from actor where last_name like "%LI%" order by last_name asc, first_name asc`  
2d. `select country_id, country from country where country in ('Afghanistan', 'Bangladesh', 'China')`  

3a. `alter table actor add middle_name varchar(45) after first_name;`
3b. `alter table actor modify column middle_name blob; `
3c. `alter table actor drop middle_name`

4