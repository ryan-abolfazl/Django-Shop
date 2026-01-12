from django.contrib.auth import forms as auth_forms
from django import forms
from django.utils.translation import gettext_lazy as _
from accounts.models import Profile
from shop.models import ProductModel


class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel

        fields = [
        "category",
        "title",
        "slug",
        "image",
        "description",
        "brief_description",
        "status",
        "stock",
        "price",
        "discount_percent",
        ]

