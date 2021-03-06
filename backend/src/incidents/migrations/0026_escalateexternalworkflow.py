# Generated by Django 2.2.1 on 2019-10-15 14:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('incidents', '0025_auto_20191015_1405'),
    ]

    operations = [
        migrations.CreateModel(
            name='EscalateExternalWorkflow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('is_internal_user', models.BooleanField(default=False)),
                ('comment', models.TextField()),
                ('escalated_user_other', models.CharField(blank=True, max_length=200, null=True)),
                ('escalated_entity_other', models.CharField(blank=True, max_length=200, null=True)),
                ('actioned_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='incidents_escalateexternalworkflow_related', related_query_name='incidents_escalateexternalworkflows', to=settings.AUTH_USER_MODEL)),
                ('escalated_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='escalation_related', related_query_name='escalated_users', to=settings.AUTH_USER_MODEL)),
                ('incident', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='incidents_escalateexternalworkflow_related', related_query_name='incidents_escalateexternalworkflows', to='incidents.Incident')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
