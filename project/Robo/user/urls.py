from django.urls import path
from . import views

urlpatterns = [
    path('getRobo/'.views.roboData.as_view())

]