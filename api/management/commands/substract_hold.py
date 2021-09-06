from django.core.management.base import BaseCommand

from api.models import BankAccount


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            accounts = BankAccount.objects.all()
            for account in accounts:
                account.current_balance -= account.hold
                account.hold = 0
            BankAccount.objects.bulk_update(accounts, ['current_balance', 'hold'])
        except Exception as e:
            pass
