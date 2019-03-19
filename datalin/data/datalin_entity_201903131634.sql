INSERT INTO public.datalin_entity (short_name,"name",description,is_storage,is_presentation,is_application,technology_id) VALUES 
('DB','Database',NULL,'Y','N','N',1)
,('T','Table',NULL,'Y','N','N',1)
,('VW','View',NULL,'Y','N','N',1)
,('SP','Stored Procedure',NULL,'Y','N','N',1)
,('Unv','Universe 3.X',NULL,'N','Y','N',2)
,('Unx','Universe 4',NULL,'N','Y','N',2)
,('DB','Database',NULL,'Y','N','N',3)
,('T','Table',NULL,'Y','N','N',3)
,('VW','View',NULL,'Y','N','N',3)
,('SP','Stored Procedure',NULL,'Y','N','N',3)
;
INSERT INTO public.datalin_entity (short_name,"name",description,is_storage,is_presentation,is_application,technology_id) VALUES 
('Rep','SSRS Report',NULL,'N','Y','N',4)
,('Con','SSRS Connection',NULL,'N','Y','N',4)
,('Cube','OLAP cube',NULL,'Y','N','N',5)
,('DB','Database',NULL,'Y','N','N',6)
,('T','Table',NULL,'Y','N','N',6)
,('VW','View',NULL,'Y','N','N',6)
,('SP','Stored Procedure',NULL,'Y','N','N',6)
,('App','Application','An application from yellow pages, like source or BI application','N','N','Y',NULL)
,('SA','Subject Area','Logical unit used to group items from a given area','N','N','N',NULL)
,('MQ','Queue','Message Queue','N','N','N',12)
;
INSERT INTO public.datalin_entity (short_name,"name",description,is_storage,is_presentation,is_application,technology_id) VALUES 
('File','File','File from the source applicatrion','N','N','N',13)
,('SQLSrv','SQL Server','Microsoft SQL Server','Y','N','N',3)
;