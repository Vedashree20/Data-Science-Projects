/*CREATE TABLE testrigger
(
   status varchar(255)
);------>create a table to check insertion of records after creating main table*/
create trigger sample_trigger
after insert
on company
for each row
insert into testrigger values('inserted record');
