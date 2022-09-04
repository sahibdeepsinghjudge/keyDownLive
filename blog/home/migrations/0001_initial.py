# Generated by Django 3.0.4 on 2022-02-03 08:01

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='blog_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.TextField(max_length=255)),
                ('blog_brief', models.TextField(max_length=255)),
                ('slug', models.SlugField(null=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('blog_clicks', models.IntegerField(default=0)),
                ('link_chain', models.TextField()),
                ('blog_creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('blod_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.blog_Details')),
            ],
        ),
    ]
