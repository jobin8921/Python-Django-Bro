from django.shortcuts import render
from . models import MovieInfo
from . forms import MovieForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def create(request):
    frm=MovieForm()
    if request.POST:
        frm=MovieForm(request.POST,request.FILES)
        if frm.is_valid:
            frm.save()
        # title=(request.POST.get('title'))
        # year=(request.POST.get('year'))
        # desc=(request.POST.get('description'))
        # movie_obj=MovieInfo(title=title,year=year,description=desc)
        # movie_obj.save()
        else:
            frm=MovieForm()

        
    return render(request,'create.html',{'frm':frm})

@login_required(login_url='login/')
def list(request):
    print(request.COOKIES)
    # visits=int(request.COOKIES.get('visits',0))
    visits = request.COOKIES.get('visits', '0')

    try:
        visits = int(visits)  
    except ValueError:
        visits = 0 


    visits=visits+1
    movie_set=MovieInfo.objects.all()
    print(movie_set)
    response=render(request,'list.html',{'movies':movie_set, 'visits':visits })
    response.set_cookie('visits',visits)
    return response
@login_required(login_url='login/')

def edit(request,pk):
    instance_to_be_edited=MovieInfo.objects.get(pk=pk)
    if request.POST:
        frm=MovieForm(request.POST,instance=instance_to_be_edited)
        # title=request.POST.get('title')
        # year=request.POST.get('year')
        # description=request.POST.get('description')
        # instance_to_be_edited.title=title
        # instance_to_be_edited.year=year
        # instance_to_be_edited.description=description
        # instance_to_be_edited.save()
        if frm.is_valid():
            instance_to_be_edited.save()

    else:
        frm=MovieForm(instance=instance_to_be_edited)    

    return render(request,'create.html',{'frm':frm})
@login_required(login_url='login/')

def delete(request,pk):
    instance=MovieInfo.objects.get(pk=pk)
    instance.delete()
    movie_set=MovieInfo.objects.all()
    print(movie_set)
    return render(request,'list.html',{'movies':movie_set})