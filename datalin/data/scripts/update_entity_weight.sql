select '-- ' || e.name || ' ' || coalesce(t.name, '') 
|| chr(10) || 'update datalin_entity set weight =    where id = ' ||  e.id || ';'
|| chr(10)
from datalin_entity e
left  join datalin_technology t on e.technology_id = t.id
order by e.id;

-- Database Netezza
update datalin_entity set weight =  30  where id = 1;

-- Table Netezza
update datalin_entity set weight = 90  where id = 2;

-- View Netezza
update datalin_entity set weight =  90  where id = 3;

-- Stored Procedure Netezza
update datalin_entity set weight =  300  where id = 4;

-- Universe 3.X Business Objects
update datalin_entity set weight =  80  where id = 5;

-- Universe 4 Business Objects
update datalin_entity set weight =  70  where id = 6;

-- Database SQL Server
update datalin_entity set weight =  50  where id = 7;

-- Table SQL Server
update datalin_entity set weight =  110  where id = 8;

-- View SQL Server
update datalin_entity set weight = 110   where id = 9;

-- Stored Procedure SQL Server
update datalin_entity set weight =  310  where id = 10;

-- SSRS Report SQL Server Reporting Services
update datalin_entity set weight =  135  where id = 11;

-- SSRS Connection SQL Server Reporting Services
update datalin_entity set weight =  320  where id = 12;

-- OLAP cube SQL Server Analysis Services
update datalin_entity set weight = 60   where id = 13;

-- Database Oracle Database
update datalin_entity set weight =  40  where id = 14;

-- Table Oracle Database
update datalin_entity set weight =  100  where id = 15;

-- View Oracle Database
update datalin_entity set weight = 100   where id = 16;

-- Stored Procedure Oracle Database
update datalin_entity set weight = 190  where id = 17;

-- Application 
update datalin_entity set weight =  10  where id = 18;

-- Subject Area 
update datalin_entity set weight =  20  where id = 19;

-- File Data Warehouse Upload Tool
update datalin_entity set weight =  140  where id = 20;

-- File Message Queue
update datalin_entity set weight = 170   where id = 21;

-- File VCOM
update datalin_entity set weight = 180   where id = 22;

-- Function Oracle Database
update datalin_entity set weight =  200  where id = 23;

-- Queue Message Queue
update datalin_entity set weight = 150   where id = 24;

-- Table DB2
update datalin_entity set weight = 160   where id = 26;

-- Sequence Netezza
update datalin_entity set weight =  400  where id = 28;

select e.id, e.name , t.name, e.weight
from datalin_entity e
left  join datalin_technology t on e.technology_id = t.id
order by e.weight, e.id;
