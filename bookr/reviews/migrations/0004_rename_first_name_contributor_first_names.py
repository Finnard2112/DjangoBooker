# Generated by Django 4.0.1 on 2022-03-06 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_book_contributor_review_bookcontributor_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contributor',
            old_name='first_name',
            new_name='first_names',
        ),
    ]
