# from drf_yasg.utils import swagger_auto_schema
# from drf_yasg import openapi
# from ..tables.models.service.user import User
#
# @swagger_auto_schema(security=[{"BearerAuth": []}])
# def get(self, request):
#     """
#     Get the list of all lotto numbers
#     """
#     lotto = User.objects.all()
#     serializer = User(lotto, many=True)
#     return Response(serializer.data)
