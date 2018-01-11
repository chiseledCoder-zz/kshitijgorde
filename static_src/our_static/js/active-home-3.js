(function ($) {
	"use strict";
    /*==================================
        Template Name: AboutMe | Personal Portfolio Template;
        Template Url: http://www.propertheme.com/html/about-me_preview;
        Template Author: CoderTheme;
        Authoor URL  : http://www.propertheme.com;   
        Descripation : Haith is a Landing Fully Responsive Template;
        Template Type: Personal Portfolio ;
        Create Date : 02/11/2017;
    ===================================*/

        /*===================
            All JS Here
        =======================*/

        /** preloder js **/
        /** menu stick js **/
        /** SmoothSroll js **/
        /** Scrollspy js **/
        /** hero-slider-area-active js **/
        /** progressbar js **/
        /** wow js **/
        /** portfolio js **/
        /** magnific js **/
        /** google-map js **/
        /** scrollUp js **/

        /**===================**/


        /*----------------------------
           preloder js
        ------------------------------ */
            $(".about-me-preloder").fadeOut(1000);

        /*===================
            menu stick js
        =======================*/
         var s = $("#menu-stick, #sticker-mobile");
            var pos = s.position();
            $(window).scroll(function () {
                var windowpos = $(window).scrollTop();
                if (windowpos > pos.top) {
                    s.addClass("stick");
                } else {
                    s.removeClass("stick");
                }
            });

            $('.meanmenu-wrap nav').meanmenu({
                meanScreenWidth: "768",
                meanMenuContainer: ".meanmenu-wrap"
            });

        /*===================
            slider-carousel
        ===================*/        
        $(".hero-slider-area-active").owlCarousel({
            items: 1,
            loop: true,
            nav: false,
            dots: true,
            autoplay: false,
        });

        /*===================
            SmoothSroll
        ===================*/
            $('.smooth, .smooth-scroll a').on('click', function (event) {
                var $anchor =$(this);
                var headerH ='62';
                $('html, body').stop().animate({
                    'scrollTop': $($anchor.attr('href')).offset().top - headerH + "px"
                }, 1200, 'easeInOutExpo');
                event.preventDefault();
            });

        /*====================
            Scrollspy
        ====================*/
        $('body').scrollspy({ target: '.navbar-collapse',offset: 95 })

        /*===================
            testimonial js
        =======================*/
     	$('.active-testimonial-carousel').owlCarousel({
     		items: 1,
     		nav: false,
    	    dots: false,
    	    pagination: true,
    	    loop:true,
            slideSpeed: 300,
            paginationSpeed: 400,
            singleItem: true,
            afterInit: makePages,
            afterUpdate: makePages
    	});
        function makePages() {
            $.each(this.owl.userItems, function(i) {
                $('.owl-controls .owl-page').eq(i)
                    .css({
                        'background': 'url(' + $(this).find('img').attr('src') + ')',
                        'background-size': 'cover'
                    })
            });
        }

        /*===================
            progressbar js
        =======================*/
        function animateElements() {
            $('.progressbar').each(function () {
                var elementPos = $(this).offset().top;
                var topOfWindow = $(window).scrollTop();
                var percent = $(this).find('.circle').attr('data-percent');
                var percentage = parseInt(percent, 10) / parseInt(100, 10);
                var animate = $(this).data('animate');
                    if (elementPos < topOfWindow + $(window).height() - 30 && !animate) {
                    $(this).data('animate', true);
                    $(this).find('.circle').circleProgress({
                        startAngle: -Math.PI / 2,
                        value: percent / 100,
                        size: 140,
                        thickness: 20,
                        emptyFill: "#c1c1c1",
                        fill: {
                            color: '#7C4BAB'
                        }
                    }).on('circle-animation-progress', function (event, progress, stepValue) {
                        $(this).find('div').text((stepValue*100).toFixed(1) + "%");
                    }).stop();
                }
            });
        }

        // Show animated elements
         animateElements();
        $(window).scroll(animateElements);        

        /*===================
            wow js
        =======================*/
        new WOW().init();

        /*===================
            portfolio js
        =======================*/
        // Portfolio hover effect init
        $('.container').imagesLoaded( function() {
    	    var $grid = $('.portfolio-items-active').isotope({
                itemSelector: '.grid-item',
                percentPosition: true,
                masonry: {
                    // use outer width of grid-sizer for columnWidth
                    columnWidth: '.grid-item'
                }
            });   
            // filter items on button click
            $('.portfolio-menu').on( 'click', 'button', function() {
                var filterValue = $(this).attr('data-filter');
                $grid.isotope({ 
                    filter: filterValue });
            });

                $('.portfolio-menu button').on('click', function(event) {
                $(this).siblings('.active').removeClass('active');
                $(this).addClass('active');
                event.preventDefault();
            });
        });

        /*===================
            magnific js
        =======================*/
        $('.portfolio-lightbox').magnificPopup({
                type: 'image',
                gallery: {
                enabled: true
            }    
        }); 
            
        /*===================
            google map js
        =======================*/
        var center = [51.507351, -0.127758];
            $('.map-marker')
            .gmap3({
            center: center,
            zoom: 13,
            mapTypeId : google.maps.MapTypeId.ROADMAP,
            scrollwheel: false,
            })
            .marker({
            position: center,
            icon: 'http://propertheme.com/html/images/tf-img/haith/marker.png',
            animation: google.maps.Animation.BOUNCE,
        });
            
        /*===================
            scrollUp js
        =======================*/
        $.scrollUp({
            scrollName: 'scrollUp', 
            scrollSpeed: 900,
            animation: 'fade',
            scrollText: '<i class="icofont icofont-rounded-up"></i>', 
            activeOverlay: false, 
        });
       
}) (jQuery);
