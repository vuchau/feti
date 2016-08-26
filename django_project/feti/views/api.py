from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView

from feti.models.campus import Campus
from feti.models.course import Course
from feti.models.campus_course_entry import CampusCourseEntry
from feti.serializers.campus_serializer import CampusSerializer
from feti.serializers.course_serializer import CourseSerializer

__author__ = 'Irwan Fathurrahman <irwan@kartoza.com>'
__date__ = '08/08/16'
__license__ = "GPL"
__copyright__ = 'kartoza.com'


class ApiCampus(APIView):
    def get(self, request, format=None):
        q = request.GET.get('q')
        if not q:
            q = ""
        set = Campus.objects.filter(Q(campus__icontains=q) | Q(provider__primary_institution__icontains=q))
        serializer = CampusSerializer(set, many=True)
        return Response(serializer.data)


class ApiCourse(APIView):
    def get(self, request, format=None):
        q = request.GET.get('q')
        if not q:
            q = ""

        set = Course.objects.filter(course_description__icontains=q)
        serializer = CourseSerializer(set, many=True)
        return Response(serializer.data)
