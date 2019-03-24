from django.urls import include, path
from rest_framework import routers
import classes.viewsets as classes
import serie.viewsets as serie


router = routers.DefaultRouter()
# router.register(r'users', viewsets.UserViewSet)
# router.register(r'groups', viewsets.GroupViewSet)
router.register(r'series', serie.SerieViewSet)
router.register(r'classes', classes.ClassesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
