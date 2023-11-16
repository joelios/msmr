(function($) {
  "use strict"; // Start of use strict

  // Smooth scrolling using jQuery easing
  $('a.js-scroll-trigger[href*="#"]:not([href="#"])').click(function() {
    if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
      if (target.length) {
        $('html, body').animate({
          scrollTop: (target.offset().top - 70)
        }, 1000, "easeInOutExpo");
        return false;
      }
    }
  });

  // Closes responsive menu when a scroll trigger link is clicked
  $('.js-scroll-trigger').click(function() {
    $('.navbar-collapse').collapse('hide');
  });

  // Activate scrollspy to add active class to navbar items on scroll
  $('body').scrollspy({
    target: '#mainNav',
    offset: 100
  });

  // Collapse Navbar
  var navbarCollapse = function() {
    if ($("#mainNav").offset().top > 100) {
      $("#mainNav").addClass("navbar-shrink");
    } else {
      $("#mainNav").removeClass("navbar-shrink");
    }
  };
  // Collapse now if page is not at top
  navbarCollapse();
  // Collapse the navbar when page is scrolled
  $(window).scroll(navbarCollapse);
  
  // Closes responsive menu when a scroll trigger link is clicked
  $('#ideebtn').click(function() {
        console.log("bini da");
        var anlagedaten = {
            'vor_nachnamen': $("#inputname").val(),
            'email': $("#inputEmail").val(),
            'idee': $("#inputIdee").val()
        };
        console.log("hani Date:")
        console.log(anlagedaten)
        frappe.call({
            method: "msmr.www.msmr.create_idee.suche",
            args:{
                    'anlagedaten': anlagedaten
            },
            freeze: true,
            freeze_message: 'Ihre Idee wird eingereicht...',
            callback: function(r)
            {
                console.log("hani feedback")
                frappe.msgprint("Vielen Dank für Ihren Input!");
                $("#inputname").val('');
                $("#inputEmail").val('');
                $("#inputIdee").val('');
            }
        });
  });

})(jQuery); // End of use strict
