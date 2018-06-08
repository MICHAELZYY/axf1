$(function () {

    $('#login').click(function(){
        $('#password').val(md5($('#password').val()))
    })

});