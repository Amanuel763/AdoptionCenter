from django.shortcuts import render, get_list_or_404

from adopt.models import Adopt


# Create your views here.
def adopt(request):
    featured = Adopt.objects.order_by('-created_date').filter(is_featured=True)

    data = {
        'featured': featured,
    }
    return render(request, 'adopts/adopt.html', data)



def search(request):
    adopts = Adopt.objects.all().order_by('-created_date')    # CHANGE

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            adopts = Adopt.objects.filter(description__icontains=keyword).order_by('-created_date')   # CHANGE
    
    




    data = {
        'adopts': adopts,
    }
    return render(request, 'adopts/search.html', data)