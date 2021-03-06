from rest_framework import viewsets
from . import Serializer
from . import models
from rest_framework.decorators import action
from django.http import HttpResponse
from django.core import serializers


class UsersViewSet(viewsets.ModelViewSet):
    queryset = models.Users.objects.all()
    serializer_class = Serializer.UserSerializer
class CoursesViewSet(viewsets.ModelViewSet):
    queryset = models.Courses.objects.all()
    serializer_class = Serializer.CourseSerializer
class Match_ExampleViewSet(viewsets.ModelViewSet):
    queryset = models.Match_Example.objects.all()
    serializer_class = Serializer.MatchWordsSerializer

    #at request body parameter number means the slice of the results if any given
    #coressponds to select * from x order by x.user_id asc limit params[number];

    @action(methods=['get'], detail=False)
    def top_ten_grade_user(self, request, *args):
        print(args)
        top_10 = self.get_queryset().order_by('age').filter(user_id__gt=request.query_params['number'])
        data = serializers.serialize('json', top_10)
        return HttpResponse(data, content_type='application/json')

