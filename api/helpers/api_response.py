from rest_framework.response import Response


class ApiResponse:
    @staticmethod
    def responseSuccess(data=None, description=None):
        return Response({
            'status': 200,
            'result': True,
            'addition': data,
            'description': description
        })

    @staticmethod
    def responseError(message, data=None, status=502):
        return Response({
            'status': status,
            'result': False,
            'addition': data,
            'description': message
        })