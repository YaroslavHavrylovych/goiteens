var buttonObj = null;

function youveGotMe() {
    alert("You've got me");
}

function runButtonRun() {
    buttonObj = document.getElementById('running_button');
    var height = $(window).height();
    var width = $(window).width();
    var x = Math.random() * (width - 20) + 10 + 'px';
    var y = Math.random() * (height - 20) + 10 + 'px';
    buttonObj.style.left = x;
    buttonObj.style.top = y;
}

function init() {
    buttonObj = document.getElementById('running_button');
    buttonObj.style.position = 'relative';
    buttonObj.style.left = '100px';
    buttonObj.style.right = '100px';
}
