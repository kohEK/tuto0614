from rest_framework.routers import DefaultRouter, SimpleRouter

from cards import views
from cards.views import UserViewSet, CardViewSet

router = SimpleRouter()

router.register(r'users',views.UserViewSet)
router.register(r'users/<int:pk>',views.UserViewSet)
router.register(r'cards', views.CardViewSet)

urlpatterns = router.urls
