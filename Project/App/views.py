from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'pages/home.html')
def gallery_page(request):
    return render(request, 'pages/gallery.html')
def contact_page(request):
    return render(request, 'pages/contact.html')