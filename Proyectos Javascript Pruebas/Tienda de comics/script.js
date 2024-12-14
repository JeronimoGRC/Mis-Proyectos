let main = document.querySelector("main")
let botonesNavegacion = document.querySelectorAll(".navegador")
let botonPulsado = ""
let carrito = document.querySelector("#carrito")

function cargarComicsFiltro() {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', 'http://localhost:3000/comics', true);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                console.log('Respuesta recibida:', xhr.responseText)
                var data = JSON.parse(xhr.responseText)
                console.log('Datos JSON:', data)   
                mostrarConFiltro(data,botonPulsado)
            } else {
                console.error('Error en la solicitud:', xhr.status)
            }
        }
    };
    console.log("Petición enviada");
    xhr.send(); 
}

function cargarComics() {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', 'http://localhost:3000/comics', true);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                console.log('Respuesta recibida:', xhr.responseText)
                var data = JSON.parse(xhr.responseText)
                console.log('Datos JSON:', data)                
                pintarComics(data)   
            } else {
                console.error('Error en la solicitud:', xhr.status)
            }
        }
    };
    console.log("Petición enviada");
    xhr.send(); 
}

function borrarTienda(id) {
    var xhr = new XMLHttpRequest();
    xhr.open('DELETE', 'http://localhost:3000/comics/'+id, true);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                console.log('Elemento eliminado.')
            } else {
                console.error('Error en la solicitud:', xhr.status)
            }
        }
    }
    xhr.send()
}

function obtenerComic(id,callback) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', 'http://localhost:3000/comics/'+id, true);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                console.log('Respuesta recibida:', xhr.responseText)
                data = JSON.parse(xhr.responseText)
                console.log('Datos JSON:', data)
                callback(data)
            } else {
                console.error('Error en la solicitud:', xhr.status)
            }
        }
    }

    xhr.send()
}

function anadirCarrito(comic) {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "http://localhost:4000/carrito", true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            console.log(xhr.responseText);
        }
    }

    xhr.send(JSON.stringify(comic))
    console.log("Añadido sin problemas");
    
}

function pulsadoDeFiltro(event) {
    botonPulsado = event.target.innerText
    cargarComicsFiltro()
}

botonesNavegacion.forEach(navegador => {
    navegador.addEventListener('click',pulsadoDeFiltro)
});

function mostrarConFiltro(comics,botonPulsado) {
    main.innerHTML = ""
    let cajaDeCompra = document.createElement("div")
    cajaDeCompra.className += "catalogo" 
    for (const comic of comics) {
        var marcaComic = comic.marca
        if (marcaComic.toUpperCase() === botonPulsado) {
            let div = document.createElement("div")
            div.className = "comicCompra"
            var img = document.createElement("img")
            img.src = comic.portada
            img.height = 200
            img.title = comic.titulo
            div.appendChild(img)
            var p = document.createElement("p")
            var titulo = comic.titulo 
            if (titulo.length > 28){
                var title = titulo.slice(0,-12)+"..."
                p.innerText = title
            }else{
                p.innerText = comic.titulo
            }
            div.appendChild(p)
            var divSecundario = document.createElement("div")
            divSecundario.className += "pago"
            var imgCarro = document.createElement("img")
            imgCarro.src = "src\\src\\icon\\anadir-al-carrito.png"
            divSecundario.appendChild(imgCarro)
            var precio = document.createElement("p")
            precio.innerText = comic.precio + "€"
            divSecundario.appendChild(precio)
            div.appendChild(divSecundario)
            cajaDeCompra.appendChild(div)
            main.appendChild(cajaDeCompra)
        }
    }
}

function obtenerCarrito(){
    var xhr = new XMLHttpRequest();
    xhr.open('GET', 'http://localhost:4000/carrito', true);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            console.log(xhr.status);
            if (xhr.status === 200) {
                console.log('Respuesta recibida:', xhr.responseText)
                data = JSON.parse(xhr.responseText)
                console.log('Datos JSON:', data)
                pintarCarrito(data)
            } else {
                console.error('Error en la solicitud:', xhr.status)
            }
        }
    }

    xhr.send()
}

function pintarCarrito(data) {
    for (const compra of data) {
        let div = document.createElement("div")
        div.className = "comprado"
        let imgComic = document.createElement("img")
        imgComic.src = compra.portada
        imgComic.height = 75
        imgComic.title = compra.titulo
        let p = document.createElement("p")
        p.innerText = compra.titulo
        p.className += "titulo"
        div.appendChild(imgComic)
        div.appendChild(p)
        carrito.appendChild(div)
    }
}

function cambioACarrito(id) {
    obtenerComic(id, function (comic) {
        anadirCarrito(comic)
        borrarTienda(id)
    })
}


function pintarComics(comics){
    let cajaDeCompra = document.createElement("div")
    cajaDeCompra.className += "catalogo"    
    for (const comic of comics) {
        let div = document.createElement("div")
        div.className = "comicCompra"
        div.id = comic.id
        var img = document.createElement("img")
        img.src = comic.portada
        img.height = 200
        img.title = comic.titulo
        div.appendChild(img)
        var p = document.createElement("p")
        var titulo = comic.titulo 
        if (titulo.length > 28){
            var title = titulo.slice(0,-12)+"..."
            p.innerText = title
        }else{
            p.innerText = comic.titulo
        }

        div.appendChild(p)
        
        var divSecundario = document.createElement("div")
        divSecundario.className += "pago"
        var imgCarro = document.createElement("img")
        imgCarro.src = "src\\src\\icon\\anadir-al-carrito.png"
        
        imgCarro.addEventListener("click", () =>{
            cambioACarrito(comic.id)
            
        })

        divSecundario.appendChild(imgCarro)
        var precio = document.createElement("p")
        precio.innerText = comic.precio+"€"
        
        divSecundario.appendChild(precio)
        
        div.appendChild(divSecundario)
        
        cajaDeCompra.appendChild(div)
        
        main.appendChild(cajaDeCompra)
    }
}

cargarComics()
obtenerCarrito()