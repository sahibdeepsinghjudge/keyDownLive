# Generated by Django 3.0.4 on 2022-02-03 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20220203_0811'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='blod_id',
            new_name='blodg_id',
        ),
        migrations.AddField(
            model_name='blog',
            name='link_chain',
            field=models.TextField(blank=True),
        ),
    ]
