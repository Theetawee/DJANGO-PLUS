from dj_waanverse_auth.base_account import AbstractBaseAccount
from django.db import models


class Account(AbstractBaseAccount):
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta(AbstractBaseAccount.Meta):
        db_table = "accounts_account"

    def __str__(self):
        return self.name or self.username

    def get_full_name(self):
        return self.name or self.username
