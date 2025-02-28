from django.urls import path
from gumisofts.views import *

urlpatterns = [path("", home, name="homr")]
