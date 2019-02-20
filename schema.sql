create table Users (
    id integer primary key autoincrement,
    name text not null,
    email text not null,
    password text not null
);

insert into Users VALUES (1, "abd","softpro@gmail.com","123123");
