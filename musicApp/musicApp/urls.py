"""musicApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from website.views import index, get_all_artists, save_artist, add_artist, artist_details, all_artists

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index, name='index'),
    url(r'^get-artists/$', get_all_artists, name='get_all_artists'),
    url(r'^save-artist/$', save_artist, name='save_artist'),
    url(r'^templates/add-artist.html$', add_artist, name='add_artist'),
    url(r'^templates/artist-details$', artist_details, name='artist_details'),
    url(r'^templates/all-artists$', all_artists, name='all_artist'),
]
