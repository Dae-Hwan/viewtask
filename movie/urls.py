from django.urls import path
from movie.views import ActorView

urlpatterns = [
    path('/actor', ActorView.as_view())
]
