# Generated by Django 2.1.4 on 2019-05-11 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatBot', '0002_reply_wordsregex'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reply',
            options={'verbose_name': 'Regex Respuesta', 'verbose_name_plural': 'Regexs Respuestas'},
        ),
        migrations.AlterModelOptions(
            name='wordsregex',
            options={'verbose_name': 'Palabra', 'verbose_name_plural': 'Palabras'},
        ),
        migrations.AlterField(
            model_name='reply',
            name='replyRegex',
            field=models.TextField(primary_key=True, serialize=False, verbose_name='Expresion regular de la respuesta'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='replyText',
            field=models.TextField(verbose_name='Texto de la respuesta'),
        ),
    ]