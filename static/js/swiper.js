var swiper = new Swiper('.banner-swiper', {
    loop: true,
    speed: 2000, 
    effect: 'cube',
    grabCursor: true,
    cubeEffect: {
        shadow: true,
        slideShadows:true,
        shadowOffset: 20, 
        shadowScale: 0.94,
    },
    pagination: {
        el: '.swiper-pagination'
    },
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
    autoplay: {
        delay: 5000, // Set the delay in milliseconds (e.g., 5000 for 5 seconds)
        disableOnInteraction: false, // Allow manual navigation to override autoplay
    },

});