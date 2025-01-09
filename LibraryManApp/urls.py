from django.urls import path
from .views import *

urlpatterns = [
    path('', Home),
    path('shop' ,Shopping ),
    path('save',Saving),
]
