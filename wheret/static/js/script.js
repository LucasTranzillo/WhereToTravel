var target_date = new Date("February 22, 2021").getTime();
var days, hours, minutes, seconds;
var regressive = document.getElementById("regressive");

setInterval(function countdown() {

    var current_date = new Date().getTime();
    var seconds_f = (target_date - current_date) / 1000;

days = parseInt(seconds_f / 86400);
    seconds_f = seconds_f % 86400;

    hours = parseInt(seconds_f / 3600);
    seconds_f = seconds_f % 3600;

    minutes = parseInt(seconds_f / 60);
    seconds = parseInt(seconds_f % 60);

    document.getElementById('day').innerHTML = days;
document.getElementById('hour').innerHTML = hours;
document.getElementById('minute').innerHTML = minutes;
document.getElementById('second').innerHTML = seconds;

}, 1000);