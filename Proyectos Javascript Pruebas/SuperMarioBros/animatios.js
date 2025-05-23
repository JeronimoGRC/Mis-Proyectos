export const createAnimations = (game) => {
    
    // Creamos la animación de mario Caminando
    game.anims.create({
        key: 'mario-walk',
        frames: game.anims.generateFrameNumbers(
            'mario',
            {start: 3, end:1}
        ),
        frameRate: 12, // La velocidad de las animaciones
        repeat: -1 // -1 para que se repita de forma continua la animación
    })
    
    // Creamos la animación de mario Caminando
    game.anims.create({
        key: 'mario-idle',
        frames: [{key: 'mario', frame: 0}],        
    })

    // Creamos la animación de mario Caminando
    game.anims.create({
        key: 'mario-jump',
        frames: [{key: 'mario', frame: 5}],        
    })

    // Creamos la animación de mario Caminando
    game.anims.create({
        key: 'mario-dead',
        frames: [{key: 'mario', frame: 4}],        
    })
 
    game.anims.create({
        key: 'goomba-walk',
        frames: game.anims.generateFrameNumbers(
            'goomba',
            {start: 0, end:1}
        ), 
        frameRate: 12,      
        repeat: -1
    })

    game.anims.create({
        key: 'goomba-dead',
        frames: [{key: 'goomba', frame: 2}],
    })

    game.anims.create({
        key:'coin-movement',
        frames: game.anims.generateFrameNumbers(
            'coin',
            { start: 0, end: 3 }
        ),
        frameRate: 10,
        repeat: -1
    })

    game.anims.create({
        key:'fire-flower-movement',
        frames: game.anims.generateFrameNumbers(
            'fire-flower',
            { start: 0, end: 3 }
        ),
        frameRate: 5,
        repeat: -1
    })

    game.anims.create({
        key: 'mario-grown-idle',
        frames: [{key: 'mario-grown', frame: 0}],
    })

    game.anims.create({
        key: 'mario-grown-walk',
        frames: game.anims.generateFrameNumbers(
            'mario-grown',
            {start: 1, end: 3}
        ),
        frameRate: 10
    })

    game.anims.create({
        key: 'mario-grown-jump',
        frames: [{key: 'mario-grown', frame: 5}]
    })


    // Mario di fogo 

    game.anims.create({
        key: 'mario-fire-idle',
        frames: [{key: 'mario-fire', frame: 0}],
    })

    game.anims.create({
        key: 'mario-fire-walk',
        frames: game.anims.generateFrameNumbers(
            'mario-fire',
            {start: 1, end: 3}
        ),
        frameRate: 10
    })

    game.anims.create({
        key: 'mario-fire-jump',
        frames: [{key: 'mario-fire', frame: 5}]
    })

    game.anims.create({
        key: 'mario-fire-ball',
        frames: [{key: 'mario-fire', frame: 6}]
    })

    game.anims.create({
        key: 'fire-ball-rotating',
        frames: game.anims.generateFrameNumbers(
            'fire-ball',
            {start: 0, end: 3}
        ),
        frameRate: 10,
        repeat: -1
    })
}