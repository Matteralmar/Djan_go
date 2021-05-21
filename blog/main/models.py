
from django.db import models

# Create your models here.


class Author(models.Model):

    class Meta:
        db_table = 'tbl_user'
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
    name = models.CharField("Author's name", max_length=100)
    email = models.CharField("Author's email", max_length=50)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Subscriber(models.Model):
    email_to = models.EmailField("Subscriber's email")
    author_id = models.ForeignKey("Author", on_delete=models.CASCADE)

    def __str__(self):
        return self.email_to


class Comment(models.Model):
    comment = models.CharField("Subscriber's comment", max_length=150)
    post_id = models.ForeignKey("Post", on_delete=models.CASCADE)


class Post(models.Model):
    class Meta:
        db_table = 'tbl_posts'
        verbose_name = "User's post"
        verbose_name_plural = "User's posts"
    title = models.CharField("User's name", max_length=40)
    description = models.CharField("User's email", max_length=60)
    comments = models.CharField("User's comment", max_length=150, default="")
    content = models.TextField("User's text")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Logg(models.Model):
    utm = models.CharField("Utm logger", max_length=40, default="")
    created = models.DateTimeField(auto_now_add=True)
    time_execution = models.CharField("Time execution", max_length=40, default="")
    path = models.CharField("Path", max_length=40, default="")
    user_ip = models.CharField("IP", max_length=40)


class Category(models.Model):
    name = models.CharField("Name", max_length=100, null=True, blank=True)


class Book(models.Model):
    title = models.CharField("Name", max_length=250)
    author = models.ForeignKey(Author, models.CASCADE)
    category = models.ForeignKey(Category, models.CASCADE)


