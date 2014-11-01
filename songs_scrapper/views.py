from django.core.urlresolvers import reverse, reverse_lazy
from django.http.response import HttpResponseRedirect, HttpResponse
from django.views.generic import FormView
from songs_scrapper.forms import SongInputForm
from songs_scrapper.models import Songs
from songs_scrapper.utils import get_download_link


class HomeView(FormView):
    form_class = SongInputForm
    template_name = 'HomeView.html'
    songs = None
    success_url = reverse_lazy('home_view')

    def form_valid(self, form):
        songs = form.cleaned_data['song_list']
        if songs:
            song_list = songs.split('\r\n')
            self.songs = [get_download_link(song, Songs()) for song in song_list]
            Songs.objects.bulk_create([s[0] for s in self.songs if s[1]])
            self.songs = [s[0] for s in self.songs]
        else:
            song = get_download_link(form.cleaned_data['name'], form.instance)
            if song[1]:
                form.instance = song[0]
                form.save()
            self.songs = [song[0]]
        return self.render_to_response(self.get_context_data(form=form, songs=self.songs))
