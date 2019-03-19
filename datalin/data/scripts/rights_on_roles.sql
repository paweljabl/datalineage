select *
from (
SELECT 
    n.nspname AS schema_name,
    c.relname AS rel_name,
    c.relkind AS rel_kind,
    pg_get_userbyid(c.relowner) AS owner_name
  FROM pg_class c
  JOIN pg_namespace n ON n.oid = c.relnamespace
 
UNION ALL

-- functions (or procedures)
SELECT
    n.nspname AS schema_name,
    p.proname,
    'p',
    pg_get_userbyid(p.proowner)
  FROM pg_proc p
  JOIN pg_namespace n ON n.oid = p.pronamespace
  ) a
 where a.rel_name = 'datalin_node'
 ;
 
SELECT oid::regprocedure AS function
     , pg_get_userbyid(proowner) AS owner
FROM   pg_proc
WHERE  oid = 'fn_absorbs(int4)'::regprocedure;

select a.*, po.rolname as grantor_name, pe.rolname as grantee_name
from (select oid::regclass,
       (aclexplode(relacl)).grantor,
       (aclexplode(relacl)).grantee,
       (aclexplode(relacl)).privilege_type,
       (aclexplode(relacl)).is_grantable
from pg_class
where relacl is not null) a
join pg_roles po on a.grantor = po.oid
join pg_roles pe on a.grantee = pe.oid
where cast(a.oid as varchar(255)) like '%vw%'
;


select * from pg_auth_members ;
select * from pg_roles ;


select oid::regclass,
       aclitem.grantee
from (select oid, aclexplode(relacl) as aclitem from pg_class) sub

SELECT
    n.nspname AS schema_name,
    p.proname,
    'p',
    pg_get_userbyid(p.proowner)
  FROM pg_proc p
  JOIN pg_namespace n ON n.oid = p.pronamespace
  where p.proname like '%lean%';
 
 grant select on vw_entities to dl_anonymus;
grant execute on FUNCTION public.fn_absorbs_lean(node_initial_id integer) to dl_anonymus;
grant execute on FUNCTION public.fn_absorbs_reverse_lean(node_initial_id integer) to dl_anonymus;

grant execute on FUNCTION public.fn_absorbs_both_dir_lean(node_initial_id integer) to dl_anonymus;
grant execute on FUNCTION public.fn_belongs_lean(node_initial_id integer) to dl_anonymus;
grant execute on FUNCTION public.fn_belongs_reverse_lean(node_initial_id integer) to dl_anonymus;

select * from datalin_node where name like '%PART%'
;
select * from datalin_relation r 
join datalin_node na on r.node_a_id = na.id
join datalin_node nb on r.node_b_id = nb.id
where (na.name like 'STOV_KOLA%' or nb.name like 'STOV_KOLA%') and
--(r.node_a_id = 5261 or r.node_b_id = 5261) and 
r.relation_type_id = 2
;

select * from datalin_relation_type
--fn_belongs_lean(5261)

delete from  datalin_relation r
where node_a_id in (select id from datalin_node where name like 'STOV%')
and r.relation_type_id = 2
and node_b_id in (select id from datalin_node where entity_id = (select id from datalin_entity where name ='Subject Area'))
;

insert into datalin_node(name, display_name,description, entity_id)
select 'STOV_' || SUBSTR(name, 4) as name, display_name, 'STOV' || SUBSTR(description, 11) as description, entity_id
from datalin_node a 
where entity_id = (select id from datalin_entity where name ='Subject Area')
;
insert into datalin_node(name, display_name,description, entity_id)
 values ('PROD_EDW_STOV', 'PROD_EDW_STOV', 'EDW STOV database', 1);

select * from datalin_entity;
select * from datalin_node where entity_id = 1;

insert into datalin_relation (node_a_id, node_b_id, relation_type_id, relation_level)
select n2.id, n.id, 2 as relation_type_id, 1
from datalin_node n, datalin_node n2
where n.name = 'PROD_EDW_STOV'
and n2.name like 'STOV_%'
and n2.entity_id = 19
;
commit

delete from datalin_relation r 
where node_a_id in (select id from datalin_node where name like 'PROD_EDW_STOV%')
and r.relation_type_id = 2
;

select * from datalin_node where NAME = 'PROD_PRDDATA_DM.D_VARIANT'

id in (5924,5170,5288, 5263);



select r.*, n1.display_name, n.display_name, n.name, n1.name 
--from datalin_relation r
from public.fn_absorbs_both_dir_lean(4847) r
left join datalin_node n on r.node_a_id = n.id
left join datalin_node n1 on r.node_b_id = n1.id
;

select * from public.fn_absorbs_both_dir_lean(1110);
select * from fn_children_lean(4847);
select * from fn_belongs_lean(4847) where node_a_id = 5288;

select * from datalin_node where id in (5459, 5287);

drop table datalin_node_b;
create table datalin_node_b as select * from datalin_node
;
drop table datalin_relation_b;
create table datalin_relation_b as select * from datalin_relation
;

select r.id, r.node_a_id, r.node_b_id, n.display_name, n1.display_name 
from (
	select node_a_id 
	from datalin_relation
	where relation_type_id = 2 and relation_level = 1
	group by node_a_id
	having count(*) > 1
) a join datalin_relation r on a.node_a_id = r.node_a_id
	and r.relation_type_id = 2  
left join datalin_node n on r.node_a_id = n.id
left join datalin_node n1 on r.node_b_id = n1.id
order by 2, 3
;
select * from datalin_node where display_name like '%D_VARIANT';
select * from datalin_rel
insert into datalin_node (name, display_name,  entity_id)
values ('PROD_VEHICLE_DM.D_VARIANT', 'D_VARIANT', 2 );

update datalin_node 
	set display_name = 'D_VARIANT'
where id = 5297;

update datalin_relation
	set node_a_id = 5964
where id = 9168;
update datalin_relation
	set node_a_id = 5297
where id = 9246;
update datalin_relation
	set node_a_id = 5964
where id in (7228)
;
update datalin_relation
	set node_b_id = 5964
where id in (7290)
;
select r.id, r.node_a_id, r.node_b_id, n.display_name, n1.display_name 
from datalin_relation r
left join datalin_node n on r.node_a_id = n.id
left join datalin_node n1 on r.node_b_id = n1.id
where (node_a_id = 5366
	or node_b_id = 5366)
and relation_type_id = 1
;
5963	PROD_PARTS_DM.D_VARIANT	D_VARIANT
5964	PROD_VEHICLE_DM.D_VARIANT	D_VARIANT
5297	PROD_PRDDATA_DM.D_VARIANT	D_VARIANT

delete from datalin_node where id = 5288;