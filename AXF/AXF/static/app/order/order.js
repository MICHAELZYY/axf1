$(function () {

    //点击支付
    $('#pay').click(function () {

        //支付完成后, 需要将订单状态更改
        $.get('/app/orderchangestatus/',{'orderid':$(this).attr('orderid'),'status':'1'},function (data) {

            if (data.status==1){
                console.log(data)
                console.log('点击支付')
                location.href = '/app/orderpaid/'

            }
            else {
                console.log(data.msg)
            }
        })

    })

});




