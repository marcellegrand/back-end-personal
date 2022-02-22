const express = require('express');
const AlumnosService = require('../services/alumnos');

function alumnosApi(app) {
    //Main Route
    const router = express.Router();
    app.use("/alumnos",router);

    const alumnosService = new AlumnosService();

    router.get("/lst",async function(req,res,next) {
        try {
            const alumnos = await alumnosService.selectAll();
            res.status(200).json({
                status:true,
                content:alumnos
            });
        }
        catch(err) {
            next(err);
        }
    });

    router.post("/add",async function(req,res,next) {
        const{body: alumno} = req;
        try {
            const crearAlumno = await alumnosService.insert({alumno});
            res.status(201).json({
                status:true,
                content:crearAlumno
            });
        }
        catch(err) {
            next(err);
        }
    });

    router.put("/upd/:id",async function(req,res,next) {
        const {id} = req.params;
        const {body:alumno} = req;

        try {
            const editarAlumno = await alumnosService.update({alumno,id});
            res.status(202).json({
                status:true,
                content:'Edited!'
            });
        }
        catch(err) {
            next(err);
        }
    });

    router.delete("/del/:id",async function(req,res,next) {
        const {id} = req.params;

        try {
            const eliminarAlumno = await alumnosService.delete({id});
            res.status(203).json({
                status:true,
                content:'Deleted!'
            });
        }
        catch(err) {
            next(err);
        }
    });
}

module.exports = alumnosApi;