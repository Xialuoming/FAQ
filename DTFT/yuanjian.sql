create table yj
	(
	id int auto_increment not null primary key,
	user_name char(8) not null,
	password char(40) not null,
	title char(100),
	salary char(10)
	);