

//设置中间调用函数
(function(){
    $.ajax({
        url:'/app/middle/',
        dataType:'json',
        type:'GET',
        success:function(data){
            if (data.code == '200'){
                show_cart()
                cart_price()
            }
        },
        error:function(data){
        }
    })
}())

// 显示购物车里面的全部shangpin
function show_cart(){
    $.ajax({
        url: '/app/gain_cart/',
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            alert(data.goods_list.length)
            // alert(data.goods_list[1].good[0].good_gpic)
            // alert(data.goods_list[1].good[0].good_gprice)
            // alert(data.goods_list[1].good[0].good_gtitle)
            // alert(data.goods_list[1].good[0].good_gunit)
            // alert(data.goods_list[1].good[0].good_id)
            // alert(data.goods_list[1].good[0].number)
            total_count = data.goods_list.length
            end_cart = ''
            $('.total_count').html('全部商品<em>'+total_count + '件</em>')
            $('#del').remove()
            for (var i = 0; i < data.goods_list.length; i += 1) {
                cart_shop = ''
                cart_shop = ''
                cart_shop += '<ul class="cart_list_td clearfix" id="del">'

                cart_shop += '<li class="col01"><input type="checkbox" checked id="check"></li>'
                cart_shop += '<li class="col02"><img src="/media/' + data.goods_list[i].good[0].good_gpic + '"></li>'
                cart_shop += '<li class="col03">' + data.goods_list[i].good[0].good_gtitle + '<br><em>' + data.goods_list[i].good[0].good_gprice + '元/' + data.goods_list[i].good[0].good_gunit + '</em></li>'
                cart_shop += '<li class="col04">' + data.goods_list[i].good[0].good_gunit + '</li>'
                cart_shop += '<li class="col05" id="' + data.goods_list[i].good[0].good_id + '">'+ data.goods_list[i].good[0].good_gprice+'元</li>'
                cart_shop += '<li class="col06"> <div class="num_add"> <a href="javascript:;" class="add fl" onclick="add_count(' + data.goods_list[i].good[0].good_id + ')">+</a><input id="' + data.goods_list[i].good[0].good_id + '" type="text" class="num_show fl" value="' + data.goods_list[i].good[0].number + '"> <a href="javascript:;" class="minus fl" onclick="sub_count(' + data.goods_list[i].good[0].good_id + ')">-</a></div></li>'
                cart_shop += '<li class="col07" id="t_price' + data.goods_list[i].good[0].good_id + '">' + data.goods_list[i].good[0].good_gprice + '元</li>'
                cart_shop += '<li class="col08"><a href="#" onclick="delete_one(' + data.goods_list[i].good[0].good_id + ')">删除</a></li>'
                cart_shop += '</ul>'

            end_cart += cart_shop
            }
        $('.cart_list_th').html(end_cart)
        },
        error: function (data) {
            alert('error')
        }
    })}


//在购物车减少商品数量
function sub_count(id){
    var csrf = $('input[name="csrfmiddlewaretoken"]').val()
    $.ajax({
        url:'/app/sub_count/',
        type:'POST',
        dataType:'json',
        data:{'id':id},
        headers:{'X-CSRFToken':csrf},
        success:function(data){
            $('#'+id).val(data.number)
            show_cart()
            cart_price()
        },
        error:function(data){
            alert('请求失败')
        }
    })
}

//算出购物车里每个商品的的总价格价格
function cart_price(){
    $.ajax({
        url: '/app/cart_total_price/',
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            total_list = data.total_list
            for (var i = 0; i < total_list.length; i += 1) {
                $('#t_price' + total_list[i].id).html(total_list[i].total_price)
            }
        },
        error: function (data) {
            alert('请求失败')
        }
    })}



//增加购物车里的商品的数量
function add_count(id){
    var csrf = $('input[name="csrfmiddlewaretoken"]').val()
    $.ajax({
        url:'/app/add_count/',
        type:'POST',
        dataType:'json',
        data:{'id':id},
        headers:{'X-CSRFToken':csrf},
        success:function(data){
            $('#'+id).val(data.number)
            cart_price()
            show_cart()
        },
        error:function(data){
            alert('请求失败')
        }
    })
}
//全选按钮
function is_select(){
     var csrf = $('input[name="csrfmiddlewaretoken"]').val();
     var checked = $('#selected').attr('checked')
    $.ajax({
        url:'/app/all_choice/',
        type:'POST',
        dataType:'json',
        data:{'checked':checked},
        headers:{'X-CSRFToken':csrf},
        success:function(data){
            if(data.is_checked){

                $('.col01 > input').attr('checked',true)
                location.href = '/app/cart/'
            }
            else{
                $('.col01 > input').attr('checked',false)

            }
        },
        error:function(data){
            alert('请求失败')
        }
    })
}

// 删除单个商品
function delete_one(id){
    var csrf = $('input[name="csrfmiddlewaretoken"]').val()
    $.ajax({
        url:'/app/delete_one/',
        type:'POST',
        dataType:'json',
        data:{'id':id},
        headers:{'X-CSRFToken':csrf},
        success:function(data){
            if(data.code == '200'){
                  show_cart()
            }
        },
        error:function(data){

        }
    })
}

// 算出购物车的总价格和总商品件数

(function total_count(){
     var csrf = $('input[name="csrfmiddlewaretoken"]').val()
    $.ajax({
        url:'/app/total_count/',
        type:'GET',
        dataType:'json',
        success:function(data){
            if(data.code == '200'){
                $('#all_price').html('合计(不含运费)：<span>¥</span><em>'+data.all_price+'</em><br>共计<b>'+ data.count +'</b>件商品')
            }
        },
        error:function(data){

        }
    })
}())

// 把商品加入到商品的订单
function one_order() {
     var csrf = $('input[name="csrfmiddlewaretoken"]').val()
    $.ajax({
        url: '/app/all_order/',
        type: 'POST',
        dataType: 'json',
        headers:{'X-CSRFToken':csrf},
        success: function (data) {
            if (data.code == '200') {
                location.href = '/app/place_order/'+ data.order +'/'

            }
        },
        error: function (data) {

        }
    })
}











































