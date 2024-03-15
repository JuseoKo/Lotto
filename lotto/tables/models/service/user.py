from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
import random
import string

class UserManager(BaseUserManager):
    def create_user(self, user_id, email, phone_number, nickname, password=None):
        if not user_id:
            raise ValueError('must have user email')
        if not email:
            raise ValueError('must have user email')
        user = self.model(
            user_id=user_id,
            email=self.normalize_email(email),
            nickname=nickname,
            phone_number=phone_number
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, email, nickname, phone_number, password):
        user = self.create_user(
            user_id=user_id,
            email=self.normalize_email(email),
            nickname=nickname,
            phone_number=phone_number,
            password=password
        )
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    user_id = models.CharField(max_length=30, null=False, unique=True, verbose_name="아이디")
    email = models.EmailField(max_length=255, null=False, unique=True, verbose_name="email")
    nickname = models.CharField(max_length=255, null=False, unique=True, verbose_name="닉네임")
    phone_number = models.CharField(max_length=11, null=True, verbose_name="전화 번호")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['email', 'phone_number', 'nickname']
    objects = UserManager()

    class Meta:
        db_table = 'users'

    def save(self, *args, **kwargs):
        if not self.nickname:
            self.nickname = self.generate_random_nickname()
        super().save(*args, **kwargs)

    def generate_random_nickname(self):
        """
        랜덤 닉네임을 생성하는 함수입니다.
        :return:
        """
        return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

    def __str__(self):
        return self.name