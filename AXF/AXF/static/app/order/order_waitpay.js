$(function () {

    //提交待付款订单信息
    $('.waitpay').click(function () {
        // var a = $(this).parent().find('span').html()
        var order_id = $(this).siblings('p').find('span').html()
        // console.log('1111')
        console.log(order_id)

        $.get('/app/topaid/',{'order_id':order_id},function (data) {
            if (data.status ==1 ){
                console.log(data.orderid)
                location.href = '/app/order/' + data.orderid +'/'
                // location.href = '/app/order/' + data.orderid + '/'

            }
            else {
                console.log(data.msg)
            }
        })
    })

//    取消待付款订单

    $('.canclepay').click(function () {

        var order_id = $(this).siblings('p').find('span').html()
        console.log(order_id)
        $.get('/app/cancelpaid',{'order_id':order_id},function (data) {
            if (data.staus == 1 ) {
                location.reload()

            }
            else{
                console.log(data.msg)
            }
        })
    })


});

