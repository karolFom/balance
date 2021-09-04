from django.db import models
from django.utils.translation import ugettext_lazy as _


class BankAccount(models.Model):
    uuid = models.CharField(_('UUID'), max_length=250, unique=True, null=False, blank=False)
    full_name = models.CharField(_('ФИО'), max_length=250, null=False, blank=False)
    current_balance = models.IntegerField(_('Текущий баланс'), null=True, blank=True)
    hold = models.IntegerField(_('Резерв'), null=True, blank=True)
    account_status = models.BooleanField(_('Статус счета'), default=True)

    class Meta:
        db_table = 'bank_accounts'
        verbose_name = _('Счет абонента')
        verbose_name_plural = _('Счета абонентов')

    def __str__(self):
        return self.uuid
