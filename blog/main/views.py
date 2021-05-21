import datetime

from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from django.urls import reverse
from django.utils import timezone

from faker import Faker

from .check_service import subscribe_check
from .forms import PostForm, CommentForm

from .notify_service import notify
from .post_service import post_find
from .subscribe_service import subscribe


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def posts(request):
    posts = Post.objects.all()
    return render(request, 'main/posts.html', {"title": "Posts", "posts": posts})


def authors(request):
    authors = Author.objects.all()
    context = {
        "title": 'Authors',
        "authors": authors,
    }
    return render(request, 'main/authors.html', context)


def categories(request):
    categories = Category.objects.all()
    context = {
        "title": 'Categories',
        "categories": categories,
    }
    return render(request, 'main/categories.html', context)


def authors_generate(request):
    faker = Faker()
    Author(name=faker.name(), email=faker.email()).save()
    return HttpResponseRedirect(reverse('authors'))


def posts_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        form.save()
    else:
        form = PostForm()

    context = {
        'form': form,
    }
    return render(request, 'main/create.html', context=context)


def api_posts(request):
    posts = Post.objects.all()
    all = [dict(title=post.title) for post in posts]
    return JsonResponse(all, safe=False)


def subs(request):
    subs = Subscriber.objects.all()
    return render(request, 'main/subs.html', {"title": "Subscribers", "Dianna": subs})


def subscription(request):
    err = "You are successfully subscribed"
    context = subscribe_check(err, request)

    return render(request, 'main/subscribe.html', context=context)


def api_subscribe(request):
    author_id = request.GET["author_id"]
    email_to = request.GET["email_to"]
    get_object_or_404(author_id, email_to)

    subscribe(author_id, email_to)
    notify(email_to)
    data = {"email_to": email_to}
    return JsonResponse(data, safe=False)


def api_authors_new(request):
    faker = Faker()
    Author(name=faker.name(), email=faker.email()).save()
    all = Author.objects.all().values('name', 'email')
    return JsonResponse(list(all), safe=False)


def api_authors_all(request):
    all = Author.objects.all().values('id', 'name', 'email')
    return JsonResponse(list(all), safe=False)


def api_subscribers_all(request):
    all = Author.objects.all().values('name', 'email')
    return JsonResponse(list(all), safe=False)


def post_update(request, post_id):
    err = ""
    pst = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = PostForm(instance=pst, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts')
        else:
            err = "Error on update Post"
    else:
        form = PostForm(instance=pst)
    context = {
        'form': form,
        'err': err
    }
    return render(request, 'main/post_update.html', context=context)


def post_show(request, post_id):
    contents = Comment.objects.all()
    pst = post_find(post_id)
    if request.method == 'POST':
        cmform = CommentForm(request.POST)
        if cmform.is_valid():
            cmform.save()
    else:
        cmform = CommentForm()

    context = {
        'pst': pst,
        'contents': contents,
        'cmform': cmform
    }
    return render(request, 'main/post_show.html', context=context)


def book_all(request):
    books = Book.objects.all()
    context = {
        'title': 'Books',
        'books': books,
    }
    return render(request, 'main/books.html', context=context)


def post_show_api(request, post_id):
    pst = post_find(post_id)
    data = {"post_id": pst}
    return JsonResponse(data, safe=False)


def slow(request):
    print('----------Start')
    print('----------End')
    return JsonResponse(dict([("dd", 123)]), safe=False)


class Posts_isView(ListView):
    queryset = Post.objects.all()

