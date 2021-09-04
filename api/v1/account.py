from rest_framework.views import APIView
from api.models import BankAccount
from api.helpers.api_response import ApiResponse


class AccountPingApi(APIView):
    def get(self, request):
        try:
            response = BankAccount.objects.all()
            return ApiResponse.responseSuccess(data=response)
        except Exception as e:
            return ApiResponse.responseError(message=str(e))


class AccountAddApi(APIView):
    def post(self, request):
        data = None
        try:
            data = request.data
            added_money = data['money']
            uuid = data['uuid']
            account: BankAccount = BankAccount.objects.get(uuid=str(uuid))
            account.current_balance += int(added_money)
            account.save()
            return ApiResponse.responseSuccess(data=data)
        except Exception as e:
            return ApiResponse.responseError(message=str(e), data=data)


class AccountStatusApi(APIView):
    def get(self, request, uuid):
        try:
            account: BankAccount = BankAccount.objects.get(uuid=str(uuid))
            if account.account_status is True:
                status = 'Открыт'
            else:
                status = 'Закрыт'
            return ApiResponse.responseSuccess(data=status)
        except Exception as e:
            return ApiResponse.responseError(message=str(e))


class AccountSubstractBalanceApi(APIView):
    def post(self, request):
        try:
            data = request.data
            money = data['money']
            uuid = data['uuid']
            account: BankAccount = BankAccount.objects.get(uuid=str(uuid))
            if self.check_if_possible(account, money):
                account.current_balance -= money
                account.hold += money
                account.save()
                return ApiResponse.responseSuccess(data=data)
            else:
                return ApiResponse.responseError(data=data, message=f'You dont have enough money to substract, '
                                                                    f'account: {account}')
        except Exception as e:
            return ApiResponse.responseError(message=str(e))

    @staticmethod
    def check_if_possible(account, money):
        result = account.current_balance - account.hold - money
        if result < 0:
            return False
        else:
            return True
