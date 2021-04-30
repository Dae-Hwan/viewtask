from django.urls import path
from owner.views import *

urlpatterns = [
    path('/owner', OwnerView.as_view()),
    path('/dog', DogView.as_view())
]
