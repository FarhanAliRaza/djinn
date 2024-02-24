from .views.task import TaskViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"tasks", TaskViewSet, "tasks_viewset")
urlpatterns = router.urls