# SQL Interview Prep Questions

Giving the table structure:
```
Employee
  int      id
  string   first_name
  string   last_name
  string   ssn
  datetime hire_date

Employees_Departments
  int   id
  int   employee_id
  int   department_id

Department
  int      id
  string   name
```

### Get me the list of employees that were hired, ordered by the date, from most recent.
```sql
SELECT first_name, last_name
FROM Employee
ORDER BY hire_date ASC
```

### Delete all employees that were hired more than 3 years ago.

dates in mysql are in the form Y-m-d H:i:s . e.g. '2015-31-01 12:00:00', so you can technically use a direct date string. The preferred method is probably using the date methods
but both ways will work.
```sql
DELETE FROM Employee
WHERE hire_date < DATE_SUB( CURDATE(), '3 YEAR');
DELETE FROM Employee
WHERE hire_date < "2013-05-01 00:00:00"
```

### Get me all the employees from the Departments "Hiring", "Firing", "Rehiring"

```sql
SELECT *
FROM Employee
JOIN Employees_Departments
  ON Employee.id = Employees_Departments.employee_id
JOIN Department
  ON Employees_Departments.department_id = Department.id
WHERE Department.name IN ("Hiring", "Firing", "Rehiring")
```
