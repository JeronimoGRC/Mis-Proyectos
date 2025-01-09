import { createAnimations } from "./animatios.js"
import { checkControls } from "./controls.js"

//Configuración del juego 
const config = {
    type: Phaser.AUTO,
    width: 256,
    height: 244,
    physics: {
        default: 'arcade',
        arcade: {
            gravity: {y: 150}, // Para que caiga a una velocidad especifica 
            debug: false
        }
    },
    backgroundColor: '#049cd8',
    parent: 'game', // El game es la id de la caja donde cargaremos el juego en el html
    scene: {
        preload,
        create,
        update
    }
}

new Phaser.Game(config)
// this -> game -> El juego que estoy haciendo
function preload() {

// -- Image --

    // Carga de la nube de fondo
    this.load.image(
        'cloud1',
        'assets/scenery/overworld/cloud1.png'
    )

    // Carga del suelo
    this.load.image(
        'floorbricks',
        'assets/scenery/overworld/floorbricks.png'
    )

    this.load.image(
        'mushroom',
        'assets/collectibles/super-mushroom.png'
    )
// -- Spritesheet --

    // Carga de Mario
    this.load.spritesheet(
        'mario',
        'assets/entities/mario.png',
        {frameWidth: 18, frameHeight: 16}
    )

    // Declaración del enemigo
    this.load.spritesheet(
        'goomba',
        'assets/entities/overworld/goomba.png',
        {frameWidth: 16, frameHeight: 16}
    )

    this.load.spritesheet(
        'coin',
        'assets/collectibles/coin.png',
        {frameWidth: 16, frameHeight: 16}
    )

    this.load.spritesheet(
        'fire-flower',
        'assets/collectibles/overworld/fire-flower.png',
        {frameWidth: 16, frameHeight: 16}
    )

    this.load.spritesheet(
        'mario-grown',
        'assets/entities/mario-grown.png',
        {frameWidth: 18, frameHeight: 32}
    )

    this.load.spritesheet(
        'mario-fire',
        'assets/entities/mario-fire.png',
        {frameWidth: 18, frameHeight: 32}
    )

//  -- Audio -- 

    this.load.audio(
        'dead','assets/sound/music/gameover.mp3'
    )

    this.load.audio(
        'goomba-stomp','assets/sound/effects/goomba-stomp.wav'
    )

    this.load.audio(
        'coin-pickup','assets/sound/effects/coin.mp3'
    )

    this.load.audio(
        'powerup','assets/sound/effects/consume-powerup.mp3'
    )
}

function create() {

    this.physics.world.setBounds(0,0,2000,config.height)
    // this.add.image -> x, y, id de la img 
    this.add.image(30,60,'cloud1').setOrigin(0,0).setScale(0.15)
    
    this.mario = this.physics.add.sprite(50, 100, 'mario')
    .setOrigin(0,1)
    .setCollideWorldBounds(true) // Marca que el personaje delimite el movimiento en el espacio del mundo
    .setGravityY(300)

    this.floor = this.physics.add.staticGroup() // Establece las fisicas solidas al suelo

    this.floor
    .create(0,config.height - 16,'floorbricks')
    .setOrigin(0, 0.5)
    .refreshBody()

    this.floor
    .create(160,config.height - 16,'floorbricks')
    .setOrigin(0, 0.5)
    .refreshBody()

    this.floor  
    .create(280,config.height - 16,'floorbricks')
    .setOrigin(0, 0.5)
    .refreshBody()
    
    // Cargar al enemigo
    this.goomba = this.physics.add.sprite(120,config.height - 64,'goomba')
    .setOrigin(0,1)
    .setVelocityX(-50)
    .setCollideWorldBounds(true)
    this.goomba.anims.play('goomba-walk',true)

    this.collectibles = this.physics.add.staticGroup()
    this.collectibles.create(150,150,'coin').anims.play('coin-movement',true)
    this.collectibles.create(250,150,'coin').anims.play('coin-movement',true)
    this.collectibles.create(175,204,'mushroom')
    this.collectibles.create(205,204,'fire-flower')
    this.physics.add.overlap(this.mario, this.collectibles, collectItem, null, this)

    this.physics.world.setBounds(0,0,2000,config.height) // Establecemos el límite del mundo y hacemos que se extienda
    //Sirve para añadir las colisiones con el suelo
    this.physics.add.collider(this.mario, this.floor)
    this.physics.add.collider(this.goomba, this.floor)
    this.physics.add.collider(this.mario, this.goomba, onHitEnemy, null, this)
    
    // Configuración de la camara
    this.cameras.main.setBounds(0,0,2000,config.height) // Marcamos a la camara para que tenga los mismos limites que el mundo
    this.cameras.main.startFollow(this.mario)

    // Importamos las animaciones
    createAnimations(this)
    
    this.keys = this.input.keyboard.createCursorKeys()
}

