const http = require('http');

http.createServer(function(req,res) {   
    console.log("Server running!");
    console.log(req.url);
    switch(req.url) {
        case '/hello':
            res.write('<h1>Hello, World!</h1>');
            res.end();
            break;
        default:
            res.write('<h1>Not found!</h1>');
            res.end();
    }
}).listen(5000);