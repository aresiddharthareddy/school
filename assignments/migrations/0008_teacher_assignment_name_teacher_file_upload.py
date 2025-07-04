# Generated by Django 5.1.6 on 2025-02-18 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0007_alter_assignment_file_upload'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='assignment_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='file_upload',
            field=models.FileField(blank=True, null=True, upload_to='teacher_assignment/'),
        ),
    ]
