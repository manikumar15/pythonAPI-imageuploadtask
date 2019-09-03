# Generated by Django 2.2.4 on 2019-09-03 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=20)),
                ('image', models.ImageField(default='images/None/No-img.jpg', upload_to='images')),
                ('profile', models.FileField(default='fies/None/No-file.pdf', upload_to='files')),
                ('task', models.BooleanField(default=False)),
            ],
        ),
    ]
