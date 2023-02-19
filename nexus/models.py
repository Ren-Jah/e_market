from django.db import models


# class ContactInfo(models.Model):
#     """
#     Модель класса  ContactInfo
#     ------
#     email : str
#     country : str
#     country : str
#     street : str
#     house_number : int
#     """
#     class Meta:
#         verbose_name = "Контакты"
#         verbose_name_plural = "Контакты"
#
#     email = models.EmailField(max_length=254)
#     country = models.CharField(verbose_name="Страна", max_length=50)
#     city = models.CharField(verbose_name="Город", max_length=50)
#     street = models.TextField(verbose_name="Улица", null=True, blank=True, default=None)
#     house_number = models.PositiveSmallIntegerField(verbose_name="Номер дома")


class ProductInfo(models.Model):
    """
    Модель класса  ProductInfo
    ------
    title : str
    model : str
    launch_date : int
    """
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    title = models.CharField(verbose_name="Название", max_length=255)
    model = models.CharField(verbose_name="Модель", max_length=255)
    launch_date = models.DateTimeField(verbose_name="Дата выхода продукта на рынок")


class Element(models.Model):
    """
       Модель класса  Element
       ------
       title : str
       email : str
       country : str
       street : str
       house_number : int
       products : int
       supplier : int
       debt : int
       created : str
       """

    class Meta:
        verbose_name = "Звено"
        verbose_name_plural = "Звенья"

    class Supplier(models.IntegerChoices):
        """ Класс для определения иерархической зависимости """
        base = 0, "Начальный"
        first = 1, "1 уровень"
        second = 2, "2 уровень"
        third = 3, "3 уровень"
        fourth = 4, "4 уровень"

    title = models.CharField(verbose_name="Название", max_length=255)
    email = models.EmailField(max_length=254)
    country = models.CharField(verbose_name="Страна", max_length=50)
    city = models.CharField(verbose_name="Город", max_length=50)
    street = models.TextField(verbose_name="Улица", null=True, blank=True, default=None)
    house_number = models.PositiveSmallIntegerField(verbose_name="Номер дома")
    products = models.ForeignKey(ProductInfo, verbose_name="Продукты", on_delete=models.PROTECT)
    supplier = models.PositiveSmallIntegerField(verbose_name="Поставщик", choices=Supplier.choices)
    debt = models.DecimalField(verbose_name="Задолженность", max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")


