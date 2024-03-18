from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie,Category
from .forms import MovieForm

# Create your views here.
def home(request,c_slug=None):
    c_page=None
    movies=None
    if c_slug != None:
        c_page=get_object_or_404(Category,slug=c_slug)
        movies=Movie.objects.all().filter(category=c_page)
    else:
        movies=Movie.objects.all()
    paginator = Paginator(movies, 6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        movie=paginator.page(page)
    except(EmptyPage,InvalidPage):
        movie=paginator.page(paginator.num_pages)


    return render(request,'home.html',{'category':c_page,'movies':movie})
def post_detail(request,post_id):
    movie=Movie.objects.get(id=post_id)
    return render(request,'detail.html',{'movie':movie})

def add_post(request):
    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        category = Category.objects.get(pk=category_id)

        user = request.user
        title=request.POST.get('title')
        slug = request.POST.get('slug')
        desc = request.POST.get('desc')
        image = request.FILES['image']
        release_date = request.POST.get('release_date')
        actors = request.POST.get('actors')
        youtube_link = request.POST.get('youtube_link')
        movie=Movie(title=title,slug=slug,desc=desc,image=image,release_date=release_date,actors=actors,category=category,youtube_link=youtube_link)
        movie.user = user
        movie.save()
        return redirect('/movieapp/home')
    return render(request,'add_post.html')

def my_post(request):
    movies = Movie.objects.filter(user=request.user)
    return render(request,'my_post.html',{'movies':movies})

def edit_post(request, post_id):
    post = get_object_or_404(Movie, id=post_id, user=request.user)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('movie:my_post')
    else:
        form = MovieForm(instance=post)
    return render(request, 'edit_post.html', {'form': form})

def delete_post(request, post_id):
    post = get_object_or_404(Movie, id=post_id, user=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('movie:my_post')
    return render(request, 'delete_post.html', {'post': post})