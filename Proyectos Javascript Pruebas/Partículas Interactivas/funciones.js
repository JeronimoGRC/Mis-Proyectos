const colores = ["red", "green", "pink", "cyan"]

function calcularDistancia(obj1, obj2) {
    
    let distanciaX = obj1.x - obj2.x
    let distanciaY = obj1.y - obj2.y

    // Calculamos la distancia total
    // Para ello utilizamos Pitagoras h = raiz cuadrada de (a^2 + b^2)
    let distanciaTotal = Math.sqrt(Math.pow(distanciaX,2) + Math.pow(distanciaY,2))
    
    return distanciaTotal
}

