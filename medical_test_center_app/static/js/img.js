// Automatic Slideshow - change image every 3 seconds
var myIndex = 0;
carousel();

function carousel() {
  // Get all elements with the class name "mySlides"
  var slides = document.getElementsByClassName("mySlides");

  // Hide all slides
  for (var i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }

  // Increment index and reset to 1 if it exceeds the number of slides
  myIndex++;
  if (myIndex > slides.length) {
    myIndex = 1;
  }

  // Display the current slide
  slides[myIndex - 1].style.display = "block";

  // Set a timeout to call the carousel function again after 3000 milliseconds (3 seconds)
  setTimeout(carousel, 3000);
}
