//1. inicializar el canvas

const canvas = document.querySelector("canvas")
const constext = canvas.getContext("2d")

//configuracion de la pantalla y el tamaño de los bloques
const BLOCK_SIZE=20
const BOARD_WIDTH = 14
const BOARD_HEIGHT=30

//escalar el contexto para cada punto
constext.scale(BLOCK_SIZE,BLOCK_SIZE)

//3. crear el boart de 30 filas
const board = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

//4. la pieza del juegador
const pice = {
    position: {
        x:5,
        y:5,
    },
    shape : [
        [1,1],
        [1,1]
    ]
}

//9. pieza ramdom
const PICE = [
    [
        [1,1],
        [1,1]
    ]
    [
        [1,1,1,1]
    ],
    [
        [1,0],
        [1,0],
        [1,1],
    ]
]

//2.game loop:esta seccion dbujara el juego
//8.auto drop
let dropCaunter = 0
let lastTime = 0

function update(time = 0) {
    const dataTime = time - lastTime
    lastTime = time
    dropCaunter += dataTime

    if (dropCaunter > 1000) {
        pice.position.y++
        dropCaunter = 0

        if (checkCollicion()) [
            pice.position.y--
            solidifyPice()
            removeRows()
        ]
    }

    //cada vez que hacemos un juego vamos a pintar
    drow()
    //loop infinto
    window.requestAnimationFrame(update)
}

//funcion drowes la que va a dibujar nuesto juego
function drow() {
    //dibujaqr el boar
    constext.fillStyle = "#222"
    constext.fillRect(0, 0,canvas.width,canvas.height)
    board.forEach((row, y) => {
        row.forEach((value,x) => {
            if (value === 1) {
                constext.fillStyle = "yellow"
                constext.fillRect(x,y,1,1)
            }
        })
    })
    pice.shape.forEach((row, y) => {
        row.forEach((value,x) => {
            if (value === 1){
                constext.fillStyle = "red"
                constext.fillRect(x + pice.position.x, y + pice.position.y,1,1)
            }
        })
    })
}

//5. mover las piezas
document.addEventListener("keydown", ev => {
    if (ev.key === "ArrowLeft"){
        pice.position.x--
        if(checkCollicion()){
            pice.position.x++
        }
    }
    if (ev.key === "ArrowRight"){
        pice.position.x++
        if(checkCollicion()){
            pice.position.x--
        }
    }
    if (ev.key === "ArrowDown"){
        pice.position.y++
        if(checkCollicion()){
            pice.position.y--
        }
    }
    if (ev.key === "ArrowUp"){
        const rotated = []
        for (let i = 0;i < pice.shape[0].length;i++){
            const row = []

            for (let x = pice.shape.length - 1 ;x >=0;x--) {
                row.push(pice.shape[i][x])
            } 
            rotated.push(row)
        }
        const previousShape = price.shape
        price.shape = rotated
        if (checkCollicion()){
            pice.shape = previousShape
        }
    }    
})

//6.coliciones
function checkCollicion() {
    return pice.shape.find((row,y) => {
        return row.find((value,x)=> {
            return (
                value !== 0 &&
                board[y + pice.position.y]?.[x + pice.position.x] !== 0
            )
        })
    })
}

//7. solidificar la pieza 
function solidifyPice() {
    pice.shape.forEach((row,y) => {
        row.forEach((value,x) => {
            if (value === 1) {
                board[y + pice.position.y][x + pice.position.x] = 1
            }
        })
    })
    //resetear la posicion de la pieza
    pice.position.x = Math.floor(BOARD_WIDTH / 2 - 2)
    pice.position.y = 0
    //establecer la pieza aleatoria
    pice.shape = PICE[Math.floor(Math.random() * PICE.length)]
    //juego finalizado game over 
    if ()
}