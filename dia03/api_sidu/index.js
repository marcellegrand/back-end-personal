const express = require('express');
const app = express();

//Settings
app.set('port',process.env.PORT || 5000);

//Middlewares
app.use(express.json());

//**********************************************
//Routes
//**********************************************
app.get('/',function(req,res){
    res.json({
        'status':true,
        'content':'Welcome to my API: SIDU on tbl_alumno@db_matricula'
    });
});

//Including database.js
const mySqlConnection = require('./database');

//GET Method: Listing records on tbl_alumno@db_matricula
app.get('/lst_students',function(req,res){
    const select_sql = 'select alumno_id, alumno_nombre, alumno_email from tbl_alumno';

    mySqlConnection.query(select_sql,(err,rows,fields) => {
        if (!err) {
            res.json(rows);
        }
        else {
            console.log(err);
        }
    });
});

//POST Method: Inserting one record on tbl_alumno@db_matricula
app.post('/add_student',function(req,res){
    const {name,email} = req.body;
    const insert_sql = 'insert into tbl_alumno(alumno_nombre,alumno_email) values (?,?)';

    mySqlConnection.query(insert_sql,[name,email],(err,rows,fields) => {
        if (!err) {
            res.json({
                'status':true,
                'content':'Record inserted!'
            });
        }
        else {
            console.log(err);
        }
    });
});

//PUT Method: Updating one record on tbl_alumno@db_matricula
app.put('/upd_student/:id',function(req,res){
    const {name,email} = req.body;
    const {id} = req.params;
    const update_sql = 'update tbl_alumno set alumno_nombre=?,alumno_email=? where alumno_id=?';

    mySqlConnection.query(update_sql,[name,email,id],(err,rows,fields) => {
        if (!err) {
            res.json({
                'status':true,
                'content':'Record updated!'
            });
        }
        else {
            console.log(err);
        }
    });
});

//DELETE Method: Deleting one record on tbl_alumno@db_matricula
app.delete('/del_student/:id',function(req,res){
    const {id} = req.params;
    const delete_sql = 'delete from tbl_alumno where alumno_id=?';

    mySqlConnection.query(delete_sql,[id],(err,rows,fields) => {
        if (!err) {
            res.json({
                'status':true,
                'content':'Record deleted!'
            });
        }
        else {
            console.log(err);
        }
    });
});

//Server
app.listen(app.get('port'),() =>{
    console.log(`Server running at http://localhost:${app.get('port')}`);
});