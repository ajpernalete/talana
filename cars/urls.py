from django.urls import path

from . import views

app_name = 'cars'

urlpatterns = [
    path('<slug:slug>', views.CarDetailList.as_view(), name='car'), #id -> llave primaria o primary key

]