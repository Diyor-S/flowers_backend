from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from common.utils import validate_phone_number


class Category(models.Model):
    title = models.CharField(max_length=120, verbose_name=_("category title"))
    image = models.ForeignKey("common.Media",on_delete=models.CASCADE, verbose_name=_("category image"))

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    title = models.CharField(max_length=120, verbose_name=_("subcategory title"))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_("category"),
                                 related_name="subcategories")

    class Meta:
        verbose_name = _("Sub Category")
        verbose_name_plural = _("Sub Categories")

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=120, verbose_name=_("product title"))
    image = models.ForeignKey("common.Media", on_delete=models.CASCADE, verbose_name=_("product image"))
    special_offers = models.CharField(max_length=100, verbose_name=_("special offers"))
    occasion = models.CharField(max_length=100, verbose_name=_("occasion"))
    for_whom = models.CharField(max_length=200, verbose_name=_("for whom"))
    description = models.TextField(verbose_name=_("description"))
    status = models.BooleanField(default=True, verbose_name=_("status"))
    quantity = models.IntegerField(verbose_name=_("quantity"), default=1)
    price = models.IntegerField(verbose_name=_("price"))
    old_price = models.IntegerField(verbose_name=_("old price"))
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name=_("subcategory"),
                                     related_name="products")

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.title

    def get_discount(self):
        discount = (((self.old_price - self.price) / self.old_price) * 100)
        return int(discount)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("product"),
                                related_name="product_images")
    images = models.ForeignKey("common.Media", on_delete=models.CASCADE, verbose_name=_("product images"))

    class Meta:
        verbose_name = _("Product Images")
        verbose_name_plural = _("Product Images")


class TogetherPurchased(models.Model):
    main_product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("product"),
                                     related_name="main_product")
    related_product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("related products"),
                                        related_name="related_products")

    class Meta:
        verbose_name = _("Together Purchased")
        verbose_name_plural = _("Together Purchased")

    def __str__(self):
        return self.main_product.title


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("product"),
                                related_name="reviews")
    review = models.TextField(verbose_name=_("review"))
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Review")
        verbose_name_plural = _("Reviews")

    def __str__(self):
        return self.product.title


class Order(models.Model):
    class OrderStatus(models.TextChoices):
        NEW = 'new', _('new')
        ACCEPTED = 'accepted', _('accepted')
        PROGRESS = 'progress', _('progress')
        CANCELLED = 'cancelled', _('cancelled')
        FINISHED = 'finished', _('finished')

    name = models.CharField(max_length=120, verbose_name=_("name"))
    phone_number = models.CharField(max_length=120, verbose_name=_("phone number"),
                                    validators=[validate_phone_number])
    status = models.CharField(max_length=20, choices=OrderStatus.choices, default=OrderStatus.NEW)
    address = models.CharField(max_length=150, verbose_name=_("address"))

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return self.name


class OrderProduct(models.Model):
    class PaymentType(models.TextChoices):
        CASH = 'cash', _("cash")
        CARD = 'card', _("card")
        CARD_PRIVATE_BANK = 'card_private_bank', _("card private bank")

    class DeliveryType(models.TextChoices):
        PICK_UP = 'pick-up', _("pick-up")
        DELIVERY = 'delivery', _("delivery")

    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name=_("order"),
                              related_name="order_products")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("product"),
                                related_name="orders")
    payment = models.CharField(max_length=50, verbose_name=_("payment"), choices=PaymentType.choices, default=PaymentType.CASH)
    delivery = models.CharField(max_length=50, verbose_name=_("delivery"), choices=DeliveryType.choices, default=DeliveryType.DELIVERY)
    quantity = models.IntegerField(verbose_name=_("quantity"))

    class Meta:
        verbose_name = _("Order Product")
        verbose_name_plural = _("Order Products")

    def total_price(self):
        total_price = self.product.price * self.quantity
        return int(total_price)

    def __str__(self):
        return self.product.title


class Contacts(models.Model):
    phone_number1 = models.CharField(max_length=20, verbose_name=_("phone number1"), validators=[validate_phone_number])
    phone_number2 = models.CharField(max_length=20, verbose_name=_("phone number2"), validators=[validate_phone_number])

    email = models.EmailField(verbose_name=_("email"))
    address = models.CharField(max_length=150, verbose_name=_("address"))
    work_time = models.CharField(max_length=120, verbose_name=_("work time"))

    class Meta:
        verbose_name = _("Contacts")
        verbose_name_plural = _("Contacts")

    def __str__(self):
        return self.phone_number1


class Questions(models.Model):
    name = models.CharField(max_length=120, verbose_name=_("name"))
    phone_number = models.CharField(max_length=20, verbose_name=_("phone number"), validators=[validate_phone_number])

    question = models.TextField(verbose_name=_("question"))

    class Meta:
        verbose_name = _("Questions")
        verbose_name_plural = _("Questions")

    def __str__(self):
        return self.name

