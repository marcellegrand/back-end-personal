const express = require('express');

const app = express();
const port = 5000;

//Definiendo una ruta
app.get('/',(req,res) => {
    res.send('<center><h1>Hello Express World, Marcel!</h1></center>');
});

app.get('/json',(req,res) => {
    res.json({
        'nombre': 'Marcel Johan',
        'apellido': 'Lazo de la Vega',
        'email': 'marcel.lazodelavega'
    });
});

//http://localhost:5000/greet/marcel
app.get('/greet/:name',(req,res) => {
    res.send('<center><h1>Hi, ' + req.params.name + '</h1></center>');
});

app.get('/form',function(req,res){
    html = "<form action='http://localhost:5000/greet_post' method='POST'>";
    html += "<input type='text' name='name'/>";
    html += "<input type='submit' name='greet'/>";
    html += "</form>";
    res.send(html);
});

const bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({ extended: true }));

app.post('/greet_post_html',function(req,res){
    html = res.send('<center><h1>Hi! How are you, ' + req.body.name + '?</h1></center>');
    res.send(html);
});

app.use(express.json());
app.post('/greet_post_json',function(req,res){
    const name = req.body.name;
    res.json({
        'greeting':'Hi! How are you, ' + name + '?'
    });
});

app.listen(port,function() {
    console.log('Server running on http://localhost:',port);
});