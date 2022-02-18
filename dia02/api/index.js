const express = require('express');
const app = express();

//Settings
app.set('port',process.env.PORT || 5000);

//Middlewares
app.use(express.json());

//Routes
app.get('/',function(req,res){
    res.json({
        'status':true,
        'content':'Bienvenido a mi API'
    });
});

const mySqlConnection = require('./database');

//Método GET: Listado de empleados
app.get('/lst_employees',function(req,res){
    const select_sql = 'select id, name, salary from employee';

    mySqlConnection.query(select_sql,(err,rows,fields) => {
        if (!err) {
            res.json(rows);
        }
        else {
            console.log(err);
        }
    });
});

//Método POST: Insertando un empleado
app.post('/add_employee',function(req,res){
    const {name,salary} = req.body;
    const insert_sql = 'insert into employee(name,salary) values (?,?)';

    mySqlConnection.query(insert_sql,[name,salary],(err,rows,fields) => {
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

//Método PUT: Actualizando un empleado
app.put('/upd_employee/:id',function(req,res){
    const {name,salary} = req.body;
    const {id} = req.params;
    const update_sql = 'update employee set name=?,salary=? where id=?';

    mySqlConnection.query(update_sql,[name,salary,id],(err,rows,fields) => {
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

//Método DELETE: Actualizando un empleado
app.delete('/del_employee/:id',function(req,res){
    const {id} = req.params;
    const delete_sql = 'delete from employee where id=?';

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