# Generated by Django 3.2.3 on 2021-05-24 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name="Author's name")),
                ('email', models.CharField(max_length=50, verbose_name="Author's email")),
                ('age', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
                'db_table': 'tbl_user',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Category name')),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=120)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Logg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('utm', models.CharField(default='', max_length=40, verbose_name='Utm logger')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('time_execution', models.CharField(default='', max_length=40, verbose_name='Time execution')),
                ('path', models.CharField(default='', max_length=40, verbose_name='Path')),
                ('user_ip', models.CharField(max_length=40, verbose_name='IP')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name="User's name")),
                ('description', models.CharField(max_length=60, verbose_name="User's email")),
                ('comments', models.CharField(default='', max_length=150, verbose_name="User's comment")),
                ('content', models.TextField(verbose_name="User's text")),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': "User's post",
                'verbose_name_plural': "User's posts",
                'db_table': 'tbl_posts',
            },
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_to', models.EmailField(max_length=254, verbose_name="Subscriber's email")),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.author')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=150, verbose_name="Subscriber's comment")),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.post')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Name')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='main.author')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='main.category')),
            ],
        ),
    ]
