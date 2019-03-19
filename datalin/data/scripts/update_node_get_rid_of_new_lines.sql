update datalin_node
	set name =  replace(replace(name,chr(10),''),chr(13),'')
	, display_name =  replace(replace(display_name,chr(10),''),chr(13),'')
where name like '%' || chr(10) || '%' 
	or name like '%' || chr(13) || '%'
;

select * from datalin_node where name = 'CHASSISERIE_TGT';
select * from datalin_relation where node_a_id = 5604;

delete from datalin_node where id = 5742;
delete from datalin_relation where node_b_id = 5742;

select * from datalin_node where name like '%' || chr(10) || '%' 
	or name like '%' || chr(13) || '%'
	