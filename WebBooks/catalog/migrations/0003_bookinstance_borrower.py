# Generated by Django 4.1.4 on 2022-12-16 14:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0002_alter_book_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinstance',
            name='borrower',
            field=models.ForeignKey(blank=True, help_text='Выберите заказчика книги', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Заказчик'),
        ),
    ]
