from django.urls import path
from app.views import *

urlpatterns = [
    path("", home_view),
    path('<category>', merc_view),
]
