var images = [
    "../static/images/1.webp",
    "../static/images/2.webp",
    "../static/images/3.webp"
]

var currentIndex = 0;
var imageElement = document.getElementById("rotatingImage");

function changeImage() {
    imageElement.style.filter = "brightness(0%)"; 

    setTimeout(function() {
        currentIndex = (currentIndex + 1) % images.length;
        imageElement.src = images[currentIndex];
        imageElement.style.filter = "brightness(30%)"; 
    }, 2000);
}

setInterval(changeImage, 5000); 