CREATE OR REPLACE FUNCTION p_application_load()
returns INTEGER
AS $$
    declare 
    	v_load_id			integer;
   		v_row_count         integer; 
   		v_st_ts				timestamptz;
   	begin
		v_load_id := nextval('public.datalin_load_log_id_seq');
	   	drop table if exists temp_application_load;
		
	    v_st_ts := CURRENT_TIMESTAMP;
		    create temp table temp_application_load as
			select al.*, e.id as entity_id 
			from datalin_application_load al
			left join datalin_node n on n.name = al.name
			left join datalin_entity e on e.name = al.entity
			where n.id is null
		;
		GET DIAGNOSTICS v_row_count := ROW_COUNT;
		insert into datalin_load_log (table_name, sql_operation, start_timestamp, duration_seconds, row_count, success_flag, load_id)
			values ('temp_application_load','create',v_st_ts,extract('epoch' from CURRENT_TIMESTAMP)  - extract('epoch' from v_st_ts),v_row_count,'Y',v_load_id);
--		commit;	
		
		v_st_ts := CURRENT_TIMESTAMP;
			insert into datalin_node (name, display_name,description, entity_id)
			select name, display_name,description, entity_id 
			from temp_application_load; 
		GET DIAGNOSTICS v_row_count := ROW_COUNT;
		insert into datalin_load_log (table_name, sql_operation, start_timestamp, duration_seconds, row_count, success_flag, load_id)
			values ('datalin_node','insert',v_st_ts,extract('epoch' from CURRENT_TIMESTAMP)  - extract('epoch' from v_st_ts),v_row_count,'Y',v_load_id);
--		commit;	
	
		v_st_ts := CURRENT_TIMESTAMP;
			insert into datalin_application (node_id, owner_name, contact_email, is_bi)
			select n.id, owner_name, contact_email, is_bi
			from temp_application_load al
			join datalin_node n on al.name = n.name; 
		GET DIAGNOSTICS v_row_count := ROW_COUNT;
		insert into datalin_load_log (table_name, sql_operation, start_timestamp, duration_seconds, row_count, success_flag, load_id)
			values ('datalin_application','insert',v_st_ts,extract('epoch' from CURRENT_TIMESTAMP)  - extract('epoch' from v_st_ts),v_row_count,'Y',v_load_id);
--		commit;	
		return v_load_id;	
	
	end;
$$ 
LANGUAGE plpgsql ;