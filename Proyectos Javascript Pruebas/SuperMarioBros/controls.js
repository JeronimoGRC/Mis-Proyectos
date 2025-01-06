const MARIO_ANIMATIONS = {
    grown:{
        idle: 'mario-grown-idle',
        walk: 'mario-grown-walk',
        jump: 'mario-grown-jump'
    },
    normal: {
        idle: 'mario-idle',
        walk: 'mario-walk',
        jump: 'mario-jump' 
    }
}

export function checkControls({mario, keys, sound, scene},config){
    const isMarioTouchingFloor =  mario.body.touching.down
    const isLeftKeyIsDown = keys.left.isDown
    const isRightKeyIsDown = keys.right.isDown
    const isUpKeyIsDown = keys.up.isDown

    if (mario.isDead) return
    if (mario.isBlocked) return 
    
    const marioAnimations = mario.isGrown ? 
    MARIO_ANIMATIONS.grown :
    MARIO_ANIMATIONS.normal
    // Condiciones de los movimientos
    if (isLeftKeyIsDown){
        mario.x -= 2
        mario.flipX = true
        isMarioTouchingFloor && mario.anims.play(marioAnimations.walk, true)

    }else if(isRightKeyIsDown){
        mario.x += 2
        mario.flipX = false
        // Para que solo se muestre la animación de correr si Mario está tocando el suelo 
        isMarioTouchingFloor && mario.anims.play(marioAnimations.walk, true)
    
    }else if(isUpKeyIsDown && isMarioTouchingFloor){
        mario.setVelocityY(-250)
        mario.anims.play(marioAnimations.jump, true)
    
    }else if(isMarioTouchingFloor){
        mario.anims.stop()
        mario.anims.play(marioAnimations.idle,true)
    }
    
    // Animación de muerte de Mario
    if (mario.y >= config.height) {
        mario.isDead = true
        mario.anims.play('mario-dead')
        mario.setCollideWorldBounds(false)
        // Activa el audio de la muerte reduciendo el volumen
        sound.add('dead', {volume: 0.2}).play()

        setTimeout(()=>{
            mario.setVelocityY(-150)
        },90)

        // Se reinicia el programa 2seg después de morir
        setTimeout(()=>{
            scene.restart()
        },2000)
    }
}