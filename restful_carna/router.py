from carna_db.viewset import CoursesViewSet, UsersViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('users', UsersViewSet)
router.register('courses', CoursesViewSet)