from django.urls import path
from .views import *

urlpatterns = [
    path('signin', signin),
    path('signup', signup),
    path('signout', signout),
    #path('signup_res', signup_res),

]