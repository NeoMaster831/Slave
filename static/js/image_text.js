var textElement = document.getElementById("centerText");
var isLightColor = true;

setInterval(function() {
    if (isLightColor) {
        textElement.style.color = "#dddddd"; // 진한 회색으로 변경
    } else {
        textElement.style.color = "#ffffff"; // 연한 회색으로 변경
    }
    isLightColor = !isLightColor;
}, 2500); // 1초마다 색상 변경