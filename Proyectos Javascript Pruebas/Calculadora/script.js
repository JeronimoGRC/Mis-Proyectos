let botones = document.querySelectorAll(".boton");
let numeros = document.querySelectorAll(".numero");
let signos = document.querySelectorAll(".signo");
let salida = document.querySelector("#salida");
let cuenta = "";
let caracter = "";
let signoPulsado = false;

function escribirNum(event) {
    if (signoPulsado == true) {
        salida.innerText = ""
        caracter = event.target.innerText
        salida.innerText += caracter
        cuenta += caracter
        signoPulsado = false
    } else {
        caracter = event.target.innerText
        salida.innerText += caracter
        cuenta += caracter
    }
}

function gestionSignos(event) {
    let signo = event.target.innerText
    if (cuenta == "") {
        alert("Debe haber numeros introducidos para hacer la cuenta")
    } else {
        if (signo == "x") {
            signo = "*"
            signoPulsado = true
            salida.innerText = signo
            cuenta += signo
        }else{
            signoPulsado = true
            salida.innerText = signo
            cuenta += signo 
        }
    }
}

function gestionIgual() {
    if (cuenta == "") {
        alert("¡No hay ninguna cuenta en proceso!")
    } else {
        calcularCuenta(cuenta)
    }
}

function calcularCuenta(cuenta) {
    console.log(cuenta);    
    salida.innerText = eval(cuenta)
}

function borrarSalida() {
    salida.innerText = ""
    cuenta = "";
    signoPulsado = false;
}

function gestionDeBotones(event) {
    let boton = event.target.className
    switch (boton) {
        case "boton numero":
            escribirNum(event)
        break;
            
        case "boton signo":
            gestionSignos(event)
        break;
            
        case "boton signo igual":
            gestionIgual()
        break;

        case "boton signo c":
            borrarSalida()
        break;
    }    
}

botones.forEach(boton => {
    boton.addEventListener('click',gestionDeBotones)
})