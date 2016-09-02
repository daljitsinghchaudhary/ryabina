$(document).ready(function(){
    if (document.getElementById('swiper_header_hero')) {
        var swiperHero = new Swiper('#swiper_header_hero', {
            nextButton: $('#swiper_header_hero .swiper-button-next_small'),
            prevButton: $('#swiper_header_hero .swiper-button-prev_small'),
            pagination: $('#swiper_header_hero .swiper-pagination'),
            paginationClickable: true,
            slidesPerView: 'auto',
            centeredSlides: true,
            spaceBetween: 0,
            keyboardControl: true,
            effect: 'fade',
            speed: 800,
            loop: true,
            autoplay: 10000,
            autoplayDisableOnInteraction: false
        });
    }

    if (document.getElementById('swiper_discount')) {
        var swiperHero = new Swiper('#swiper_discount', {
            nextButton: $('#swiper_discount').parent().find('.swiper-button-next_discount'),
            prevButton: $('#swiper_discount').parent().find('.swiper-button-prev_discount'),
            slidesPerView: 'auto',
            centeredSlides: true,
            spaceBetween: 0,
            keyboardControl: true,
            effect: 'slide',
            speed: 800,
            loop: true
        });
    }

    var pw = $('.parallax-container');
    pw.parallax();

    $('.sticky-discount').stick_in_parent({
        parent: '[data-sticky_parent]',
        offset_top: 30
    });

    $('.newsboard_expand').click(function(){
       $(this).parent().removeClass('limited');
    });

     $(window).on('scroll load', function () {
            if ($(window).scrollTop() + $(window).height() > $('#wrapper_content').outerHeight()) {
                $('#wrapper_content').addClass('tight');
                $(window).trigger('resize.px.parallax');
            } else {
                $('#wrapper_content').removeClass('tight');
                $(window).trigger('resize.px.parallax');
            }
        });

    $('.service_isotope_grid').imagesLoaded( function() {
        $('.service_isotope_grid').isotope({
            itemSelector: '.service_isotope_item',
            layoutMode: 'fitRows',
            transitionDuration: 0
        });
    });
    $('.newsboard_isotope_grid').imagesLoaded( function() {
        $('.newsboard_isotope_grid').isotope({
            itemSelector: '.newsboard_isotope_item',
            layoutMode: 'masonry',
            transitionDuration: 0
        });
    });
});