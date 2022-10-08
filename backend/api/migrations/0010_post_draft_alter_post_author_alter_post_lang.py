# Generated by Django 4.1.2 on 2022-10-08 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_blog_icon_alter_category_blog_alter_category_lang'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.DecimalField(decimal_places=0, default=-1, max_digits=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='lang',
            field=models.CharField(default='en', max_length=12),
        ),
    ]
