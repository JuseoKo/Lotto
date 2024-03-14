from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=255, null=False, unique=True, verbose_name="본인인증용 email")
    name = models.CharField(max_length=255, null=False, verbose_name="로그인 아이디")
    password = models.CharField(max_length=100, null=False, verbose_name="비밀번호")
    phone = models.CharField(max_length=11, null=False, verbose_name="phone 번호")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['email', 'name'], name='unique_email')
        ]
        indexes = [
            models.Index(fields=['name', 'password'], name='name_password_index')
        ]
        db_table = 'user'