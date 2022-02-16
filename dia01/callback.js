function hello(nombre,my_callback_01) {
    setTimeout(function() {
        console.log('Hi, ' + nombre);
        my_callback_01(nombre);
    },2500);
}

function talk(nombre,my_callback_02) {
    setTimeout(function() {
        console.log('Talking to ' + nombre);
        my_callback_02(nombre);
    },5000);
}

function bye(nombre,my_callback_03) {
    setTimeout(function() {
        console.log('Bye, ' + nombre);
        my_callback_03(nombre);
    },2500);
}

hello('Marcel',
    function(nombre) 
    {
        talk(nombre,
            function(nombre)
            {
                bye(nombre,
                    function()
                    {
                        console.log('Finish');
                    }
                )
            }
        )      
    }
);