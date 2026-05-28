select A.name as Employee
from Employee A 
join Employee B
on B.id = A.managerID
where A.salary>B.salary;