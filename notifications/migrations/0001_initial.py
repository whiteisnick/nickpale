# Generated by Django 2.0.3 on 2018-05-28 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PushNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField()),
                ('data', models.TextField(default='{}')),
                ('headers', models.TextField(default='{}')),
            ],
        ),
    ]
