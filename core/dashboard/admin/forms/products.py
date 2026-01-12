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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["category"].widget.attrs["class"] = 'form-control'
        self.fields["title"].widget.attrs["class"] = 'form-control'
        self.fields["slug"].widget.attrs["class"] = 'form-control'
        self.fields["image"].widget.attrs["class"] = 'form-control'
        self.fields["description"].widget.attrs["class"] = 'form-control'
        self.fields["brief_description"].widget.attrs["class"] = 'form-control'
        self.fields["status"].widget.attrs["class"] = 'selected'
        self.fields["stock"].widget.attrs["class"] = 'number'
        self.fields["price"].widget.attrs["class"] = 'form-control'
        self.fields["discount_percent"].widget.attrs["class"] = 'form-control'