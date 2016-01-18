+ create table diary like inno_diary;
+ alter table diary engine=MyISAM;
+ insert into diary select * from inno_diary;

+ show engines

+ create table diary select * from inno_diary;
+ create table diary like inno_diary;