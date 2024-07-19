let botones = document.querySelectorAll(".boton");
let numeros = document.querySelectorAll(".numero");
let signos = document.querySelectorAll(".signo");
let salida = document.querySelector("#salida");
let cuenta = "";
let signoPulsado = false;
let resuelto = false;

function gestionNumero(event) {
    if (signoPulsado) {
        if (salida.innerText == "x") {
            cuenta += "*"
        }else{
            cuenta += salida.innerText
        }
        salida.innerText = ""
        signoPulsado = !signoPulsado
    }
    caracteres = salida.innerText
    if (caracteres.length <= 20) {
        salida.innerText += event.target.innerText        
    }
}
    

function gestionSignos(event) {
    if(cuenta == ""){
        alert("Debes introducir un número")
    }else{
        cuenta += salida.innerText
        salida.innerText = event.target.innerText
        signoPulsado = true
    }
    
}

function gestionIgual() {
    if(cuenta == ""){
        alert("Debes introducir un número")
    }else{
        cuenta += salida.innerText
        let resultado = calcularCuenta(cuenta)
        pintarResultado(resultado)
    }
    
}

function calcularCuenta(cuenta) {
        resultado = eval(cuenta)
        return resultado
}

function pintarResultado(resultado) {
    salida.innerText = ""
    salida.innerText = resultado
    resuelto = true
    cuenta = ""
}

function borrarSalida() {
    salida.innerText = ""
}

function gestionDeBotones(event) {
    if (!resuelto) {
        let boton = event.target.className
        switch (boton) {
            case "boton numero":
                gestionNumero(event)
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
    }else{
        salida.innerText = ""
        resuelto = !resuelto
    }

    
}

botones.forEach(boton => {
    boton.addEventListener('click',gestionDeBotones)
})