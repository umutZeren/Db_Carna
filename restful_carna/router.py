from carna_db.viewset import CoursesViewSet, UsersViewSet,Match_ExampleViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('users', UsersViewSet)
router.register('courses', CoursesViewSet)
router.register('match_words_exp',Match_ExampleViewSet)