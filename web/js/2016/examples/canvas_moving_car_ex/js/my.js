var myGamePiece;
var img = new Image();
img.src = "car.png";

function startGame() {
    myGamePiece = new carComponent(img.naturalWidth, img.naturalHeight, img, 225, 225);
    myGameArea.start();
}

var myGameArea = {
    canvas : document.createElement("canvas"),
    start : function() {
        this.canvas.width = 1200;
        this.canvas.height = 480;
        this.context = this.canvas.getContext("2d");
        document.body.insertBefore(this.canvas, document.body.childNodes[0]);
        this.frameNo = 0;
        this.interval = setInterval(updateGameArea, 20);
        i = 0;
        window.addEventListener('keydown', function (e) {
            e.preventDefault();
            myGameArea.keys = (myGameArea.keys || []);
            myGameArea.keys[e.keyCode] = (e.type == "keydown");
        });
        window.addEventListener('keyup', function (e) {
            myGameArea.keys[e.keyCode] = (e.type == "keydown");            
        });
    },
    stop : function() {
        clearInterval(this.interval);
    },    
    clear : function() {
        this.context.clearRect(0, 0, this.canvas.width, this.canvas.height);
    }
};

function carComponent(width, height, img, x, y, type) {
    this.type = type;
    this.width = width;
    this.height = height;
    this.half_width = width / 2;
    this.half_height = height / 2;
    this.speed = 0;
    this.angle = 0;
    this.moveAngle = 0;
    this.x = x;
    this.y = y;    
    this.update = function() {
        ctx = myGameArea.context;
        ctx.save();
        ctx.translate(this.x + this.half_width, this.y + this.half_height);
        ctx.rotate(this.angle);
        ctx.drawImage(img, -this.half_width, -this.half_height, width, height);
        ctx.restore();    
    };
    this.newPos = function() {
        this.angle += this.moveAngle * Math.PI / 180;
        this.x += this.speed * Math.sin(this.angle);
        this.y -= this.speed * Math.cos(this.angle);
    };
}

function updateGameArea() {
    myGameArea.clear();
    myGamePiece.moveAngle = 0;
    myGamePiece.speed = 0;
    if (myGameArea.keys && myGameArea.keys[37]) {myGamePiece.moveAngle = -5; }
    if (myGameArea.keys && myGameArea.keys[39]) {myGamePiece.moveAngle = 5; }
    if (myGameArea.keys && myGameArea.keys[38]) {myGamePiece.speed= 5; }
    if (myGameArea.keys && myGameArea.keys[40]) {myGamePiece.speed= -5; }
    myGamePiece.newPos();
    myGamePiece.update();
}

