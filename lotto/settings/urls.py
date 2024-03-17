from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi

# from rest_framework.authtoken import views
from drf_yasg.views import get_schema_view
from rest_framework.authtoken import views
from settings.url_router import UrlRouter

router = UrlRouter()

schema_view = get_schema_view(
    openapi.Info(
        title="Lotto 사이트 API",
        default_version="v1",
        description="계정을 등록해두면 로또를 자동으로 구매해주는 사이트 API 입니다.",
    ),
    public=True,
)
# 토큰 인증 해더
token_param = openapi.Parameter(
    "Authorization",
    openapi.IN_HEADER,
    description="Bearer Token",
    type=openapi.TYPE_STRING,
)

urlpatterns = [
    path("", include(router.urls)),
    path("auth/", views.obtain_auth_token),  # 토큰 인증 뷰 추가
    path(
        "api/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("admin/", admin.site.urls),
]
