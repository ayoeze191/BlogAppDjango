# Generated by Django 5.2 on 2025-05-02 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blog_text_alter_blog_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='text',
            field=models.TextField(blank=True, max_length=50000, null=True),
        ),
    ]
