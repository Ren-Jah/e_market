from django.contrib import admin
from django.contrib.auth.models import Group
from django.urls import reverse
from django.utils.safestring import mark_safe

from nexus.models import ProductInfo, Element


@admin.action(description='Очистить задолженность перед поставщиком у выбранных объектов')
def write_off_debt(modeladmin, request, queryset):
    queryset.update(debt=0)


class ElementAdmin(admin.ModelAdmin):
    list_display = ("title", "email", "country", "street", "house_number", "products", "supplier", "debt", "created")
    search_fields = ("city",)
    actions = [write_off_debt]

    def supplier_display(self, obj):
        url = reverse('admin:id_supplier_change', args=[obj.id])
        return mark_safe("<a href={0}>{1}</a>".format(url, obj.supplier))


admin.site.register(Element, ElementAdmin)
admin.site.register(ProductInfo)

admin.site.unregister(Group)
