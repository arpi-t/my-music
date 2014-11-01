from django.contrib import admin

# Register your models here.
from songs_scrapper.models import Songs


class SongAdmin(admin.ModelAdmin):
    list_display = ['name', 'song_id', 'download_url', 'original_url']


admin.site.register(Songs, SongAdmin)

