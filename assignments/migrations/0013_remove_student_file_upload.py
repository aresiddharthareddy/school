# Generated by Django 5.1.6 on 2025-02-25 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0012_remove_scores_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='file_upload',
        ),
    ]
