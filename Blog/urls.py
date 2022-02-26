from django.urls import path, include
from .views import BlogViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# 첫번째 인자는 url 의 prefix 값
# 두번째 인자는 ViewSet 을 넣어 주면 된다.
router.register('blog',BlogViewSet)

urlpatterns = [
    path('',include(router.urls))
]