# Generated by Django 4.2.7 on 2024-02-15 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_event_image_alter_event_unique_together'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a category name (e.g. Music, Sports, Food etc.)', max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organiser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_name', models.CharField(max_length=100)),
                ('org_description', models.TextField(blank=True, null=True)),
                ('org_contact_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('org_website', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='event',
            name='organizer',
        ),
        migrations.AddField(
            model_name='event',
            name='organiser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.organiser'),
        ),
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.category'),
        ),
    ]