from django.shortcuts import render, redirect
import youtube_dl
from main.models import Song
from .forms import DownloadForm


def download(request):
    form = DownloadForm()
    if request.method == "POST":
        form = DownloadForm(request.POST)
        print(request.POST)
        if form.is_valid():
            video_url = form.cleaned_data.get('url')
            Song.objects.create(link=video_url)
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }]}
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                # ydl.download([video_url])
                info = ydl.extract_info(video_url, download=False)

                return redirect(info['formats'][0]['url'])

    return render(request, "index.html", context={
        'form': form,
    })
