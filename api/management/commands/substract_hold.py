from django.core.management.base import BaseCommand
from api.models import BankAccount


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            accounts = BankAccount.objects.all()
            for account in accounts:
                current_balance = account.current_balance - account.hold
                account.update(current_balance=current_balance, hold=0)
        except Exception as e:
            pass
