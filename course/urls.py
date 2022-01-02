from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('course/', views.course, name='course'),
    path('ajax_audit', views.ajax_audit, name='ajax_audit'),

]