$(function () {

    flag1 = false;  //表示用户名输入是否合法
    flag2 = false;  //表示密码输入是否合法
    flag3 = false;  //表示确认密码输入是否合法
    flag4 = false;  //表示邮箱输入是否合法

    // 用户名
    $('#username').change(function () {
        var v = $(this).val()
        // console.log(v)
        if (/^[a-zA-Z]\w{5,17}$/.test(v)) {
            // console.log('合法的用户名')
            flag1 = true;
            //如果输入格式正确，则验证用户名是否存在
            $.get('/app/checkusername',{username:$(this).val()},function (data) {
                if(data.status ==1){
                    $('#msg').html('用户名可以使用').css('color','green');

                }
                if(data.status ==0){
                    $('#msg').html('用户名已存在').css('color','red');

                }
                if(data.status == -1){
                    $('#msg').html('请求方式错误').css('color','orange');

                }


            })


        }
        else {
            // console.log('不合法的用户名')
            $('#msg').html('请输入6到18位的数字字母下划线且不能以数字开头的用户名').css('color','red');
            flag1 = false;

        }
    })

    $('#password').change(function () {
        var v = $(this).val()

        if (/^.{8,}$/.test(v)) {
            // console.log('可以使用该密码')
            $('#msg1').html('ok').css('color','green');
            flag2 = true;

        }
        else {
            // console.log('密码太短')
            $('#msg1').html('请输入8位以上的字符').css('color','red');

            flag2 = false;


        }
    });

    $('#again').change(function () {
        var v = $(this).val()
        // console.log(v)
        if (v == $('#password').val()) {
            // console.log('密码一致')
            $('#msg2').html('ok').css('color','green');

            flag3 = true;

        }
        else {
            // console.log('密码不一致')red
            $('#msg2').html('两次密码输入不一致').css('color','red');

            flag3 = false;

        }
    });

    $('#email').change(function () {
        var v = $(this).val()
        // console.log(v)
        if (/^\w+@\w+\.?\w+$/.test(v)) {
            // console.log('合法邮箱')
            $('#msg3').html('ok').css('color','green');

            flag4 = true;

        }
        else {
            // console.log('')
            $('#msg3').html('不合法的邮箱').css('color','red');

            flag1 = false;

        }
    })

//注册验证
    $('#register').click(function () {

        if (flag1 && flag2 && flag3 && flag4){


            //获取用户明文密码
            var username = $('#username').val()
            var password = $('#password').val()
            $.get('/app/getpwd/',{'username':username,'password':password},function (data) {
                if (data.status ==1){
                    console.log('密码保存Ok')
                }
                else{
                    console.log('register.js114行显示报错')
                }
            })



            $('#password').val(md5($('#password').val()));

            return true

        }
        else{
            // console.log('上面信息有误')
        $('#msg4').html('以上信息有误').css('color','red');

            return false
        }

    })






});