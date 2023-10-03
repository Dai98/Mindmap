// Control the dropdown
let playerState = "run";
const dropdown = document.getElementById("animations");
dropdown.addEventListener('change', function(e) {
    playerState = e.target.value;
})


const canvas = document.getElementById('canvas1');
const ctx = canvas.getContext('2d');

// Canvas setup
const CANVAS_WIDTH = canvas.width = 600;
const CANVAS_HEIGHT = canvas.height = 600;
const spriteWidth = 575;
const spriteHeight = 523;

// Make animation slower
let gameFrame = 0;
const staggerFrames = 3;

const playerImage = new Image();
playerImage.src = 'shadow_dog.png';

// Switch between different rows in sprite sheet
const spriteAnimations = [];
const animationStates = [
    {
        name: 'idle',
        frames: 7
    },
    {
        name: 'jump',
        frames: 7
    },
    {
        name: 'fall',
        frames: 7
    },
    {
        name: 'run',
        frames: 9
    },
    {
        name: 'dizzy',
        frames: 11
    }, 
    {
        name: 'sit',
        frames: 5
    },
    {
        name: 'roll',
        frames: 7
    },
    {
        name: 'bite',
        frames: 7
    },
    {
        name: 'ko',
        frames: 12
    },
    {
        name: 'getHit',
        frames: 4
    }
]

animationStates.forEach((state, index) => {
    let frames = {
        loc: []
    }

    for(let j=0; j < state.frames; j++) {
        let positionX = j * spriteWidth;
        let positionY = index * spriteHeight;
        frames.loc.push({x: positionX, y: positionY});
    }

    spriteAnimations[state.name] = frames;
});

console.log(spriteAnimations);

// What happens in every frame
function animate() {
    ctx.clearRect(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT);

    // Which image in sprite animation to show
    // Move to next image in sprite sheet only after <staggerFrames> frames
    let position = Math.floor(gameFrame/staggerFrames) % spriteAnimations[playerState].loc.length;
    let frameX = position * spriteWidth;
    let frameY = spriteAnimations[playerState].loc[position].y;

    ctx.drawImage(playerImage, // Which image to show
        frameX, frameY, spriteWidth, spriteHeight, // Which part of image to show
        0, 0, spriteWidth, spriteHeight  // Where to show the image
    );

    gameFrame++;

    requestAnimationFrame(animate);
}

animate();