SELECT Department.name as Department,
Employee.name as Employee, 
employee.salary as Salary
FROM Employee
join department
on Employee.departmentid = Department.id
where Employee.salary =
(Select max(salary) 
from Employee e
where e.departmentId=Employee.departmentID);