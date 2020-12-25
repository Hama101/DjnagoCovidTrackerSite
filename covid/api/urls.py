from django.urls import path
from . import views as v

urlpatterns = [
    path('home/',v.home,name="home") ,
    path('showcovid/',v.showCovid , name="showcovid")
]