# Generated by Django 4.1 on 2022-08-18 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_news_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='categories',
            field=models.ManyToManyField(null=True, related_name='category_blog', to='blog.category'),
        ),
    ]