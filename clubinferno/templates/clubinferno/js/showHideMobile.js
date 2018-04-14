function showHideMobile() {
    $(".hamburger").toggleClass('active');
    $(".hamburger").parent('.menu').toggleClass('active');
    $('.dimmer').toggleClass('active');
    $('body').toggleClass('no-scrolling');
}