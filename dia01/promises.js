function hello(nombre) {
    return new Promise((resolve,reject) => {
        setTimeout(() => {
            console.log('Hi, ' + nombre)
            resolve(nombre);
            reject('no hello');
        },2500);
    });
}

function talk(nombre) {
    return new Promise((resolve,reject) => {
        setTimeout(() => {
            console.log('Talking to ' + nombre)
            resolve(nombre);
            reject('no talk');
        },5000);
    });
}

function bye(nombre) {
    return new Promise((resolve,reject) => {
        setTimeout(() => {
            console.log('Bye, ' + nombre)
            resolve(nombre);
            reject('no bye');
        },2500);
    });
}

hello('Marcel')
    .then(talk)
    .then(bye)
    .then(() => {
        console.log('Finish');
    });