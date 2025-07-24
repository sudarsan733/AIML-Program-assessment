use employees;
select * from salary;


DROP TABLE IF EXISTS salary;
CREATE TABLE salary (
    empid INT,
    firstname VARCHAR(100),
    lastname VARCHAR(100),
    email VARCHAR(50),
    phone VARCHAR(15),
    hire_date DATE,
    job_id VARCHAR(15),
    salary INT
);