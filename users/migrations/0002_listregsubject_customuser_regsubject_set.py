# Generated by Django 4.2.6 on 2023-10-06 15:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0002_subject_remaining_class'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListRegSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='list_name', to='subjects.subject')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='list_subject', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='RegSubject_set',
            field=models.ManyToManyField(related_name='StudentReg_set', through='users.ListRegSubject', to='subjects.subject'),
        ),
    ]