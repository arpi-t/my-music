import json

import bs4
from django.db.models import Q
import requests


def get_download_link(name, instance):
    from songs_scrapper.models import Songs

    song = Songs.objects.filter(Q(song_id=instance.song_id) | Q(name__iexact=instance.name)).first()
    if song:
        return song, False
    else:
        if instance.song_id:
            download_url_data = 'http://clip.dj/update.php?id={}&f=mp3'.format(instance.song_id)
            resp = requests.get(download_url_data)
            instance.download_url = json.loads(resp.text).get('file', '')

        else:
            instance.name = name.strip()
            if instance.name:
                instance.original_url = 'https://www.youtube.com/results?search_query={}'.format(
                    instance.name.replace(' ', '+'))
                resp = requests.get(instance.original_url)
                tree = bs4.BeautifulSoup(resp.text)
                first_song = tree.select('.yt-lockup.yt-lockup-tile')[0]
                if first_song:
                    instance.song_id = first_song.attrs.get('data-context-item-id')
                    download_url_data = 'http://clip.dj/update.php?id={}&f=mp3'.format(instance.song_id)
                    resp = requests.get(download_url_data)
                    instance.download_url = json.loads(resp.text).get('file', '')
    return instance, True
