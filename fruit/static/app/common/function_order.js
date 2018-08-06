//定义中间函数
$.get('/app/show_order/',function(data){
    if(data.code == '200'){
         create_order()

    }
})


// 在详情订单裂变拿出数据
function create_order(){
}
    var order = $('#order').text()
    var csrf = $('input[name="csrfmiddlewaretoken"]').val()
    $.ajax({
        url:'/app/look_order/',
        type:'POST',
        data:{'order':order},
        dataType:'json',
        headers:{'X-CSRFToken':csrf},
        success:function(data){
            if(data.code == '200'){
                for(var i=0;i<data.order_goods.length;i+=1){
                    // alert(data.order_goods[i].good[0].price)
                    // alert(data.order_goods[i].good[0].count)
                    // alert(data.order_goods[i].good[0].img)
                    // alert(data.order_goods[i].good[0].gunit)
                    // alert(data.order_goods[i].good[0].good_id)
                    // alert(data.order_goods[i].good[0].good_title)
                    index = parseInt(i)+1
                    order = ''
                    	order += '<ul class="goods_list_td clearfix">'
			order += '<li class="col01">'+ index +'</li>'
			order += '<li class="col02"><img src="/media/'+data.order_goods[i].good[0].img+'"></li>'
			order += '<li class="col03">'+data.order_goods[i].good[0].good_title+'</li>'
			order += '<li class="col04">'+data.order_goods[i].good[0].gunit+'</li>'
			order += '<li class="col05">'+data.order_goods[i].good[0].good_price+'元</li>'
			order += '<li class="col06">'+data.order_goods[i].good[0].count+'</li>'
			order += '<li class="col07">'+data.order_goods[i].good[0].price+'</li></ul>'

                    $('#order_list_all').append(order)
                }
                total_pay = parseInt(data.end_price) + 10
                $('.total_goods_count').html('共<em>'+ data.order_goods.length +'</em>件商品<b>'+ data.end_price+ '</b>')
                $('.total_pay').html('实付款：<b>'+ total_pay +'</b>')
            }
        },
        error:function(data){

        }

    })

//提交订单,我要把购物车全部清空，改变商品的支付状态
function change_status(){
    var order = $('#order').text()
    var csrf = $('input[name="csrfmiddlewaretoken"]').val()
        $.ajax({
            url: '/app/pay_order/',
            type: 'POST',
            data: {'order': order},
            dataType: 'json',
            headers: {'X-CSRFToken': csrf},
            success: function (data) {
                if (data.code == '200') {
                    alert('0000000000000000')
                    location.href = '/app/user_center_order/'
                }
            },
            error: function (data) {

            }
        })
}
































