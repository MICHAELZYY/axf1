$(function () {

    // 轮播
    new Swiper('#topSwiper', {
         loop: true,
         pagination: '.swiper-pagination',

    });

    // 必购
    new Swiper('#swiperMenu', {
        slidesPerView: 3,
    })

});