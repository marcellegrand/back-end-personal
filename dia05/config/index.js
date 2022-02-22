require('dotenv').config();

const config = {
    port : process.env.PORT || 5000,
    sqlserver_user : process.env.SQLSERVER_USER || 'administrador',
    sqlserver_pwd : process.env.SQLSERVER_PWD || 'Codigo123',
    sqlserver_host : process.env.SQLSERVER_HOST || 'codigo11-sqlserver.database.windows.net',
    sqlserver_db : process.env.SQLSERVER_DB || 'db_matricula'
}

module.exports = {config};