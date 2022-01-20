from django.urls import include, path
from rest_framework import routers

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.views.generic import TemplateView
from .views import marketpostViewSet, tutorpostViewSet, employeepostViewSet

router = routers.DefaultRouter()
router.register(r'marketPost', marketpostViewSet)
router.register(r'tutorPost', tutorpostViewSet)
router.register(r'employeePost', employeepostViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="API for my social network",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="anewday1999@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('openapi', schema_view.without_ui(cache_timeout=0), name='openapi-schema'),
    path('', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
    path('', include(router.urls)),
]