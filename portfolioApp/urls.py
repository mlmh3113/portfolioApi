from .views import WorkViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('work', WorkViewSet)

urlpatterns = router.urls