# Generated by Django 4.2.2 on 2023-06-17 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testdb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=80)),
                ('password', models.TextField()),
                ('role', models.CharField(max_length=80)),
            ],
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]
