# Generated by Django 5.1.6 on 2025-02-19 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0010_scores_file_upload_scores_teacher_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scores',
            name='file_upload',
            field=models.FileField(blank=True, null=True, upload_to='students_assignment/'),
        ),
    ]
