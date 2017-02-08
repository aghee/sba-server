from django.contrib import admin
from .models import UserProfile,Category,Product,Business,Sales


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','phone_number','profile_image','national_id')

class CategoryAdmin(admin.ModelAdmin):
    list_display=("name",)

class ProductAdmin(admin.ModelAdmin):
    list_display=('product_name','product_category','unit_price','shiping_price','shiped_on','end_on')

class BusinessAdmin(admin.ModelAdmin):
    list_display=('name','get_products','county','owner','city','street',)

class SalesAdmin(admin.ModelAdmin):
    list_display=('product','units','sold_at','business')

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Business,BusinessAdmin)
admin.site.register(Sales,SalesAdmin)