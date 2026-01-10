from django.shortcuts import render
from django.views.generic import View, TemplateView

class CustomerDashboardHomeView(TemplateView):
    template_name = "dashboard/customer/home.html"