from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import  Location, Category, Photo

# Create your views here.
def index(request):

    '''
    view function to display landing page
    '''

    images = Photo.objects.all()

    return render(request, 'index.html', {"images": images,})


def search_results(request):

    '''
    view function to open search page and display searched images
    '''

    if 'search' in request.GET and request.GET["search"]:
        search_term = request.GET.get("search")
        images = Photo.search_image(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "images": images})

    

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
        

def sortby_locations(request):

    '''
    view function to display images sorted by Location
    '''

    images = Photo.filter_by_location()

    return render(request, 'location.html', {"images":images})

def single_image(request, image_id):

    '''
    view function to display a single image and its details
    '''

    image = Photo.get_image_by_id(image_id)
    return render(request, 'single_image.html', {"image":image})