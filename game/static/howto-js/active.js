(function ($) {

    // Progress Bar Active Code
    if ($.fn.barfiller) {
        $('#bar1').barfiller({
            tooltip: true,
            duration: 1000,
            animateOnResize: true
        });
        $('#bar2').barfiller({
            tooltip: true,
            duration: 1000,
            animateOnResize: true
        });
        $('#bar3').barfiller({
            tooltip: true,
            duration: 1000,
            animateOnResize: true
        });
        $('#bar4').barfiller({
            tooltip: true,
            duration: 1000,
            animateOnResize: true
        });
        $('#bar5').barfiller({
            tooltip: true,
            duration: 1000,
            animateOnResize: true
        });
        $('#bar6').barfiller({
            tooltip: true,
            duration: 1000,
            animateOnResize: true
        });
        $('#bar7').barfiller({
            tooltip: true,
            duration: 1000,
            animateOnResize: true
        });
        $('#bar8').barfiller({
            tooltip: true,
            duration: 1000,
            animateOnResize: true
        });
        $('#bar9').barfiller({
            tooltip: true,
            duration: 1000,
            animateOnResize: true
        });
        $('#bar10').barfiller({
            tooltip: true,
            duration: 1000,
            animateOnResize: true
        });
        $('#bar11').barfiller({
            tooltip: true,
            duration: 1000,
            animateOnResize: true
        });
        $('#bar12').barfiller({
            tooltip: true,
            duration: 1000,
            animateOnResize: true
        });
    }

    // wow Active Code
    if ($.fn.init) {
        new WOW().init();
    }

})(jQuery);

var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}    
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";  
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";  
  dots[slideIndex-1].className += " active";
}