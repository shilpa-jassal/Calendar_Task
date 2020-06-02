# Generated by Django 3.0.6 on 2020-06-02 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200602_0723'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, verbose_name='User name')),
                ('email', models.CharField(max_length=100, verbose_name='User email')),
                ('password', models.CharField(max_length=200, verbose_name='User Password')),
            ],
        ),
        migrations.DeleteModel(
            name='UserProfileInfo',
        ),
    ]
