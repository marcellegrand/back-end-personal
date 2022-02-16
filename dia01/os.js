const os = require('os');

console.log(os.arch());
console.log(os.platform());
console.log(os.cpus().length);
console.log(os.totalmem());

const factor = 1024;

/*
FUNCIONES SIMPLES
*/
function kb(bytes) { return bytes / factor; }
function mb(bytes) { return kb(bytes) / factor; }
function gb(bytes) { return mb(bytes) / factor; }
console.log("RAM en KB: " + kb(os.totalmem()));
console.log("RAM en MB: " + mb(os.totalmem()));
console.log("RAM en GB: " + gb(os.totalmem()));

/*
PROMESAS
*/
function kb_promise(p_b) {
    return new Promise((resolve,reject) => {
        //setTimeout(() => {
            let p_kb = p_b / factor;
            console.log("RAM en KB: " + p_kb);
            resolve(p_kb);
            //reject();
        //},10);
    });
}

function mb_promise(p_kb) {
    return new Promise((resolve,reject) => {
        //setTimeout(() => {
            let p_mb = p_kb / factor;
            console.log("RAM en MB: " + p_mb);
            resolve(p_mb);
            //reject();
        //},10);
    });
}

function gb_promise(p_mb) {
    return new Promise((resolve,reject) => {
        //setTimeout(() => {
            let p_gb = p_mb / factor;
            console.log("RAM en GB: " + p_gb);
            resolve(p_gb);
            //reject();
        //},10);
    });
}
kb_promise(os.totalmem()).then(mb_promise).then(gb_promise);

/*
ASYNC and AWAIT
*/
async function memoria(bytes) {
    return new Promise(function(resolve,reject) {
            result = bytes / factor;
            resolve(result);
    });
}

async function main() {
    kb = await memoria(os.totalmem());
    mb = await memoria(kb);
    gb = await memoria(mb);
    console.table(
        [
            {capacidad:'KB',tam:kb},
            {capacidad:'MB',tam:mb},
            {capacidad:'GB',tam:gb}
        ]
    );
}
main();