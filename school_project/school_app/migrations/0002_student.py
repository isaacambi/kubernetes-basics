# Generated by Django 3.2.7 on 2022-02-13 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('surname', models.CharField(max_length=256)),
                ('age', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('subjects', models.ManyToManyField(blank=True, related_name='students', to='school_app.Subject')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
