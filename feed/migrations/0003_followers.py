# Generated by Django 4.1.5 on 2023-02-14 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_likepost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Followers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.CharField(max_length=200)),
                ('user', models.CharField(max_length=200)),
            ],
        ),
    ]
