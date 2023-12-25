# Generated by Django 4.0 on 2023-12-12 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_news_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50, verbose_name='email')),
                ('username', models.CharField(max_length=20, verbose_name='логин')),
                ('comment', models.TextField(verbose_name='комментарий')),
                ('published_at', models.DateTimeField(auto_now_add=True, verbose_name='дата публикации')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.news', verbose_name='новость')),
            ],
            options={
                'verbose_name': 'комментарий',
                'verbose_name_plural': 'комментарии',
                'db_table': 'comments',
            },
        ),
    ]
