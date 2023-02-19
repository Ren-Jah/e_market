import django_filters
from django.db import models
from django_filters import rest_framework

from nexus.models import Element


class ElementFilter(rest_framework.FilterSet):
    """ Класс для фильтрации данных по городу """
    class Meta:
        model = Element
        fields = ["city"]
