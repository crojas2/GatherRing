# Generated by Django 4.2.4 on 2023-08-23 05:50

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover_photo', models.ImageField(blank=True, upload_to='event_cover_photos/')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField(max_length=500)),
                ('visibility', models.CharField(choices=[('Public', 'Public'), ('Memebers Only', 'Members Only')], default='Public', max_length=20)),
                ('join_mode', models.CharField(choices=[('Direct', 'Direct'), ('Request', 'Request'), ('Invite', 'Invite')], default='Direct', max_length=10)),
                ('status', models.CharField(choices=[('Canceled', 'Canceled'), ('Active', 'Active')], default='Active', max_length=10)),
                ('capacity', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1000)])),
                ('location', models.CharField(max_length=64)),
                ('location_lat', models.FloatField(blank=True, null=True)),
                ('location_lng', models.FloatField(blank=True, null=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('attendees', models.ManyToManyField(blank=True, related_name='attending_events', to=settings.AUTH_USER_MODEL)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_events', to=settings.AUTH_USER_MODEL)),
                ('hosts', models.ManyToManyField(related_name='hosting_events', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GroupEvent',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='event.event')),
            ],
            bases=('event.event',),
        ),
        migrations.CreateModel(
            name='EventRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='event.event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_requests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]