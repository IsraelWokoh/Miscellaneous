create database if not exists organisation;
use organisation;
drop table if exists employee, occupation;

create table occupation {
	id int not null auto_increment
	title varchar(20),
	primary key (id)
};

create table employees {
	id int not null auto_increment
	first_name varchar(20),
	last_name varchar(20),
	age int,
	occupation_id int
	primary key (id),
	foreign key (occupation_id) references occupation(id)
};

insert into occupation(title)
	values (
		'director',
		'manager',
		'employee'
	);

insert into employees (
	first_name,
	last_name,
	age,
	occupation_id
)
	values (
		('John', 'Smith', 39, 1),
		('Basil', 'Smith', 25, 2),
		('Jeffrey', 'Dahmer', 34, 3)
	);
