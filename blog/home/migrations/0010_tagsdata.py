# Generated by Django 3.0.4 on 2022-09-03 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20220903_1755'),
    ]

    operations = [
        migrations.CreateModel(
            name='tagsData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_text', models.CharField(max_length=50)),
                ('tag_uses', models.IntegerField(default=1)),
            ],
        ),
    ]
