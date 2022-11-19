# Generated by Django 4.1.3 on 2022-11-18 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NameModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yourname', models.CharField(blank=True, max_length=200)),
                ('myname', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='mymodel',
            old_name='long',
            new_name='longmessage',
        ),
        migrations.RenameField(
            model_name='mymodel',
            old_name='short',
            new_name='shortmessage',
        ),
    ]