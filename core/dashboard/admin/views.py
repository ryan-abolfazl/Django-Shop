from django.shortcuts import render
from django.views.generic import View, TemplateView

class AdminDashboardHomeView(TemplateView):
    template_name = "dashboard/admin/home.html"