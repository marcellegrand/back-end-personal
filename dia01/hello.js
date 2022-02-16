console.log("Hello, World!");
let i = 0;

var j = setInterval(function() {
    i++;
    if (i == 5)
        clearInterval(j);
    console.log("Defined function " + i);
},1000);

var k = setInterval(() => {
    i++;
    if (i == 10)
        clearInterval(k);
    console.log("Arrow function " + i);
},500)

console.log("Bye, World!");