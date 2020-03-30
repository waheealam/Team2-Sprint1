from django.conf.urls import url
from . import views
from django.urls import path, re_path

app_name = 'retirecenterapp'
urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),
    path('order_list', views.order_list, name='order_list'),
    path('order/create/', views.order_new, name='order_new'),
    path('order/<int:pk>/edit/', views.order_edit, name='order_edit'),
    path('order/<int:pk>/delete/', views.order_delete, name='order_delete'),
    path('profile_display', views.profile_display, name='profile_display'),
    path('profile_edit', views.profile_edit, name='profile_edit'),

]