from django.db import models

class LottoAccount(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.OneToOneField('User', on_delete=models.CASCADE, db_column='user_id')
    lotto_id = models.CharField(max_length=255, null=False, verbose_name="로또 아이디")
    lotto_password = models.CharField(max_length=255, null=False, verbose_name="로또 비밀번호")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'lotto_account'