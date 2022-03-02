const express = require('express');
const cors = require('cors');

const { config } = require('./config');

const app = express();

//Configuraciones
app.set('port',config.port);

//Middlewares: Funciones que se ejecutan antes de un request
app.use(cors()); //Permite conexiones desde otros servidores, como React
app.use(express.json()); //Permite recibir datos en json hacia el servidor

//Vistas - Rutas
app.get('/',(req,res) => {
    res.json({
        'status':'OK',
        'service':'Server running succesfully!'
    });
});

//Vista ALUMNOS
app.use('/alumnos',require('./routes/alumnos'));

module.exports = app;