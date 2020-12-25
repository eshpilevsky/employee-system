from django.contrib import admin
from django.urls import path

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from employee.views import EmployeesList, BranchesList

schema_view = get_schema_view(
    openapi.Info(
        title="Employee management API",
        default_version='v1',
        contact=openapi.Contact(email="eshpilevsky@icloud.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r'^api/swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("api/employees/", EmployeesList.as_view()),
    path("api/branches/", BranchesList.as_view()),
]
