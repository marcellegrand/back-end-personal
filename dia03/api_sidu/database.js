const mysql = require('mysql');

//Creating a set for connection
const mySqlConnection = mysql.createConnection({
    host:'localhost',
    user:'root',
    password:'',
    database:'db_matricula'
});

//Testing connection
mySqlConnection.connect(function (err) {
    if (err) {
        console.error(err);
        return;
    }
    else {
        console.log('Database [db_matricula] is connected!')
    }
});

module.exports = mySqlConnection;