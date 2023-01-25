from django.db import models
from django.db.models import SET_NULL, Sum
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify

from apps.user.models import Student


# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Brand, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=3)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=12)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=SET_NULL, null=True, blank=True, related_name='cat_product')
    brand = models.ForeignKey(Brand, on_delete=SET_NULL, null=True, blank=True, related_name='brand_product')
    tag = models.ManyToManyField(Tag, related_name='tag_product')
    color = models.ManyToManyField(Color, related_name='color_product')
    size = models.ManyToManyField(Size, related_name='size_product')
    thumbnail = models.ImageField(upload_to='product')
    price = models.FloatField(default=0)
    is_offer = models.BooleanField(default=False)
    offer_price = models.FloatField(default=0)
    short_description = models.CharField(max_length=250, null=True, blank=True)
    long_description = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        a = slugify(self.title)
        self.slug = a + '-' + str(self.id)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_img')
    image = models.ImageField(upload_to='product')

    def __str__(self):
        return str(self.product.title)


class Order(models.Model):
    code = models.CharField(max_length=100, null=True, blank=True)
    student = models.ForeignKey(Student, on_delete=SET_NULL, null=True, blank=True, related_name='student_order')
    amount = models.FloatField(default=0, null=True, blank=True)
    coupon = models.CharField(max_length=100, null=True, blank=True)
    coupon_amount = models.FloatField(default=0, null=True, blank=True)
    final_amount = models.FloatField(default=0, null=True, blank=True)
    is_paid = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        am = self.order_item.aggregate(Sum('price')).get('price__sum', 0)
        self.amount = am

        self.final_amount = am
        super(Order, self).save(*args, **kwargs)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_item')
    product = models.ForeignKey(Product, on_delete=SET_NULL, null=True, blank=True)
    qty = models.FloatField(default=0)
    unit = models.FloatField(default=0)
    price = models.FloatField(default=0)

    def save(self, *args, **kwargs):
        self.price = self.qty * self.unit
        super(OrderItem, self).save(*args, **kwargs)


@receiver(post_save, sender=Order)
def signal_code(sender, instance, created, **kwargs):
    if created:
        instance.code = 'ORD' + '-' + str(instance.id)
        # amount = OrderItem.objects.filter(order__id=instance.id).aggregate(Sum('price')).get('price__sum', 0)
        # instance.amount = amount
        # # # if instance.coupon:
        # # # c = Coupon.
        # instance.final_amount = amount
        post_save.disconnect(signal_code, sender=Order)
        instance.save()
        post_save.connect(signal_code, sender=Order)

# @receiver(post_save, sender=OrderItem)
# def signal_price(sender, instance, created, **kwargs):
#     if created:
#         amount = OrderItem.objects.filter(order=instance.order).aggregate(Sum('price')).get('price__sum')
#         instance.order.amount = amount
#         # if instance.coupon:
#         # c = Coupon.
#         instance.order.final_amount = amount
