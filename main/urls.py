from django.conf.urls import url, include
from rest_framework import routers
from main import api

router = routers.DefaultRouter()
router.register(r'subcategory_json', api.SubcategoryViewSet)
router.register(r'executor_json', api.ExecutorViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^api/', include(router.urls)),
]
