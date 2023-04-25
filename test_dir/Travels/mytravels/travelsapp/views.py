from django.shortcuts import render

def car_images(request):
    context={
        'name':'Laxmi Travels'
    }
    return render(request,'car_images.html',context=context)
