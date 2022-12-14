# Generated by Django 4.0.5 on 2022-07-11 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=1000)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('image', models.TextField(max_length=2000)),
                ('desc', models.TextField(max_length=5000)),
                ('trend', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Series_Part',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField(max_length=1000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('title', models.TextField(max_length=500, null=True)),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='for_series', to='app.series')),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('des', models.TextField(max_length=5000, null=True)),
                ('image', models.TextField(max_length=5000, null=True)),
                ('url', models.TextField(max_length=1000, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('trend', models.BooleanField(default=False)),
                ('kind', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='film_category', to='app.category')),
            ],
        ),
    ]
