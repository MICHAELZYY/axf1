$(function () {

    //数量加
    $('.add').click(function () {

        //    先获取要修改数量的购物车id

        var cartid = $(this).parents('.menuList').attr('cartid')

        // var num = $(this).prev().val()
        var that = this;

        //ajax
        $.get('/app/addnum/', {cartid: cartid}, function (data) {
            // console.log(data)
            //如果修改成功，则将页面中对应的数量节点改变
            if (data.status == 1) {
                $(that).prev().html(data.num)
            }
            else {
                console.log(data.msg)
            }
            //重新计算总价
            calculate();
        })
    });

    //数量减
    $('.reduce').click(function () {

        var cartid = $(this).parents('.menuList').attr('cartid')
        var that = this
        $.get('/app/reducenum/', {cartid: cartid}, function (data) {
            if (data.status == 1) {
                $(that).next().html(data.num)
            }
            else {
                console.log(data.msg)
            }
            //重新计算总价
            calculate();
        })


    })

    //删除
    $('.delbtn').click(function () {
        var cartid = $(this).parent().attr('cartid')
        var that = this
        $.get('/app/deletecart', {cartid: cartid}, function (data) {
            // console.log(data)
            if (data.status == 1) {
                // location.reload()
                $(that).parent().remove() //删除节点
            }
            else {
                console.log(data.msg)
            }
            // 重新判断是否全选
            isAllSelected()
        })

    })

//    勾选/取消勾选
    $('.select').click(function () {
        var cartid = $(this).parents('.menuList').attr('cartid')
        var that = this
        $.get('/app/cartselect/', {cartid: cartid}, function (data) {
            // console.log(data)
            if (data.status == 1) {
                if (data.is_select) {
                    $(that).find('span').html('√')
                }
                else {
                    $(that).find('span').html('')
                }
                // $(that).find('span').html(data.is_select1 ? '√' : '')
            }
            else
                {
                    console.log(data.msg)
                }
        // 重新判断是否全选
            isAllSelected()

        })
    });

    //全选

    // $('#allselect').click(function () {
    //
    //
    // //    1.如果当前全部勾选，则点击取消全选
    // //    2.如果当前未全部勾选，则点击全部选中
    //
    // //   先判断是否全部勾选了
    //     selects = [] //保存所有选中的cartid
    //     unselects = [] //保存所有未选中的cartid
    //     //遍历所有的li
    //     // print(selects,unselects)
    //     $('.menuList').each(function() {
    //         var select = $(this).find('.select>').children('span').html()
    //         // 如果是勾选,则添加到selects中
    //         if (select){
    //             selects.push($(this).attr('cartid'))
    //         }
    //         // 如果是未勾选,则添加到unselects中
    //         else {
    //              unselects.push($(this).attr('cartid'))
    //         }
    //     })
    //
    //     //当前全部被选中,则执行全不选
    //     if (unselects.length == 0){
    //         //ajax
    //         console.log('11111')
    //         $.get('/app/cartselectsall',{'action':'cancelselect','selects':selects.join('#')},function (data) {
    //             // console.log(data)
    //             if(data.status==1){
    //                 $('.select').find('span').html('')
    //             }
    //             else{
    //                 console.log(data.msg)
    //             }
    //         })
    //     }
    //     //当前未全选,则执行全选
    //     else{
    //         $.get('/app/cartselectsall',{'action':'select','selects':unselects.join('#')},function (data) {
    //             // console.log(data)
    //             if(data.status==1){
    //                 $('.select').find('span').html('√')
    //             }
    //             else{
    //                 console.log(data.msg)
    //             }
    //         })
    //     }
    // })

    //全选
    $('#allselect').click(function () {

        selects = []
        unselects = []

        $('.menuList').each(function () {
            var select = $(this).find('.select').children('span').html();
            if (select){
                selects.push($(this).attr('cartid'))
            }
            else{
                unselects.push($(this).attr('cartid'))

            }
        })
        // console.log(selects)
        // console.log(unselects)

        if(unselects.length==0){

            $.get('/app/cartselectall/',{'action':'cancelselect','selects':selects.join('#')},function (data) {

                if (data.status == 1){
                    $('.select').find('span').html('')
                }
                else{
                    console.log(data.msg)
                }
                // 重新判断是否全选
                isAllSelected()
            })
        }

        else{
            $.get('/app/cartselectall/', {'action': 'select', 'selects': unselects.join('#')}, function(data) {
                // console.log(data)

                if (data.status == 1){
                    $('.select').find('span').html('√')
                }
                else {
                    console.log(data.msg)
                }
                // 重新判断是否全选
                isAllSelected()

            });
        }

    })




    isAllSelected()
    //检测是否全选了
    function isAllSelected() {

        var count = 0;
        $('.select').each(function () {
            if ($(this).find('span').html()){
                count++;
            }

        });

        // console.log(count)
        // console.log($('.select').length)

        //如果全选了
        if(count==$('.select').length){
            console.log('说好的打钩')

            $('#allselect').find('span').html('√')
        }
        //否则不打钩
        else{
            console.log('说好的不打钩')
            $('#allselect').find('span').html('')

        }
        //重新计算总价
        calculate();
        // $('.select').each(function () {
        //     if($(this).find('span').html()==''){
        //         $('#allselect').find('span').html('')
        //     }
        //     else{
        //         $('#allselect').find('span').html('√')
        //
        //     }
        // })


    }

    // calculate()
    //计算总价
    function calculate() {

        //总价
        total= 0;
        //遍历所有的li
        $('.menuList').each(function () {
            if ($(this).find('.select').find('span').html()){
                //如果是勾选的,则计算价格
                price = parseFloat($(this).find('.price').html())  //取到单价
                num = parseInt($(this).find('.num').html())

                total +=price * num;
                // console.log(total)
            }
        });

        //显示总价
        // $('#totalprice').html(total.toFixed(2))
        $('#totalprice').html(total)

    }

    //结算生成订单
    $('#calculate').click(function () {

        //1 先获取购物车中勾选的所有商品

        //2 或直接让后台生成订单

        $.get('/app/orderadd',function (data) {
            // console.log(data)

            if(data.status == 1){
                location.href = '/app/order/' + data.orderid + '/'
            }
            else{
                console.log(data.msg)
            }
        })



    })

    // $('#calculate').click(function () {
    //     console.log('aaaaaa')
    // })


});


