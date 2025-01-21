# Generated by Django 5.1.5 on 2025-01-21 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "students",
            "0002_remove_student_address_remove_student_date_of_birth_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="attendance",
            old_name="date_attended",
            new_name="last_date_attended",
        ),
        migrations.RemoveField(
            model_name="attendance",
            name="hours",
        ),
        migrations.AddField(
            model_name="attendance",
            name="total_days",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
