# Generated by Django 4.2.2 on 2023-06-17 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testdb', '0002_user_delete_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eggs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eggtype', models.TextField()),
                ('color', models.TextField()),
                ('size', models.IntegerField()),
                ('weight', models.IntegerField()),
            ],
        ),
    ]
