
$.get('/app/show_user/',function(data){
    if (data.code == '200'){
        user_str = ''
        user_str += '<li><span>用户名:</span>'+ data.user.uname  +'</li>'
        user_str += '<li><span>联系方式：</span>'+ data.user.uphone +'</li>'
        user_str += '<li><span>联系地址：</span>'+ data.user.uaddress +'</li>'


        $('.user_info_list').html(user_str)
    }
})

















