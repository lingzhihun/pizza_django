from django.urls import include, re_path
from . import views
app_name = 'pizzerias'
urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^pizza/$',views.pizza,name='pizza'),
    re_path(r'^pizza/?P<pizze_id>/d+$',views.Toppings,name='toppings')
]