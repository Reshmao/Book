# Generated by Django 4.1.1 on 2023-12-01 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0006_book_luminar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.PositiveIntegerField()),
                ('course', models.CharField(max_length=30)),
                ('place', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
    ]
