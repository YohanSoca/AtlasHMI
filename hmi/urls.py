from django.urls import path, include


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('status', views.status, name='status'),
    path('setCoil', views.setCoil, name='setCoil')
]