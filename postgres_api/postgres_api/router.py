from rest_db.viewset import UsersViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('users', UsersViewSet)
