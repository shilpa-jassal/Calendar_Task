# Generated by Django 3.0.6 on 2020-05-31 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0002_auto_20200531_1444'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=256)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Task1',
        ),
    ]
