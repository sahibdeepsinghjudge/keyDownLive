
$(function () {
  $(document).scroll(function () {
      var $nav = $(".navi");
      $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
  });
});




function navOpen(){
  $('.ios-side-nav').css('left','0px');
  $('.nav-open').css('font-size','0px');
}
function navClose(){
$('.ios-side-nav').css('left','-300px');
$('.nav-open').css('font-size','23px');
}



$(document).ready(function(){
// Add smooth scrolling to all links
$("a").on('click', function(event) {

  // Make sure this.hash has a value before overriding default behavior
  if (this.hash !== "") {
    // Prevent default anchor click behavior
    event.preventDefault();

    // Store hash
    var hash = this.hash;

    // Using jQuery's animate() method to add smooth page scroll
    // The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area
    $('html, body').animate({
      scrollTop: $(hash).offset().top
    }, 800, function(){

      // Add hash (#) to URL when done scrolling (default click behavior)
      window.location.hash = hash;
    });
  } // End if
});
});



$( function() {
$( ".ddp" ).on( "click", function() {
 $(".popup-bg").css('display','none')
});
} );
$( function() {
  $( ".ddp" ).on( "click", function() {
   $("#notifi").css('display','none')
  });
  } );
  $( function() {
    $( ".ddp" ).on( "click", function() {
     $("#delete").css('display','none')
    });
    } );
    $( function() {
      $( ".dpp2" ).on( "click", function() {
       $("#delete").css('display','none')
      });
      } );
$( function() {
$( ".openPOP" ).on( "click", function() {
 $(".popup-bg").css({'display':'block'},1000)
 $(".openPOP").toggleClass('active',1000)
 $(".all").toggleClass('animatedUP',1000)
});
} );

$( function() {
  $( ".openPOP2" ).on( "click", function() {
   $("#notifi").css({'display':'block'},1000)
   $(".openPOP2").toggleClass('active',1000)
   $(".all").toggleClass('animatedUP',1000)
  });
  } );

  $( function() {
    $( ".openPOP3" ).on( "click", function() {
     $("#delete").css({'display':'block'},1000)
     $(".openPOP3").toggleClass('active',1000)
     $(".all").toggleClass('animatedUP',1000)
    });
    } );

$( function(){
$(".sl1").on('click',function(){
$(".sl1 .side-li-ul").toggleClass("show");
$(".sl2 .side-li-ul").removeClass("show");
  $(".sl3 .side-li-ul").removeClass("show");
})});

$( function(){
$(".sl2").on('click',function(){
  $(".sl2 .side-li-ul").toggleClass("show");
  $(".sl3 .side-li-ul").removeClass("show");
  $(".sl1 .side-li-ul").removeClass("show");
})});

$( function(){
$(".sl3").on('click',function(){
  $(".sl3 .side-li-ul").toggleClass("show");
  $(".sl2 .side-li-ul").removeClass("show");
  $(".sl1 .side-li-ul").removeClass("show");
})});


$( function(){
  $(".toggle-btn").on('click',function(){
  $(".sidebar-ios").toggleClass("show-bar");
  $(".toggle-btn").toggleClass("move-icon");
})});

$( function(){
$(".checkbtn").on('click',function(){
$(".menu").toggleClass("menu-show");
})});


$(function(){
$('.ios-control-textarea').on('click', function(){
  var plan=$('#plan').find(":selected").text();
  if(plan=="Simple $49"){
    $('.addon').addClass('show-add');
  }
  else{
    $('.addon').removeClass('show-add');
  }
})
})
