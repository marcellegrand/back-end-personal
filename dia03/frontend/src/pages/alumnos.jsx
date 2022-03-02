import React, { Component } from 'react'

import Table from 'react-bootstrap/Table'
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button'

import axios from 'axios'

export default class Alumnos extends Component {
    constructor(props) {
        super(props);
        this.state=({
            alumnos:[], //Creando dentro del 'state' un arreglo llamada 'alumnos
            nombre:'',
            email:''
        })
        this.setNombre = this.setNombre.bind(this);
        this.setEmail = this.setEmail.bind(this);
        this.listAlumnos = this.listAlumnos.bind(this);
        this.saveAlumno = this.saveAlumno.bind(this);
    }

    setNombre(e) {
        this.setState({
            nombre:e.target.value
        })
    }

    setEmail(e) {
        this.setState({
            email:e.target.value
        })
    }

    listAlumnos() {
        axios.get('http://localhost:5000/alumnos')
        .then((res) => {
            this.setState({alumnos:res.data});
        })
    }

    saveAlumno(e) {
        e.preventDefault();
        axios.post('http://localhost:5000/alumnos',{
            nombre: this.state.nombre,
            email: this.state.email
        })
        this.setState({
            nombre: '',
            email: ''
        })
        this.listAlumnos();
    }

    componentDidMount() {
        this.listAlumnos();
    }

    render() {
        return (
            <div>
                <Container>
                    <Row>
                        <Col sm={8}></Col>
                        <Col sm={12}>
                            <Table striped bordered hover>
                                <thead>
                                    <tr>
                                        <th>#</th>
                                        <th>Nombre</th>
                                        <th>Email</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {this.state.alumnos.map((alumno) => {
                                        return (
                                            <tr>
                                                <td>{alumno._id}</td>
                                                <td>{alumno.nombre}</td>
                                                <td>{alumno.email}</td>
                                            </tr>
                                        )
                                    })}
                                </tbody>
                            </Table>
                        </Col>
                        <Col sm={8}></Col>
                    </Row>
                    <Row>
                    <Form onSubmit={this.saveAlumno}>
                        <Form.Group className="mb-3">
                            <Form.Label>Nombre</Form.Label>
                            <Form.Control type="text" placeholder="Nombre" onChange={this.setNombre}/>
                        </Form.Group> 
                        <Form.Group className="mb-3" controlId="formBasicEmail">
                            <Form.Label>Email</Form.Label>
                            <Form.Control type="email" placeholder="Email" onChange={this.setEmail}/>
                        </Form.Group>
                        <Button variant="primary" type="submit">
                            Insertar
                        </Button>
                    </Form>                           
                    </Row>
                </Container>                
           </div>
        )
    }
}