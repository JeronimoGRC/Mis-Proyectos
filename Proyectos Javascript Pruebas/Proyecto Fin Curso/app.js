// Declaración de variables globales  
// Etiquetas HTML
const precio_total = document.getElementById("total")
let boton_agregar_tarea = document.getElementById("agregar_tarea")
let lista_tareas = document.getElementById("lista_tareas")
let mi_carrito = document.getElementById("mi_carrito")
let boton_agregar_notas = document.getElementById("agregar_notas")
let lista_notas = document.getElementById("lista_notas")
// Creación de elementos
let camiseta_li = document.createElement("li")
let pantalon_li = document.createElement("li")
let sombrero_li = document.createElement("li")
let zapatos_li = document.createElement("li")
// Booleanos
let etiqueta_puesta_camiseta = false
let etiqueta_puesta_pantalon = false
let etiqueta_puesta_zapatos = false
let etiqueta_puesta_sombrero = false
// Numéricos
let total = 0
// Declaración de objetos 
const CAMISETA = {
    nombre: "Camiseta",
    precio: 20,
    cantidad: 1
}
const PANTALON = {
    nombre: "Pantalón",
    precio: 35,
    cantidad: 1
}
const ZAPATO = {
    nombre: "Zapatos",
    precio: 50,
    cantidad: 1
}
const SOMBRERO = {
    nombre: "Sombrero",
    precio: 15,
    cantidad: 1
}

// Funcionalidad de agregar tareas
boton_agregar_tarea.addEventListener("click", () => {    
    if (document.getElementById("tarea").value.trim() != "") {
        let li = document.createElement("li")
        li.textContent = document.getElementById("tarea").value
        li.className = "tarea"
        li.addEventListener("click", () => {
            li.className += " finalizada"
        })
        lista_tareas.appendChild(li)
        document.getElementById("tarea").value = ""
    }else{
        alert("No has introducido ningún valor")
    }
})

let agregar_prod = document.querySelectorAll(".agregar_prod")

agregar_prod.forEach(element => {
    element.addEventListener("click", (ev) =>{
        let id = ev.target.id
        agregar_a_carrito(id) // Rastrear un array con los objetos y hacerlo mas optimizable
        calcularTotal(id)
    })
});

//Función para filtrar en función del producto para agregar al carrito
function agregar_a_carrito(id) {
    switch (id) {
        case "camiseta":
            aniadir_camiseta()
            break;
        case "pantalon":
            aniadir_pantalon()
            break;
        case "zapatos":        
            aniadir_zapatos()
            break;
        case "sombrero":
            aniadir_sombrero()
            break;
    }
}

function aniadir_camiseta() {    
    if (etiqueta_puesta_camiseta == true) {
        CAMISETA.cantidad++
        camiseta_li.textContent = ""
        camiseta_li.textContent += `Camiseta - $20 x${CAMISETA.cantidad}`        
    } else {
        camiseta_li.textContent = "Camiseta - $20 "
        mi_carrito.appendChild(camiseta_li)
        etiqueta_puesta_camiseta = true
    }
}

function aniadir_pantalon() {
    if (etiqueta_puesta_pantalon == true) {
        PANTALON.cantidad++
        pantalon_li.textContent = ""
        pantalon_li.textContent += `Pantalón - $35 x${PANTALON.cantidad}`        
    } else {
        pantalon_li.textContent = "Pantalón - $35 "
        mi_carrito.appendChild(pantalon_li)
        etiqueta_puesta_pantalon = true
    }
}

function aniadir_zapatos() {
    if (etiqueta_puesta_zapatos == true) {
        ZAPATO.cantidad++
        zapatos_li.textContent = ""
        zapatos_li.textContent += `Zapatos - $50 x${ZAPATO.cantidad}`        
    } else {
        zapatos_li.textContent = "Zapatos - $50 "
        mi_carrito.appendChild(zapatos_li)
        etiqueta_puesta_zapatos = true
    }
}

function aniadir_sombrero() {
    if (etiqueta_puesta_sombrero == true) {
        SOMBRERO.cantidad++
        sombrero_li.textContent = ""
        sombrero_li.textContent += `Sombrero - $15 x${SOMBRERO.cantidad}`        
    } else {
        sombrero_li.textContent = "Sombrero - $15 "
        mi_carrito.appendChild(sombrero_li)
        etiqueta_puesta_sombrero = true
    }
}

// Calculamos el total y a la vez lo añadimos en las líneas de precio_total.innerText = total
function calcularTotal(id) {
    switch (id) {
        case "camiseta":
            total += CAMISETA.precio
            precio_total.innerText = total
            break;
        case "pantalon":
            total += PANTALON.precio
            precio_total.innerText = total
            break;
        case "zapatos":        
            total += ZAPATO.precio
            precio_total.innerText = total
            break;
        case "sombrero":
            total += SOMBRERO.precio
            precio_total.innerText = total
            break;
    }
}

boton_agregar_notas.addEventListener("click", () =>{    
    agregar_notas()
})

function agregar_notas() {
    let div = document.createElement("div")

    if (document.getElementById("titulo_nota").value.trim() != "" && document.getElementById("descripcion_nota").value.trim() != "") {        
        let h3 = document.createElement("h3")        
        h3.innerText = document.getElementById("titulo_nota").value
        let p = document.createElement("p")
        p.innerText = document.getElementById("descripcion_nota").value        
        div.appendChild(h3)
        div.appendChild(p)
        lista_notas.appendChild(div)
    }else{
        alert("Te falta un elemento por rellenar")
    }   
}