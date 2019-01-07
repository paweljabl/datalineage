DELETE FROM public.django_migrations
	WHERE app = 'datalin';


SELECT 'DROP TABLE ' || table_name || ' ;'
FROM information_schema.tables
where table_schema = 'public'
and table_name like 'datalin%'
;


DROP TABLE datalin_relation ;
DROP TABLE datalin_relation_type ;
DROP TABLE datalin_application ;
DROP TABLE datalin_node ;
DROP TABLE datalin_entity ;
DROP TABLE datalin_technology ;

-- w folderze migrations ma być tylko zero size plik: __init__.py



