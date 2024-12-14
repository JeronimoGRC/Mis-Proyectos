const canvas = document.querySelector("canvas");
const ctx = canvas.getContext("2d");

canvas.width = innerWidth;
canvas.height = innerHeight;
// Se inicializan las particulas
let particulas = []

// Situamos el ratón en el centro de la pantalla
let raton = {
    x: canvas.width/2,
    y: canvas.height/2
}

window.addEventListener("mousemove", (e)=>{
    raton.x = e.x
    raton.y = e.y
})  

for (let i = 0; i < 500; i++) {
    particulas.push(new Particula())    
}

function animar(){// La función animar() dentro de la misma función para utilizarlo como
    // un bucle
    requestAnimationFrame(animar);
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    // Por cada particula del array particulas se actualizarán
    particulas.forEach(particula => {
        particula.actualizar(ctx);
        //Pasar el ctx al método actualizar para que el método dibujar lo gestione
    })
}

animar();