# Generated by Django 4.1 on 2022-08-16 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, verbose_name='Name of News')),
                ('content', models.TextField(verbose_name='Main News')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('draft', models.BooleanField(default=True, verbose_name='Should be post?')),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'More News',
            },
        ),
    ]
