from django.urls import path, include
from django.contrib import admin
# from rest_framework import permissions

from rest_framework.authtoken import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Lotto 사이트 API",
        default_version='v1',
        description="계정을 등록해두면 로또를 자동으로 구매해주는 사이트 API 입니다.",
    ),
    public=True,
)

urlpatterns = [
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('api-token-auth/', views.obtain_auth_token),  # 토큰 인증 뷰 추가
]