from django.db import models

class Actor(models.Model):
    first_name = models.CharField(max_length = 45, null = True)
    last_name = models.CharField(max_length = 45, null = True)
    date_of_birth = models.CharField(max_length = 45, null = True)
    movies = models.ManyToManyField('Movie', through = 'Actor_Movie')

    def __str__(self):
        return self.last_name

    class Meta():
        db_table = 'actor'


class Movie(models.Model):
    title = models.CharField(max_length = 45, null = True)
    release_date = models.CharField(max_length = 45, null = True)
    running_time = models.IntegerField(null = True)

    def __str__(self):
        return self.title

    class Meta():
        db_table = 'movie'

class Actor_Movie(models.Model):
    actor = models.ForeignKey('Actor', on_delete = models.CASCADE)
    movie = models.ForeignKey('Movie', on_delete = models.CASCADE)

    class Meta():
        db_table = 'actor_movie'
