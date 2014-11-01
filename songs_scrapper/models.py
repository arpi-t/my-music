from django.db import models
from songs_scrapper.utils import get_download_link


class Songs(models.Model):
    name = models.CharField(max_length=256)
    song_id = models.CharField(max_length=256, unique=True)
    download_url = models.URLField()
    original_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '{} -- {} -- {}'.format(self.name, self.song_id, self.download_url)

    def get_download_link(self):
        return get_download_link(self.name, self) if self.download_url is None else self.download_url
    
    def save(self, **kwargs):
        if not self.song_id:
            return 
        else:
            return super(Songs, self).save(**kwargs)