from django.contrib import admin

from app.models import UserInfo,GoodsInfo,TypeInfo


class UserAdmin(admin.ModelAdmin):
    list_display = ('id','uname','uemail','ushow','uaddress','uyoubian','uphone')
    search_fields = ('uemail','uphone')
    ordering = ('id',)

admin.site.register(UserInfo,UserAdmin)


class GoodsAdmin(admin.ModelAdmin):
    list_display = ('gtitle','gpic','gprice','isDelete','gunit','gclick','gjianjie','gkucun','gcontent')
    search_fields = ('id','gtitle')
    ordering = ('id',)

admin.site.register(GoodsInfo,GoodsAdmin)



class TypeAdmin(admin.ModelAdmin):
    list_display = ('ttitle',)
    ordering = ('id',)

admin.site.register(TypeInfo,TypeAdmin)