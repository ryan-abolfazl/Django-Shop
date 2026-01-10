from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.permissions import HasAdminAccessPermission

class AdminDashboardHomeView(HasAdminAccessPermission,LoginRequiredMixin, TemplateView):
    template_name = "dashboard/admin/home.html"