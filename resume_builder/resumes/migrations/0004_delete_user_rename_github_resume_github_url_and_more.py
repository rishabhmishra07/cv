# Generated by Django 5.1.2 on 2024-11-16 08:37

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0003_rename_last_name_user_email'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
        migrations.RenameField(
            model_name='resume',
            old_name='github',
            new_name='github_url',
        ),
        migrations.RenameField(
            model_name='resume',
            old_name='linkedin',
            new_name='linkedin_url',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='pincode',
        ),
        migrations.AddField(
            model_name='resume',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='resume',
            name='postal_code',
            field=models.CharField(default='00000', max_length=10),
        ),
        migrations.AddField(
            model_name='resume',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='resume',
            name='certifications',
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name='resume',
            name='college_marks',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d+(\\.\\d+)?$', message='Enter valid marks.')]),
        ),
        migrations.AlterField(
            model_name='resume',
            name='college_passing_year',
            field=models.CharField(max_length=4, validators=[django.core.validators.RegexValidator('^\\d{4}$', message='Enter a valid year.')]),
        ),
        migrations.AlterField(
            model_name='resume',
            name='email',
            field=models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator(message='Enter a valid email address.')]),
        ),
        migrations.AlterField(
            model_name='resume',
            name='hobbies',
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name='resume',
            name='languages',
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name='resume',
            name='phone',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('^\\+?1?\\d{9,15}$', message='Enter a valid phone number.')]),
        ),
        migrations.AlterField(
            model_name='resume',
            name='school_marks',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d+(\\.\\d+)?$', message='Enter valid marks.')]),
        ),
        migrations.AlterField(
            model_name='resume',
            name='school_passing_year',
            field=models.CharField(max_length=4, validators=[django.core.validators.RegexValidator('^\\d{4}$', message='Enter a valid year.')]),
        ),
        migrations.AlterField(
            model_name='resume',
            name='skills',
            field=models.JSONField(default=list),
        ),
    ]
