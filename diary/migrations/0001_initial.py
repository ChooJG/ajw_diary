# Generated by Django 5.1.3 on 2024-11-15 11:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=700)),
                ('summary', models.CharField(max_length=50)),
                ('mood', models.CharField(choices=[('happy', '기쁨'), ('sad', '슬픔'), ('angry', '화남'), ('fear', '두려움'), ('peaceful', '평온함')], max_length=10)),
                ('diary_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='DiaryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField()),
                ('diary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='diary.diary')),
            ],
        ),
    ]
