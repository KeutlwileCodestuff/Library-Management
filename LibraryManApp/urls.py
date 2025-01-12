from django.urls import path
from .views import *

urlpatterns = [
    path('home', Home),
    path('shop' ,Shopping ),
    path('save',Saving),
    path('books' , BOOKS),
    path('returns',RETURNS),
    path('my-bag',MY_BAG),
    path('readers',READERS)
]
