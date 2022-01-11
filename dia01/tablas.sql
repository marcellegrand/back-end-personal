create table computadoras
(
    id int(11) primary key auto_increment,
    marca varchar(100) not null,
    precio double,
    modelo varchar(100),
    procesador varchar(10),
    ram varchar(10),
    arquitectura varchar(10)
);

create table clientes
(
    id int(11) primary key auto_increment,
    nombre varchar(100) not null,
    email varchar(100)
);