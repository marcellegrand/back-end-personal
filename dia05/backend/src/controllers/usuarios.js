const usuarioController = {};

const usuarioModel = require('../models/alumnos');
const boom = require('@hapi/boom');
const jwt = require('jsonwebtoken');

usuarioController.getAll = async (req,res)=>{
    const usuarios = await usuarioModel.find();
    res.json(usuarios);
}

usuarioController.create = async (req,res) =>{
    const {usuario,password} = req.body;
    const token = 

    const nuevoUsuario = new usuarioModel({
        usuario,
        password
    })
    await nuevoUsuario.save();
    res.json({
        status:true,
        content:'usuario creado con exito'
    })
}