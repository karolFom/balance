from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from api.models import BankAccount
from api.helpers.api_response import ApiResponse
from api.serializers.serializer import BankAccountSerializer


class AccountPingApi(ListAPIView):
    serializer_class = BankAccountSerializer

    def get_queryset(self):
        return BankAccount.objects.all()

    def list(self, request, *args, **kwargs):
        try:
            res = super(AccountPingApi, self).list(request, *args, **kwargs)
            return ApiResponse.responseSuccess(data=res.data)
        except Exception as e:
            return ApiResponse.responseError(message=str(e))


class AccountAddApi(APIView):
    def post(self, request):
        data = None
        try:
            data = request.data
            added_money = data['money']
            uuid = data['uuid']
            account = BankAccount.objects.get(uuid=str(uuid))
            current_balance = account.current_balance + int(added_money)
            account.update(current_balance=current_balance)
            return ApiResponse.responseSuccess(data=data)
        except Exception as e:
            return ApiResponse.responseError(message=str(e), data=data)


class AccountStatusApi(APIView):
    def get(self, request, uuid):
        try:
            account: BankAccount = BankAccount.objects.get(uuid=str(uuid))
            status = 'Открыт' if account.account_status else status = 'Закрыт'
            data = {
                'current_balance': account.current_balance,
                'status': status
            }
            return ApiResponse.responseSuccess(data=data)
        except Exception as e:
            return ApiResponse.responseError(message=str(e))


class AccountSubstractBalanceApi(APIView):
    def post(self, request):
        try:
            data = request.data
            money = int(data['money'])
            uuid = data['uuid']
            account = BankAccount.objects.get(uuid=str(uuid))
            if self.check_if_possible(account, money):
                current_balance = account.current_balance - money
                hold = account.hold + money
                account.update(current_balance=current_balance, hold=hold)
                return ApiResponse.responseSuccess(data=data)
            else:
                return ApiResponse.responseError(data=data, message=f'You dont have enough money '
                                                                    f'to substract, account: '
                                                                    f'{account}')
        except Exception as e:
            return ApiResponse.responseError(message=str(e))

    @staticmethod
    def check_if_possible(account, money):
        result = account.current_balance - account.hold - money
        if result < 0:
            return False
        else:
            return True
