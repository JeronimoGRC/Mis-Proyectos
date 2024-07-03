'use strict';

const main = document.querySelector(".lista")
let reproduciendo = false

// Código para cargar la base de datos de las canciones
function cargarCanciones() {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', 'http://localhost:3000/canciones', true);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                console.log('Respuesta recibida:', xhr.responseText)
                var data = JSON.parse(xhr.responseText)
                console.log('Datos JSON:', data)
                pintarListaCanciones(data)
            } else {
                console.error('Error en la solicitud:', xhr.status)
            }
        }
    };
    console.log("Petición enviada");
    xhr.send();    
}

// Añadir el evento del reproducir
function cargarEvento(song,imgPlay){
    var audio = new Audio(song.musica)
    imgPlay.addEventListener('click', ()=>{
        reproduciendo = !reproduciendo
        if (reproduciendo == true){
            audio.currentTime = 0
            audio.play()
            console.log("Play",reproduciendo);
        }else{
            console.log("Pausa",reproduciendo);
            audio.pause()
            reproduciendo = false
        }
            

    })
}

function pintarListaCanciones(song) {
    let ul = document.createElement("ul")
    for (const cancion of song) {
        let li = document.createElement("li")
        let img = document.createElement("img")
        let imgPlay = document.createElement("img")
        img.src = cancion.portada
        imgPlay.src = "src/boton-de-play.png"
        imgPlay.className = "play"
        imgPlay.id = cancion.id
        cargarEvento(cancion,imgPlay)
        li.innerText = cancion.nombre
        li.appendChild(img)
        li.appendChild(imgPlay)
        ul.appendChild(li)
    }
    main.appendChild(ul)
}

cargarCanciones()