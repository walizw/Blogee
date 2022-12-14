# Generated by Django 4.1.2 on 2022-10-06 18:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('author', models.DecimalField(decimal_places=0, max_digits=10)),
                ('blog', models.DecimalField(decimal_places=0, max_digits=10)),
                ('content', models.TextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('thumbnail', models.FileField(blank=True, null=True, upload_to='thumbs/')),
                ('tags', models.TextField(blank=True, null=True)),
                ('category', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('views', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('likes', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('comments', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('featured', models.BooleanField(blank=True, default=False)),
            ],
        ),
    ]
