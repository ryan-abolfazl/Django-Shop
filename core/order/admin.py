from django.contrib import admin
from .models import CouponModel, OrderStatusType, OrderModel, OrderItemModel, UserAddressModel

@admin.register(OrderModel)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "total_price",
        "coupon",
        "status",
        "created_date",
        )
    

@admin.register(OrderItemModel)
class OrderItemModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "order",
        "product",
        "quantity",
        "price",
        "created_date",
        )
@admin.register(UserAddressModel)
class UserAddressModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "address",
        "state",
        "city",
        "zip_code",
        "created_date",
        )
@admin.register(CouponModel)
class CouponModelAdmin(admin.ModelAdmin):
    list_display = (
        "code",
        "discount_pecent",
        "max_limit_usage",
        "used_by_count",
        "expiration_date",
        "created_date",
        )
    
    def used_by_count(self, obj):
        return obj.used_by.all().count()
    
