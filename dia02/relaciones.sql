create table clientes (
    id int(11) not null AUTO_INCREMENT,
    nombre varchar(100) not null,
    email varchar(100),
    vigente int(1) default 1 not null,
    primary key (id)
) ENGINE=InnoDB;

create table articulos (
    id int(10) not null AUTO_INCREMENT,
    descripcion varchar(100) not null,
    familia varchar(100),
    vigente int(1) default 1 not null,
    primary key (id)
) ENGINE=InnoDB;

create table ventas (
    fecha date not null,
    correlativo int(6) not null,
    cliente_id int(11) not null,
    vigente int(1) default 1 not null ,
    primary key (fecha, correlativo),
    foreign key (cliente_id) references clientes (id)
) ENGINE=InnoDB;

create table ventas_detalle (
    fecha date not null,
    correlativo int(6) not null,
    item int(3) not null,
    cantidad double(10,2) not null,
    unidad varchar(3) not null,
    precio double(10,2) not null,
    vigente int(1) default 1 not null,
    articulo_id int(10) not null,
    primary key (fecha, correlativo, item),
    foreign key (fecha, correlativo) references ventas (fecha, correlativo),
    foreign key (articulo_id) references articulos (id)
) ENGINE=InnoDB;
