from django.http import HttpResponseRedirect
from django.shortcuts import render
from encoder.models import VideoForm



# Imaginary function to handle an uploaded file.
# from somewhere import handle_uploaded_file


def upload_file(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = VideoForm()
    return render(request, 'base.html', {'form': form})
