from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions, filters
from nexus.filters import ElementFilter
from nexus.models import ProductInfo, Element
from nexus.permissions import IsUserActive
from nexus.serializers import *


# ContactInfo view
# class ContactInfoCreateView(CreateAPIView):
#     """ Вьюшка для создания элемента цепи """
#     model = ContactInfo
#     serializer_class = ContactInfoCreateSerializer
#
#
# class ContactInfoListView(ListAPIView):
#     """ Вьюшка для выведения списка элементов цепи """
#     model = ContactInfo
#     serializer_class = ContactInfoSerializer
#
#     def get_queryset(self):
#         """ Метод для получения отфильрованных элементов цепи """
#         return ContactInfo.objects.all()
#
#
# class ContactInfoView(RetrieveUpdateDestroyAPIView):
#     """ Вьюшка для взаимодействия с элементом цепи """
#     queryset = ContactInfo.objects.all()
#     model = ContactInfo
#     serializer_class = ContactInfoSerializer
#     lookup_field = 'pk'
#
#     def perform_destroy(self, instance):
#         """ Метод для удаления элемента цепи """
#         instance.is_deleted = True
#         instance.save()
#         return instance


# ProductInfo View
class ProductInfoCreateView(CreateAPIView):
    """ Вьюшка для создания информации о продукте """
    model = ProductInfo
    serializer_class = ProductInfoCreateSerializer
    permission_classes = [IsUserActive]


class ProductInfoListView(ListAPIView):
    """ Вьюшка для выведения списка продуктов """
    model = ProductInfo
    serializer_class = ProductInfoSerializer
    permission_classes = [IsUserActive]

    def get_queryset(self):
        """ Метод для возврата всех продуктов """
        return ProductInfo.objects.all()


class ProductInfoView(RetrieveUpdateDestroyAPIView):
    """ Вьюшка для взаимодействия с информацией о продукте """
    queryset = ProductInfo.objects.all()
    model = ProductInfo
    serializer_class = ProductInfoSerializer
    permission_classes = [IsUserActive]
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        """ Метод для удаления информации о продукте """
        instance.is_deleted = True
        instance.save()
        return instance


# Element View
class ElementCreateView(CreateAPIView):
    """ Вьюшка для создания элемента цепи """
    model = Element
    serializer_class = ElementCreateSerializer
    permission_classes = [IsUserActive]


class ElementListView(ListAPIView):
    """ Вьюшка для выведения списка элементов цепи """
    model = Element
    serializer_class = ElementSerializer
    permission_classes = [IsUserActive]
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_class = ElementFilter
    search_fields = ['city', 'country']

    def get_queryset(self):
        """ Метод для получения отфильрованных элементов цепи """
        return Element.objects.all()


class ElementView(RetrieveUpdateDestroyAPIView):
    """ Вьюшка для взаимодействия с элементом цепи """
    queryset = Element.objects.all()
    model = Element
    serializer_class = ElementSerializer
    permission_classes = [IsUserActive]
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        """ Метод для удаления элемента цепи """
        instance.is_deleted = True
        instance.save()
        return instance

