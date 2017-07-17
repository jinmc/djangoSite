from django.shortcuts import render, get_object_or_404
from .models import Album
from django.http import Http404
from django.http import HttpResponse



def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums': all_albums}
    return render(request, 'music/index.html', context)


def detail(request, album_id):
    # return HttpResponse("<h2>Details for Album id: " + str(album_id) + "</h2>")

    # try:
    #     album = Album.objects.get(pk=album_id)
    # except Album.DoesNotExist:
    #     raise Http404("Album does not exist")
    album = get_object_or_404(Album, pk=album_id) # same as above code
    return render(request, 'music/detail.html', {'album' : album})
