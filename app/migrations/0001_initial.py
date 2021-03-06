# Generated by Django 3.2 on 2021-05-01 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_id', models.IntegerField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('number', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('password', models.TextField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('measurement', models.TextField(blank=True, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('sum', models.FloatField(blank=True, null=True)),
                ('document', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.document')),
            ],
        ),
        migrations.AddField(
            model_name='document',
            name='from_whom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='from_whom', to='app.organization'),
        ),
        migrations.AddField(
            model_name='document',
            name='to_whom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='to_whom', to='app.organization'),
        ),
    ]
