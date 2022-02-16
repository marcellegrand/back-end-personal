async function hello(nombre) {
    return new Promise((resolve,reject) => {
        setTimeout(() => {
            console.log('Hi, ' + nombre)
            resolve(nombre);
            reject('no hello');
        },2500);
    });
}

async function talk(nombre) {
    return new Promise((resolve,reject) => {
        setTimeout(() => {
            console.log('Talking to ' + nombre)
            resolve(nombre);
            reject('no talk');
        },5000);
    });
}

async function bye(nombre) {
    return new Promise((resolve,reject) => {
        setTimeout(() => {
            console.log('Bye, ' + nombre)
            resolve(nombre);
            reject('no bye');
        },2500);
    });
}

async function main() {
    let nombre = await hello('Marcel');
    await talk(nombre);
    await bye(nombre);
    console.log('Finish');
}

console.log('Before');
main();
console.log('After');
