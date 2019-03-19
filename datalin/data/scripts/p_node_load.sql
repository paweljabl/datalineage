CREATE OR REPLACE FUNCTION p_node_load(p_load_id integer default 0)
returns INTEGER
AS $$
    declare 
    	v_load_id			integer;
   		v_row_count         integer; 
   		v_st_ts				timestamptz;
   		v_technology_nf		integer;
		v_entity_nf			integer;
		v_node_nf			integer;
   	begin
		if p_load_id = 0 then 
			v_load_id := nextval('public.datalin_load_log_id_seq');
		else 
			v_load_id := p_load_id;
		end if;
	
	   	drop table if exists temp_node_load;
		
	    v_st_ts := CURRENT_TIMESTAMP;
		    create temp table temp_node_load as
			select nl.*, e.id as entity_id, t.id as technology_id, n.id as node_id
			from datalin_node_load nl
			left join datalin_technology t on nl.technology = t.name
			left join datalin_entity e on nl.entity = e.name
				and coalesce(e.technology_id,0) = coalesce(t.id,0)
			left join datalin_node n on n.name = nl.name
				and n.entity_id = e.id
			;
		GET DIAGNOSTICS v_row_count := ROW_COUNT;
		insert into datalin_load_log (table_name, sql_operation, start_timestamp, duration_seconds, row_count, success_flag, load_id)
			values ('temp_node_load','create',v_st_ts,extract('epoch' from CURRENT_TIMESTAMP)  - extract('epoch' from v_st_ts),v_row_count,'Y',v_load_id);
--		commit;	
		
		v_st_ts := CURRENT_TIMESTAMP;
			select count(*) into v_technology_nf
			from temp_node_load 
			where technology is not null and technology_id is null; 
		insert into datalin_load_log (table_name, sql_operation, start_timestamp, duration_seconds, row_count, success_flag, load_id)
			values ('temp_node_load','technology not found',v_st_ts,extract('epoch' from CURRENT_TIMESTAMP)  - extract('epoch' from v_st_ts),v_technology_nf,'Y',v_load_id);
--		commit;	
		
		v_st_ts := CURRENT_TIMESTAMP;
			select count(*) into v_entity_nf
			from temp_node_load 
			where entity_id is null;
		insert into datalin_load_log (table_name, sql_operation, start_timestamp, duration_seconds, row_count, success_flag, load_id)
			values ('temp_node_load','entity not found',v_st_ts,extract('epoch' from CURRENT_TIMESTAMP)  - extract('epoch' from v_st_ts),v_entity_nf,'Y',v_load_id);
--		commit;	
		
		v_st_ts := CURRENT_TIMESTAMP;
			select count(*) into v_node_nf
			from temp_node_load 
			where node_id is not null;
		insert into datalin_load_log (table_name, sql_operation, start_timestamp, duration_seconds, row_count, success_flag, load_id)
			values ('temp_node_load','node exists',v_st_ts,extract('epoch' from CURRENT_TIMESTAMP)  - extract('epoch' from v_st_ts),v_node_nf,'Y',v_load_id);
--		commit;	

		v_st_ts := CURRENT_TIMESTAMP;
			insert into datalin_node (name, display_name,description, entity_id)
			select name, display_name,description, entity_id 
			from temp_node_load
			where node_id is null and entity_id is not null; 
		GET DIAGNOSTICS v_row_count := ROW_COUNT;
		insert into datalin_load_log (table_name, sql_operation, start_timestamp, duration_seconds, row_count, success_flag, load_id)
			values ('datalin_node','insert',v_st_ts,extract('epoch' from CURRENT_TIMESTAMP)  - extract('epoch' from v_st_ts),v_row_count,'Y',v_load_id);
--		commit;	
		return v_load_id;	
	
	end;
$$ 
LANGUAGE plpgsql ;