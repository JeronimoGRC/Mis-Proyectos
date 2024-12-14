class Particula {
    constructor() {
        this.x = Math.random() * innerWidth; // Posición inicial aleatoria dentro del canvas
        this.y = Math.random() * innerHeight; // Posición inicial aleatoria dentro del canvas
        this.radio = 5;
        //La velocidad será tanto negativa como positiva para así poder ir en cualquier dirección
        this.velocidadX = (Math.random() - 0.5)*4; // Va de -2 hasta 2 el Math.random
        this.velocidadY = (Math.random() - 0.5)*4;
        this.tamanioMax = 50
        this.tamanioMin = this.radio
        this.incremento = 0.8
        this.color = colores[Math.floor(Math.random() * colores.length)]
    }

    dibujar(ctx) {
        //Se comienza el trazo
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.radio, 0, Math.PI * 2, false);
        //Se rellena la particula
        ctx.fillStyle = this.color // Color para identificar el círculo
        ctx.fill();
        ctx.stroke() // Para darle un borde
        // Se comienza el trazo
        ctx.closePath();
    }

    mover(){
        // Indicar los limites en el eje horizontal
        if (this.x + this.radio > canvas.width || this.x - this.radio < 0) {
            this.velocidadX = -this.velocidadX
        }
        // Indicar los limites en el eje vertical
        if (this.y + this.radio > canvas.height || this.y - this.radio < 0) {
            this.velocidadY = -this.velocidadY
        }

        this.x += this.velocidadX
        this.y += this.velocidadY
    }

    actualizar(ctx){

        if (calcularDistancia(raton,this) < 100 && this.radio < this.tamanioMax) {
            this.radio += this.incremento 
        }else{
            if (this.radio > this.tamanioMin) {
                this.radio -= this.incremento
            }
        }

        this.dibujar(ctx)
        this.mover()
    }
}
