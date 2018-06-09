$(function () {

    // 全部类型
    $('#child_type').click(function () {
        $('#child_type_container').toggle();  // 切换显示和隐藏
        $('#child_type_icon').toggleClass('glyphicon-chevron-down').addClass('glyphicon-chevron-up')

        // 主动触发$('#sort_rule_container')的click事件
        $('#sort_rule_container').trigger('click')
    });

    $('#child_type_container').click(function () {
        $(this).hide();  //隐藏
        $('#child_type_icon').removeClass('glyphicon-chevron-up').addClass('glyphicon-chevron-down')
    });

    //排序规则
    $('#sort_rule').click(function () {
        $('#sort_rule_container').toggle();  // 切换显示和隐藏
        $('#sort_rule_icon').toggleClass('glyphicon-chevron-down').addClass('glyphicon-chevron-up')

        // 主动触发$('#child_type_container')的click事件
        $('#child_type_container').triggerHandler('click');
    });

    $('#sort_rule_container').click(function () {
        $(this).hide();
        $('#sort_rule_icon').removeClass('glyphicon-chevron-up').addClass('glyphicon-chevron-down')

    });


// 加入购物车

    // 数量+
    $('.add').click(function () {
        // index = $(this).index('.add');
        // num = $('.number').eq(index)
        $number = $(this).parent().find('.number');
        $number.html( parseInt($number.html()) + 1 );

    });

    // 数量-
    $('.reduce').click(function () {
        $number = $(this).parent().find('.number');
        num = parseInt($number.html()) - 1;
        if (num < 1) {
            num = 1
        }
        $number.html( num );
    });


    // 点击‘加入购物车’
    $('.addtocart').click(function () {
        //商品id: 获取当前要加入购物车的商品的id
        goodsid = $(this).attr('goodsid');

        //商品数量
        num = parseInt($(this).prev().find('.number').html());

        //ajax提交给后台
        $.get('/app/addtocart/', {'goodsid': goodsid, 'num': num}, function(data) {
            // console.log(data);

            if (data.status == 1){
                console.log('加入购物车成功')

            }
            else if(data.status == 0 ){
                print('111')
                location.href = '/app/login/'
            }


            else {
                console.log('加入购物车失败')
            }
        })


    })




});