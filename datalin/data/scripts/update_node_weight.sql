--select * from datalin_node;

update datalin_node 
	set weight = a.weight
from  (
	select node_id, count(*) as weight
	from (
		select node_a_id as node_id  
		from datalin_relation
		union all
		select node_b_id as node_id  
		from datalin_relation 
	) b 
	group by node_id
) a
where a.node_id = datalin_node.id
	and coalesce(datalin_node.weight, -1) != a.weight
;
	