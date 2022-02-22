const express = require('express');
const app = express();

app.get("/",(req,res)=>{
    res.json({
        'status':'OK',
        'content':'Server running succesfully!'
    });
});

const port = 5000;
app.listen(port,()=>{
    console.log(`Server running on http://localhost:${port}`)
});

//Trabajando con SEQUELIZE
const clsSequelize = require('sequelize');

const objSequelize = new clsSequelize({
    dialect:'sqlite',
    storage:'./database/sqlite'
});

objSequelize.authenticate()
.then(()=>{
    console.log('Connection done!');
})
.catch(err=>{
    console.log('Connection error!')
});

//Creando MODELS
const tblAlumnos = objSequelize.define(
    'alumnos',
    {
        nombre:clsSequelize.STRING,
        email:clsSequelize.STRING
    }
);

//Migrando MODELS
objSequelize.sync({force:true})
.then(()=>{
    console.log('Tables created!');

    //Poblando DATA
    tblAlumnos.bulkCreate(
        [
            {nombre:'Marcel Lazo de la Vega',email:'mlazodelavega@gmail.com'},
            {nombre:'Juan Pablo Lazo de la Vega',email:'jp_lazodelavega@gmail.com'},
            {nombre:'José Ignacio Lazo de la Vega',email:'ji_lazodelavega@gmail.com'}
        ]
    )
    .then(function() {
        return tblAlumnos.findAll();
    })
    .then(function(rdsAlumnos) {
        console.log(rdsAlumnos)
    });
});

//Creando los ENDPOINTS: GET
app.get('/lstAll',(req,res) => {
    tblAlumnos.findAll()
    .then((rdsAlumnos) => {
        res.json(rdsAlumnos)
    });
});

app.get('/lstOne/:id',(req,res) => {
    tblAlumnos.findAll({where: {id:req.params.id}})
    .then((rdsAlumnos) => {
        res.json(rdsAlumnos)
    });
});

//Esto sirve para aceptar entradas json, necesarias para los métodos POST y PUT
app.use(express.json());

//Creando los ENDPOINTS: POST
app.post('/ins',(req,res) => {
    tblAlumnos.create({
        nombre:req.body.nombre,
        email:req.body.email
    })
    .then((rdsAlumnos) => {
        res.json(rdsAlumnos)
    });
});

//Creando los ENDPOINTS: PUT
app.put('/upd/:id',(req,res) => {
    tblAlumnos.findByPk(req.params.id)
    .then((rdsAlumno) => {
        rdsAlumno.update({
            nombre:req.body.nombre,
            email:req.body.email    
        })
        .then((rdsAlumno) => {
            res.json(rdsAlumno)
        })
    });
});

//Creando los ENDPOINTS: DELEte
app.delete('/del/:id',(req,res) => {
    tblAlumnos.findByPk(req.params.id)
    .then((rdsAlumno) => {
        rdsAlumno.destroy();
    })
    .then(() => {
        res.json({
            'status':'OK',
            'action':'Deleted!'
        })
    })
});
