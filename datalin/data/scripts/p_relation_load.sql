CREATE OR REPLACE FUNCTION p_relation_load(p_load_id integer default 0)
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
   	begin
		if p_load_id = 0 then 
			v_load_id := nextval('public.datalin_load_log_id_seq');
		else 
			v_load_id := p_load_id;
		end if;
	
	   	drop table if exists temp_relation_load;
		
	    v_st_ts := CURRENT_TIMESTAMP;
		    create temp table temp_relation_load as
			select rl.*, na.id as node_a_id, nb.id as node_b_id, rt.id as relation_type_id, r.id as relation_id
			from datalin_relation_load rl
			left join datalin_node na on rl.node_a = na.name
			left join datalin_node nb on rl.node_b = nb.name
			left join datalin_relation_type rt on rl.relation_type = rt.name
			left join datalin_relation r on na.id = r.node_a_id
				and nb.id = r.node_b_id
				and rt.id = r.relation_type_id
				and rl.relation_level = r.relation_level
			;
		GET DIAGNOSTICS v_row_count := ROW_COUNT;
		insert into datalin_load_log (table_name, sql_operation, start_timestamp, duration_seconds, row_count, success_flag, load_id)
			values ('temp_relation_load','create',v_st_ts,extract('epoch' from CURRENT_TIMESTAMP)  - extract('epoch' from v_st_ts),v_row_count,'Y',v_load_id);
		
		v_st_ts := CURRENT_TIMESTAMP;
			select count(*) into v_node_a_nf
			from temp_relation_load 
			where node_a_id is null; 
		insert into datalin_load_log (table_name, sql_operation, start_timestamp, duration_seconds, row_count, success_flag, load_id)
			values ('temp_relation_load','node_a not found',v_st_ts,extract('epoch' from CURRENT_TIMESTAMP)  - extract('epoch' from v_st_ts),v_node_a_nf,'Y',v_load_id);

		v_st_ts := CURRENT_TIMESTAMP;
			select count(*) into v_node_b_nf
			from temp_relation_load 
			where node_b_id is null; 
		insert into datalin_load_log (table_name, sql_operation, start_timestamp, duration_seconds, row_count, success_flag, load_id)
			values ('temp_relation_load','node_b not found',v_st_ts,extract('epoch' from CURRENT_TIMESTAMP)  - extract('epoch' from v_st_ts),v_node_b_nf,'Y',v_load_id);
		
		v_st_ts := CURRENT_TIMESTAMP;
			select count(*) into v_relation_type_nf
			from temp_relation_load 
			where relation_type_id is null; 
		insert into datalin_load_log (table_name, sql_operation, start_timestamp, duration_seconds, row_count, success_flag, load_id)
			values ('temp_relation_load','relation type not found',v_st_ts,extract('epoch' from CURRENT_TIMESTAMP)  - extract('epoch' from v_st_ts),v_relation_type_nf,'Y',v_load_id);

		
		v_st_ts := CURRENT_TIMESTAMP;
			insert into datalin_relation (node_a_id, node_b_id, relation_type_id, relation_level)
			select node_a_id, node_b_id, relation_type_id, coalesce(relation_level, 1)
			from temp_relation_load
			where node_a_id is not null and node_b_id is not null and relation_type_id is not null and relation_id is null; 
		GET DIAGNOSTICS v_row_count := ROW_COUNT;
		insert into datalin_load_log (table_name, sql_operation, start_timestamp, duration_seconds, row_count, success_flag, load_id)
			values ('datalin_relation','insert',v_st_ts,extract('epoch' from CURRENT_TIMESTAMP)  - extract('epoch' from v_st_ts),v_row_count,'Y',v_load_id);
--		commit;	
		return v_load_id;	
	
	end;
$$ 
LANGUAGE plpgsql ;