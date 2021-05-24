from django.urls import path
from django.views.decorators import cache

from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('about', views.about, name='about'),
    path('posts', views.posts, name='posts'),
    path('subs', views.subs, name='subs'),
    path('posts/create', views.posts_create, name='posts_create'),
    path('post/<int:post_id>', views.post_show, name='post_show'),
    path('post/update/<int:post_id>', views.post_update, name='post_update'),
    path('subscription', views.subscription, name='subscription'),
    path('authors', views.authors, name='authors'),
    path('categories', views.categories, name='categories'),
    path('authors/generate', views.authors_generate, name='authors_generate'),
    path('api/posts', views.api_posts, name='api_posts'),
    path('api/subscribe', views.api_subscribe, name='api_subscribe'),
    path('api/authors/new', views.api_authors_new, name='api_authors_new'),
    path('api/authors/all', views.api_authors_all, name='api_authors_all'),
    path('books/all', views.book_all, name='books_all'),
    path('api/subscribers/all', views.api_subscribers_all, name='api_subscribers_all'),
    path('api/post/<int:post_id>', views.post_show_api, name='post_show_api'),
    path('slow', views.slow, name='slow'),
    path('posts/list', views.Posts_isView.as_view(), name='list'),
    path('contact-us/create/', views.ContactUs_View.as_view(), name='contact_us_create'),
]
