from django.db import transaction
from rest_framework import serializers

from nexus.models import ProductInfo, Element


# ContactInfo Serializers
# class ContactInfoCreateSerializer(serializers.ModelSerializer):
#     """ Сериализатор для создания элемента цепи """
#
#     class Meta:
#         model = ContactInfo
#         fields = "__all__"
#
#
# class ContactInfoSerializer(serializers.ModelSerializer):
#     """ Сериализатор для контактной информации  """
#     class Meta:
#         model = ContactInfo
#         fields = "__all__"


# ProductInfo Serializers
class ProductInfoCreateSerializer(serializers.ModelSerializer):
    """ Сериализатор для создания элемента цепи """

    class Meta:
        model = ProductInfo
        fields = "__all__"


class ProductInfoSerializer(serializers.ModelSerializer):
    """ Сериализатор для информации по продуктам """
    class Meta:
        model = ProductInfo
        fields = "__all__"


# Element
class ElementCreateSerializer(serializers.ModelSerializer):
    """ Сериализатор для создания элемента цепи """

    class Meta:
        model = Element
        fields = "__all__"


class ElementSerializer(serializers.ModelSerializer):
    """ Сериализатор элемента цепи """

    class Meta:
        model = Element
        read_only_fields = ("id", "debt", "created")
        fields = "__all__"
