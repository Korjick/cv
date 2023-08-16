# Generated by Django 4.2.4 on 2023-08-16 15:46

from django.db import migrations, models
import landing.models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0003_education_image_education_institution_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('institution', models.TextField()),
                ('institution_url', models.URLField(blank=True, null=True)),
                ('image', models.ImageField(null=True, upload_to=landing.models.PathAndRename('course/'))),
                ('started', models.DateField()),
                ('ended', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HardSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('level', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Proud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('image', models.ImageField(null=True, upload_to=landing.models.PathAndRename('course/'))),
            ],
        ),
        migrations.CreateModel(
            name='Referee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('job_title', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SoftSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='education',
            name='image',
            field=models.ImageField(null=True, upload_to=landing.models.PathAndRename('education/')),
        ),
    ]
