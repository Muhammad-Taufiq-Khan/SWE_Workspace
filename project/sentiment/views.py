from django.shortcuts import render
from django.http import HttpResponse
from .models import File
from .forms import MyForm


def my_form(request):
    saved = False
    if request.method == "POST":
        form = MyForm(request.POST, request.FILES)
        if form.is_valid():
            # file = File()
            # file.name = MyForm.cleaned_data["filename"]
            # file.file = MyForm.cleaned_data["file"]
            saved = True
            form.save()

            return HttpResponse("File has uploaded")
    else:
        form = MyForm()
    return render(request, 'homepage.html', {'form': form})














