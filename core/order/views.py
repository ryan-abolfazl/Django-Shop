from django.views.generic import (
    TemplateView,
    FormView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from .permissions import HasCustomerAccessPermission
from .models import UserAddressModel
from cart.models import CartModel
from .forms import CheckOutForm
from django.urls import reverse_lazy
from order.models import OrderModel, OrderItemModel
from cart.cart import CartSession
from decimal import Decimal


class OrderCheckoutView(LoginRequiredMixin, HasCustomerAccessPermission, FormView):
    template_name = 'order/checkout.html'
    form_class = CheckOutForm
    success_url = reverse_lazy("order:completed")


    def get_form_kwargs(self):
        kwargs = super(OrderCheckoutView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs
    
    def form_valid(self, form):
        user = self.request.user
        cleaned_data = form.cleaned_data
        address = cleaned_data['address_id']
        coupon = cleaned_data['coupon']

        cart = CartModel.objects.get(user=user)
        order = self.create_order(address)

        self.create_order_items(order, cart)
        self.clear_cart(cart)

        total_price = order.calculate_total_price()
        self.apply_coupon(coupon, order, user, total_price)
        order.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)

    def create_order(self, address):
        return OrderModel.objects.create(
            user=self.request.user,
            address=address.address,
            state=address.state,
            city=address.city,
            zip_code=address.zip_code,
        )

    def create_order_items(self, order, cart):
        for item in cart.cart_items.all():
            OrderItemModel.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.get_price(),
            )

    def clear_cart(self, cart):
        cart.cart_items.all().delete()
        CartSession(self.request.session).clear()

    def apply_coupon(self, coupon, order, user, total_price):
        if coupon:
            discount_amount = round(
                (total_price * Decimal(coupon.discount_percent / 100)))
            total_price -= discount_amount

            order.coupon = coupon
            coupon.used_by.add(user)
            coupon.save()

        order.total_price = total_price

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        cart = CartModel.objects.get(user=self.request.user)
        context["addresses"] = UserAddressModel.objects.filter(user=self.request.user)
        total_price = cart.calculate_total_price()
        context["total_price"] = total_price
        context["total_tax"] = round((total_price * 12)/100)
        return context
    
class OrderCompletedView(LoginRequiredMixin, HasCustomerAccessPermission, TemplateView):
    template_name = 'order/completed.html'
