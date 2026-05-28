select max(num) as num 
from( 
    select num
    from MyNumbers
    Group by num
    having count(num) = 1)
as unique_num;