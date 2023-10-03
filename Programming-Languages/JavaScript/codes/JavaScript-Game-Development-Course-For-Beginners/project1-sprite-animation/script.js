const canvas = document.getElementById('canvas1');
const ctx = canvas.getContext('2d');

// Canvas setup
const CANVAS_WIDTH = canvas.width = 600;
const CANVAS_HEIGHT = canvas.height = 600;

const playerImage = new Image();
playerImage.src = 'shadow_dog.png';

// What happens in every frame
function animate() {
    ctx.clearRect(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT);
    ctx.drawImage(playerImage, // Which image to show
        0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, // Which
    );
    requestAnimationFrame(animate);
}

animate();