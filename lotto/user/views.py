from tables.models.service.user import User
from tables.models.service.lotto_user import LottoAccount
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from .serializers import UserSerializer, LottoAccountSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.decorators import action


class UserViewSet(viewsets.ViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects

    @swagger_auto_schema(tags=['User'], operation_description="모든 유저 목록을 반환하는 API 입니다.")
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(tags=['User'], operation_description="특정 유저의 정보를 반환하는 API 입니다.")
    @action(detail=False, methods=['get'], url_path='(?P<user_id>[^/.]+)')
    def check_user_nickname(self, request, nickname=None):
        queryset = User.objects.filter(user_id=nickname)
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)



class LottoAccountViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = LottoAccount.objects.all().order_by('-user_id')
    serializer_class = LottoAccountSerializer
    # permission_classes = [permissions.IsAuthenticated]