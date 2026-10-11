from django.urls import path

from . import views

app_name = 'tenant'

urlpatterns = [
	path('', views.home, name='home'),
	path('tenants/', views.tenant_list, name='list'),
]
