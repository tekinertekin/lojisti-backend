# Generated by Django 4.2.4 on 2023-09-02 13:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('util', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('CREATED', 'CREATED'), ('PENDING', 'PENDING'), ('ACTIVE', 'ACTIVE'), ('ACCEPTED', 'ACCEPTED'), ('CANCELLED', 'CANCELLED')], default='CREATED', max_length=30)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_createdby', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_modifiedby', to=settings.AUTH_USER_MODEL)),
                ('new_home', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='location_publication_new_home', to='util.location')),
                ('old_home', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='location_publication_old_home', to='util.location')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
