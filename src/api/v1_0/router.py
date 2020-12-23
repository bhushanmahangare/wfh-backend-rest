from django.urls import (
    path,
    include
)
from rest_framework.routers import DefaultRouter
from knox.views import (
    LoginView,
    LogoutView
)

from api.v1_0.views.authentication_views import (
    # AccountAPIView,
    LoginAPIView
)

router = DefaultRouter(trailing_slash=False)
#router.register('authentication', AgentViewSet, basename='new-policy')

urlpatterns = [
    path('login', LoginAPIView.as_view()),
    # path('logout/', LogoutView.as_view()),
] + router.urls
