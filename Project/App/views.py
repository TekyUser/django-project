from django.shortcuts import render

# Create your views here.
def home_page(request):
    featured_places = [
        {"image": "images/featured-reo-de-janeiro-brazil.jpg", "name": "Rio De Janeiro, Brazil", "des": ""},
        {"image": "images/featured-north-bondi-australia.jpg", "name": "North Bondi, Australia", "des": ""},
        {"image": "images/featured-berlin-germany.jpg", "name": "Berlin, Germany", "des": ""},
        {"image": "images/featured-khwaeng-wat-arun-thailand.jpg", "name": "Khwaeng Wat Arun, Thailand"},
        {"image": "images/featured-rome-italy.jpg", "name": "Rome, Italy"},
        {"image": "images/featured-fuvahmulah-maldives.jpg", "name": "Fuvahmulah, Maldives"},
    ]
    return render(request, 'pages/home.html', {"featured_places": featured_places})
def gallery_page(request):
    return render(request, 'pages/gallery.html')
def contact_page(request):
    return render(request, 'pages/contact.html')