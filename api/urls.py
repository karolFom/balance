from django.urls import path

from api.v1.account import *

app_name = 'api'
urlpatterns = [
    path('ping/', AccountPingApi.as_view(), name='ping'),
    path('add/', AccountAddApi.as_view(), name='add_money'),
    path('substract/', AccountSubstractBalanceApi.as_view(), name='substract_money'),
    path('status/<str:uuid>', AccountStatusApi.as_view(), name='balance')

]