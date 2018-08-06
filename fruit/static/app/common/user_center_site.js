

//展示默认的地址
$.get('/app/show_user/',function(data){
    if (data.code == '200'){
        user_str = ''
        user_str += '<dl><dt>当前地址：</dt>'
		user_str += '<dd>'+ data.user.uaddress +'（'+ data.user.ushow+ ' 收'+ data.user.uphone+')</dd>'
        user_str += '</dl>'
        $('#adress').html(user_str)
    }
})


$('.info_submit').click(function(e){

    var csrf = $('input[name="csrfmiddlewaretoken"]').val()
    var consignee = $('#consignee').val()
    var phone = $('#phone').val()
    var address = $('#address').val()
    var email = $('#email').val()
    $.ajax({
        url:'/app/add_address/',
        type:'POST',
        dataType:'json',
        data:{'consignee':consignee,'phone':phone,'address':address,'email':email},
        headers:{'X-CSRFToken':csrf},
        success:function(data){
            alert('success')
        },
        error:function(data){

        }

    })
})



















































