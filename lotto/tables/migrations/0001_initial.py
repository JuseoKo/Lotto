# Generated by Django 4.2 on 2024-03-15 14:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_id', models.CharField(max_length=30, unique=True, verbose_name='아이디')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email')),
                ('nickname', models.CharField(max_length=255, unique=True, verbose_name='닉네임')),
                ('phone_number', models.CharField(max_length=11, null=True, verbose_name='전화 번호')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='LottoAccount',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('lotto_id', models.CharField(max_length=255, verbose_name='로또 아이디')),
                ('lotto_password', models.CharField(max_length=255, verbose_name='로또 비밀번호')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_id', models.OneToOneField(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'lotto_account',
            },
        ),
    ]
