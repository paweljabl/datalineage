CREATE OR REPLACE FUNCTION p_full_load()
returns INTEGER
AS $$
    declare 
    	v_load_id			integer;
   		v_row_count         integer; 
   		v_st_ts				timestamptz;
		v_node_a_nf			integer;
		v_node_b_nf			integer;
		v_relation_type_nf	integer;
		v_relation_nf		integer;
		v_exec_return		integer;
   	begin
		v_load_id := nextval('public.datalin_load_log_id_seq');
		
		truncate table datalin_node_load;
		truncate table datalin_relation_load;
	    v_st_ts := CURRENT_TIMESTAMP;
	   		insert into datalin_node_load(name, display_name, description, entity, technology)	
	   		select distinct a_name, a_display_name, a_description, a_entity, a_technology
	   		from datalin_full_load
	   		union
	   		select distinct b_name, b_display_name, b_description, b_entity, b_technology
	   		from datalin_full_load;
		GET DIAGNOSTICS v_row_count := ROW_COUNT;
		insert into datalin_load_log (table_name, sql_operation, start_timestamp, duration_seconds, row_count, success_flag, load_id)
			values ('datalin_node_load','insert',v_st_ts,extract('epoch' from CURRENT_TIMESTAMP)  - extract('epoch' from v_st_ts),v_row_count,'Y',v_load_id);
		
		select p_node_load(v_load_id) into v_exec_return;
	
		v_st_ts := CURRENT_TIMESTAMP;
			insert into datalin_relation_load (node_a, relation_type, relation_level, node_b)
			select a_name, relation_type, relation_level, b_name
			from datalin_full_load;	
		GET DIAGNOSTICS v_row_count := ROW_COUNT;
		insert into datalin_load_log (table_name, sql_operation, start_timestamp, duration_seconds, row_count, success_flag, load_id)
			values ('datalin_relation_load','insert',v_st_ts,extract('epoch' from CURRENT_TIMESTAMP)  - extract('epoch' from v_st_ts),v_row_count,'Y',v_load_id);
		
		select p_relation_load(v_load_id) into v_exec_return;
	
		return v_load_id;	
	
	end;
$$ 
LANGUAGE plpgsql ;