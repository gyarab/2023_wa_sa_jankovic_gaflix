from django.contrib import admin
from filmy.models import Movie, Director, Genre, Actor, Fotbal
class MovieAdmin(admin.ModelAdmin):
    list_display = ["id","name","year","footage","director"]
    list_display_links = ["id","name"]
    search_fields = ["id","name", "director__name"]
    list_filter = ["year","genres"]
    list_editable = ["year","footage", "director"]

    list_display = ["id", "name", "year", "footage", "director", "genres_display"]
    list_display_links = ["id", "name"]
    search_fields = ["=id", "name", "director__name"]
    list_filter = ["year", "genres"]
    list_editable = ["year", "footage"]


class DirectorAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "birth_year"]
    list_display_links = ["id", "name"]
    search_fields = ["=id", "name"]
    list_filter = ["birth_year"]
    list_editable = ["birth_year"]


class GenreAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_display_links = ["id", "name"]
    search_fields = ["=id", "name"]


class ActorAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "birth_year"]
    list_display_links = ["id", "name"]
    search_fields = ["=id", "name"]
    list_filter = ["birth_year"]
    list_editable = ["birth_year"]

class FotbalAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_display_links = ["id", "name"]
    search_fields = ["=id", "name"]
   

admin.site.register(Movie, MovieAdmin)

admin.site.register(Actor, ActorAdmin)

admin.site.register(Director, DirectorAdmin)

admin.site.register(Genre, GenreAdmin)
admin.site.register(Fotbal, FotbalAdmin)