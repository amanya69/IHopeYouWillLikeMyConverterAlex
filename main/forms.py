from django import forms
from .models import Song

class DownloadForm(forms.ModelForm):
    class Meta:
        model = Song
        exclude = ['link']
    url = forms.RegexField(regex=r'^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+$')

    def __unicode__(self):
        return "Request " + '#' + str(self.id)



