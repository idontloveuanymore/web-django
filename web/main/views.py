# views.py
import requests
from bs4 import BeautifulSoup as bs
from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return render(request, 'main/index.html')

def music(request):
    return render(request, 'main/music.html')

def get_recent_beatmaps():
    url = 'https://osu.ppy.sh/users/35292982/extra-pages/historical?mode=osu'
    response = requests.get(url).json()
    return response["recent"]

def get_lastfm_track(request):
    url = 'https://www.last.fm/ru/user/fade_awway'
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')

    img_tag = soup.find('td', class_='chartlist-image').find('img')
    image_url = img_tag['src']
    name_tag = soup.find('td', class_='chartlist-name').find('a')
    track_name = name_tag.text.strip()[:25] + '...' if len(name_tag.text.strip()) > 25 else name_tag.text.strip()
    artist_tag = soup.find('td', class_='chartlist-artist').find('a')
    artist_name = artist_tag.text.strip()[:25] + '...' if len(artist_tag.text.strip()) > 25 else artist_tag.text.strip()

    play_tag = soup.find('td', class_='chartlist-play')
    play_link_tag = play_tag.find('a', class_='js-playlink')
    play_url = None
    if play_link_tag:
        play_url = play_link_tag['href']

    scrobbling_tag = soup.find('span', class_='chartlist-now-scrobbling')
    scrobbling_state = None
    if scrobbling_tag:
        scrobbling_state = scrobbling_tag.find('a').text.strip()

    data = {
        "image_url": image_url,
        "track_name": track_name,
        "artist_name": artist_name,
        "play_url": play_url,
        "scrobbling_state": scrobbling_state
    }

    return JsonResponse(data)
