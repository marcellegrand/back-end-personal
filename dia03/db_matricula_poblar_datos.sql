select * from tbl_alumno;
insert into tbl_alumno(alumno_nombre, alumno_email) 
values 
('Marcel Lazo de la Vega','mlazodelavega@gmail.com'),
('Rocío Vizcarra','rvizcarra@hotmail.com'),
('Juan Pablo Lazo de la Vega','jp_lazodelavega@yahoo.com'),
('José Ignacio Lazo de la Vega','ji_lazodelavega@yahoo.com')
;

select * from tbl_bootcamp;
insert into tbl_bootcamp(bootcamp_nombre)
values
('Desarrollo Web Full Stack'),
('Desarrollo de aplicaciones móviles'),
('Desarrollo de videojuegos')
;

select * from tbl_curso;
insert into tbl_curso(curso_nombre)
values
('HTML 5.0'),
('JavaScript'),
('CCS'),
('React'),
('Angular'),
('Python'),
('MySQL'),
('PostgreSQL'),
('MongoDB'),
('Firebase')
;

select * from tbl_matricula;
insert into tbl_matricula(matricula_grupo,matricula_fecha,bootcamp_id,alumno_id)
values
('CodiGO_G11',STR_TO_DATE('2021-09-01','%Y-%m-%d'),1,1),
('CodiGO_G11',STR_TO_DATE('2021-09-01','%Y-%m-%d'),1,2),
('CodiGO_G11',STR_TO_DATE('2021-09-01','%Y-%m-%d'),1,3),
('CodiGO_G11',STR_TO_DATE('2021-09-01','%Y-%m-%d'),1,4),
('CodiGO_G11',STR_TO_DATE('2022-01-01','%Y-%m-%d'),2,1),
('CodiGO_G11',STR_TO_DATE('2022-01-01','%Y-%m-%d'),2,2),
('CodiGO_G11',STR_TO_DATE('2021-10-01','%Y-%m-%d'),3,3),
('CodiGO_G11',STR_TO_DATE('2021-10-01','%Y-%m-%d'),3,4)
;

select * from tbl_profesor;
insert into tbl_profesor(profesor_nombre,profesor_email)
values
('Sebastian Yabiku','syabiku@tecsup.edu.pe'),
('César Mayta','cmayta@tecsup.edu.pe'),
('Linder Hassinger','lhassinger@tecsup.edu.pe'),
('Claudio Garnica','cgarnica@tecsup.edu.pe')
;

select * from tbl_matricula_curso;
insert into tbl_matricula_curso(matricula_id,curso_id,profesor_id)
values
(),


