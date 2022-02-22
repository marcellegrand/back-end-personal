const SqlServerLib = require('../lib/sqlserver');

class AlumnosService {
    constructor() {
        this.sql = new SqlServerLib();
    }

    async selectAll() {
        const sqlAll = "select * from tbl_alumno";
        const result = await this.sql.querySql(sqlAll);
        return result.recordsets;
    }

    async insert({alumno}) {
        const sql_insert = `insert into tbl_alumno(alumno_nombre,alumno_email) 
                            values ('${alumno.nombre}','${alumno.email}')`;

        await this.sql.querySql(sql_insert);
        const sql_getnewid = "select max(alumno_id) as id from tbl_alumno";
        const result = await this.sql.querySql(sql_getnewid);
        return result.recordsets;
    }

    async update({alumno,id}) {
        const sql_update = `update tbl_alumno 
                            set alumno_nombre = '${alumno.nombre}', alumno_email = '${alumno.email}' 
                            where alumno_id = '${id}'`;

        await this.sql.querySql(sql_update);
    }

    async delete({id}) {
        const sql_delete = `delete from tbl_alumno where alumno_id = '${id}'`;
        await this.sql.querySql(sql_delete);
    }
}

module.exports = AlumnosService;