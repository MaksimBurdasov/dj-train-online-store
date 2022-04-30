from django.db import models

class Product(models.Model):

    title = models.CharField("Название товара/услуги", max_length=50)
    description = models.TextField("Описание")
    price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        """ Изменение этого магического метода даёт нам возможность увидеть поля
        title, price и description при печати на экран объекта Product (таблица). """
        return "{}; {}; {}".format(self.title, self.price, self.description)


    class Meta:
        """ Переименование объекта и таблицы при выводе в учётке admin. """
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
