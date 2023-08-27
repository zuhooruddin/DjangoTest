
from django.urls import path,include
from . import views

from .views import *

urlpatterns=[

    path("adddata",views.savedata,name='adddata')

]