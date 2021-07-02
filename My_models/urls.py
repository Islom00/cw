from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    #function_based
    path("user", views.users),
    path("form", views.form),
    #class_based
    path("user_cbv", TemplateView.as_view(template_name="Users/users.html")),
    path("form_cbv", TemplateView.as_view(template_name="Users/form.html"))
]