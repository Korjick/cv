# Generated by Django 4.2.4 on 2023-08-16 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_education_alter_experience_company_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='education/'),
        ),
        migrations.AddField(
            model_name='education',
            name='institution_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