function collectItem(mario, item) {
    const {texture: {key} } = item
    
    if (key == 'coin') {
        item.destroy();
        this.sound.add('coin-pickup', {volume: 0.1}).play()
        addScore(item,100,this)    
    }else if (key == 'mushroom') {
        item.destroy();
        this.physics.world.pause();
        this.anims.pauseAll()
        this.sound.add('powerup', {volume: 0.1}).play() 

        let i = 0
        const interval = setInterval(() => {
            i++;
            mario.anims.play(i % 2 == 0
                ? 'mario-grown-idle'
                : 'mario-idle'
            )
        },100)

        mario.isBlocked = true
        mario.isGrown = true
        
        console.log('Grown -> '+mario.isGrown);

        setTimeout(() =>{
            mario.setScale(1,1)
            mario.body.setSize(18,32)
            mario.body.setOffset(0,0)
            mario.y -= 16
            mario.isBlocked = false
            clearInterval(interval)
            this.anims.resumeAll()
            this.physics.world.resume()            
        },1000)

        addScore(item,1000,this)

    }else if(key == 'fire-flower'){

        if(!mario.isGrown){
            item.destroy();
            this.physics.world.pause();
            this.anims.pauseAll()
            this.sound.add('powerup', {volume: 0.1}).play()
            
            let i = 0
            const interval = setInterval(() => {
                i++;
                mario.anims.play(i % 2 == 0
                    ? 'mario-fire-idle'
                    : 'mario-grown-idle'
                )
            },100)

            mario.isBlocked = true
            mario.isFire = true
            
            setTimeout(() =>{
                mario.setScale(1,1)
                mario.body.setSize(18,32)
                mario.body.setOffset(0,0)
                mario.y -= 16
                mario.isBlocked = false
                clearInterval(interval)
                this.anims.resumeAll()
                this.physics.world.resume()            
            },1000)
            addScore(item,2000,this)

        }else{
            item.destroy();
            this.physics.world.pause();
            this.anims.pauseAll()
            this.sound.add('powerup', {volume: 0.1}).play()
            
            let i = 0
            const interval = setInterval(() => {
                i++;
                mario.anims.play(i % 2 == 0
                    ? 'mario-fire-idle'
                    : 'mario-grown-idle'
                )
            },100)

            mario.isBlocked = true
            mario.isFire = true
            
            console.log(mario);

            setTimeout(() =>{
                mario.isBlocked = false
                clearInterval(interval)
                this.anims.resumeAll()
                this.physics.world.resume()            
            },1000)
            addScore(item,2000,this)
        }
        
    }
        
}
        

 
function addScore(origin, scoreNumber, game) {
    const score = game.add.text(
        origin.x,
        origin.y,
        scoreNumber,
        {
            fontFamily: 'pixel',
            fontSize: config.width / 35
        }
    )
    game.tweens.add({
        targets: score,
        duration: 500,
        y: score.y - 20,
        onComplete: () => {
            game.tweens.add({
                targets: score,
                duration: 100,
                alpha: 0, // Significa opacidad
                onComplete: () => {
                    score.destroy()
                }
            })
        }
    })
}

function onHitEnemy(mario, enemy) {

    if (mario.body.touching.down && enemy.body.touching.up) {
        enemy.anims.play('goomba-dead',true);
        enemy.setVelocityX(0)
        this.sound.play('goomba-stomp')
        setTimeout(() => {
            enemy.destroy();
        },500)
        mario.setVelocityY(-150); // Salto del mario después de matar al enemigo
        addScore(enemy,200,this)
    } else {
        if (mario.isDead) return 

        if (mario.isGrown) {
            mario.isGrown = false
            mario.isDead = false        
            
            let i = 0
            const interval = setInterval(() => {
                i++;
                mario.setVisible(i % 2 === 0)
            },100)
            
            
            setTimeout(() => {
                mario.body.setSize(18,16)
                mario.body.setOffset(0,0)
                mario.setY(mario.y - 16)
                clearInterval(interval);
                mario.setVisible(true);
            }, 1500);
            
            mario.anims.play('mario-idle')

        } else {
            mario.isDead = true
            mario.anims.play('mario-dead')
            mario.setCollideWorldBounds(false)
            // Activa el audio de la muerte reduciendo el volumen
            this.sound.add('dead', {volume: 0.2}).play()
    
            mario.body.checkCollision.none = true
            mario.setVelocityX(0)
    
            setTimeout(()=>{
                mario.setVelocityY(-150)
            },90)
    
            // Se reinicia el programa 2seg después de morir
            setTimeout(()=>{
                this.scene.restart()
            },1000)
    
            enemy.setVelocityX(0)    
        }
        
    }
}


function update() {
    checkControls(this,config)
    
}