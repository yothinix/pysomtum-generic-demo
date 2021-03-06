# Generated by Django 2.2.3 on 2019-07-09 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256)),
                ('last_name', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=256)),
                ('phone', models.CharField(max_length=256)),
                ('prefered_contact_method', models.CharField(choices=[('phone', 'Via Phone'), ('email', 'Via Email')], max_length=256)),
                ('message', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
