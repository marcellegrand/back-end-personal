create table tbl_alumno(
    alumno_id INT NOT NULL IDENTITY PRIMARY KEY,
    alumno_nombre VARCHAR(100) NOT NULL,
    alumno_email VARCHAR(100)
);

insert into tbl_alumno(alumno_nombre,alumno_email) values('Marcel Lazo de la Vega Velarde','marcel.lazodelavega@gmail.com');