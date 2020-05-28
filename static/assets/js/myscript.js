function myLine(ele){
    var id = ele.id;
    document.getElementById(id).style.borderBottom="1px solid white";
}
function myRemoveLine(ele){
    var id = ele.id;
    document.getElementById(id).style.borderBottom="";
}

var slideIndex = 0;
var t;

function abc(){
    showSlides();
}

function showSlides(n) {
  clearTimeout(t);
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
  }
  if(n==0){
    slideIndex++;
  }
  else{
      slideIndex=n;
  }
  if (slideIndex > slides.length) {slideIndex = 1}    
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block"; 
  dots[slideIndex-1].className += " active";
  t=setTimeout(showSlides,7000,0);
}

function openSlide(ele){
    var id = ele.id;
    switch(id) {
        case 'slide1':
          showSlides(1);
          break;
        case 'slide2':
          showSlides(2);
          break;
        case 'slide3':
          showSlides(3);
          break;          
      }
}
function onSignIn(googleUser){
  var profile = googleUser.getBasicProfile();
     var user_name = profile.getName();
    alert(JSON.stringify(profile));
document.querySelector('#content').innerText=user_name;
}
function signOut(){
gapi.auth2.getAuthInstance().signOut().then(function(){
  document.querySelector('#content').innerText='';
});
}

function closePopUp(){
  var x = document.getElementById("fixedconstruction");
  if (x.style.display === "none") {
    x.style.display = "visible";
  } else {
    x.style.display = "none";
  }
}