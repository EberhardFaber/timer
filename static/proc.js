let date = document.querySelector("date");
date.onchange = function(){
console.log(date.value);
}
year = 2020
month = "Sep"
day = 10
hour = 00
minute = 00
second = 00
var dat = month+" "+day+", "+year+" "+hour+":"+minute+":"+second
var deadline = new Date(dat).getTime();
var x = setInterval(function() {
var now = new Date().getTime();
var t = deadline - now;
var days = Math.floor(t / (1000 * 60 * 60 * 24));
var hours = Math.floor((t%(1000 * 60 * 60 * 24))/(1000 * 60 * 60));
var minutes = Math.floor((t % (1000 * 60 * 60)) / (1000 * 60));
var seconds = Math.floor((t % (1000 * 60)) / 1000);
document.getElementById("demo").innerHTML = days + "д "
+ hours + "ч " + minutes + "м " + seconds + "с ";
    if (t < 0) {
        clearInterval(x);
        document.getElementById("demo").innerHTML = "Время истекло";
    }
}, 1000);