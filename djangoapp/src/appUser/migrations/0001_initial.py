# Generated by Django 2.0.7 on 2020-07-16 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='appUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=36)),
                ('Email', models.EmailField(max_length=100)),
                ('Username', models.CharField(max_length=36)),
                ('Password', models.CharField(max_length=32)),
            ],
        ),
    ]
