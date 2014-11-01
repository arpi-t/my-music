from django import forms
from songs_scrapper.models import Songs


class SongInputForm(forms.ModelForm):

    song_list = forms.CharField(widget=forms.Textarea(), required=False, label='Songs names')

    class Meta:
        model = Songs
        fields = ['name', 'song_id']

    def __init__(self, **kwargs):
        super(SongInputForm, self).__init__(**kwargs)
        self.fields['song_id'].required = False
        self.fields['name'].required = False
