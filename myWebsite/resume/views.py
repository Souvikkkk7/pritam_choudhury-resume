from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request, 'resume/base.html')

def gallery(request):
    return render(request, 'resume/gallery.html')

def certificate(request):
    return render(request, 'resume/certificate.html')
