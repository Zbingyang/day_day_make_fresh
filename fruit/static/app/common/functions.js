
//页面加载完成的时候，自定刷新购物车里已经存在商品数量
(function show_cart(){
    $.ajax({
        url:'/app/get_cart/',
        type:'GET',
        dataType:'json',
        success:function(goods){
            message = goods.message
            for (var i=0;i<message.length;i+=1){
                $('#'+ message[i].id).val(message[i].number)
            }
        },
        error:function(message){
            alert('请求失败')
        }
    })
}())
// 加入购物车
function add_cart(id){
    var csrf = $('input[name="csrfmiddlewaretoken"]').val()
    var number  = $('#'+id).val()
    $.ajax({
        url:'/app/cart/',
        type:'POST',
        data:{'id':id,'number':number},
        dataType:'json',
        headers:{'X-CSRFToken':csrf},
        success:function(){
            alert('success')
        },
        error:function(){
            alert('error')
        }

    })
}

//点击按钮增加商品的数量

function add_num(id){
    var csrf = $('input[name="csrfmiddlewaretoken"]').val();
    var number = parseInt($('#'+ id).val());
    number += 1;
    $.ajax({
        type:'POST',
        url:'/app/add_cart/',
        dataType:'json',
        data:{'number':number,'id':id},
        headers:{'X-CSRFToken':csrf},
        success:function(data){
          if (data['code'] == '200'){
              $('#'+ id).val(data.number);
              refresh()
          }
        },
        error:function(data){
            alert('添加失败')
        }

    })

}

//点击按钮减少商品的数量
function sub_num(id){
    var csrf = $('input[name="csrfmiddlewaretoken"]').val();
    var number = parseInt($('#'+ id).val());
    $.ajax({
        type:'POST',
        url:'/app/sub_cart/',
        dataType:'json',
        data:{'id':id,'number':number},
        headers:{'X-CSRFToken':csrf},
        success:function(data){
            $('#'+ id).val(data.number)
            refresh()

        },
        error:function(data){
            alert('请求失败')
        }

    })
}

//页面加载完成时算出选择的商品的总价
function refresh(){
    var id = $('.num_add > input').attr('id');
    var csrf = $('input[name="csrfmiddlewaretoken"]').val();
    id = parseInt(id);
    $.ajax({
        url:'/app/total_price/',
        type:'POST',
        dataType:'json',
        data:{'id':id},
        headers:{'X-CSRFToken':csrf},
        success:function(data){
            $('#price'+ id).html('总价:<em>' + data.total_price + '</em>元')
        },
        error:function(data){

        }

    })
}



















