# Generated by Django 3.0.4 on 2022-09-04 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_postlikes'),
    ]

    operations = [
        migrations.AddField(
            model_name='postlikes',
            name='status',
            field=models.CharField(choices=[('like', 'like'), ('unlike', 'unlike')], default='unlike', max_length=20),
        ),
    ]
