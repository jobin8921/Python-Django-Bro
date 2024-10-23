from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def print_hello(request):
    movie_data={
            'movies':[
            {
            'title': 'Godfather',
            'year': 1990,
            'summary': 'story of an underworld',
            'sucess': True
        },
        {
            'title': 'Mayavi',
            'year': 2000,
            'summary':'story of dillep',
            'sucess': False
        },
        {
            'title': 'thilakkam',
            'year': 2002,
            'summary': 'story of dillep',
            'sucess': True
        }

    ]}
    return render(request,'hello.html',movie_data)
