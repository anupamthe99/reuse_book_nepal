# Generated by Django 4.0.4 on 2022-08-16 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0020_ask_question_id_ask'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply_ask',
            name='id_reply',
            field=models.CharField(default='hoka', max_length=100),
            preserve_default=False,
        ),
    ]
