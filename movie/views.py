import json

from django.http import JsonResponse
from django.views import View
from movie.models import Actor, Movie, Actor_Movie

class ActorView(View):
    def get(self, request):
        results = []
        actors = Actor.objects.all()
        for actor in actors:
            movie_list = []
            movies = actor.movies.all()
            for movie in movies:
                movie_list.append({'movie_name': movie.title}) 
            results.append(
                    {
                        'first_name': actor.first_name,
                        'last_name': actor.last_name,
                        'date_of_birth': actor.date_of_birth,
                        'movies_list': movie_list
                    }
            )

        return JsonResponse({'results': results}, status = 200)
