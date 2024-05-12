select distinct(f.flavor)
from  first_half as f
join icecream_info as i on f.flavor = i.flavor
where f.total_order > 3000 and i.ingredient_type like "fruit%"
order by total_order desc