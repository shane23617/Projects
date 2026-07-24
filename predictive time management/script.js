let seconds = 0;
let timer;

function startTimer() {
    timer = setInterval(updateTimer, 1000);
}

function updateTimer() {
    seconds++;
    document.getElementById("timer").textContent = seconds;
}

function stopTimer() {
    clearInterval(timer);
}

function resetTimer() {
    clearInterval(timer);
    seconds = 0;
    document.getElementById("timer").textContent = seconds;
}