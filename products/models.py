from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField

from common.models import Media


class Category(models.Model):
    name = models.CharField(_('name'), max_length=255)
    image = models.ForeignKey(Media, related_name='category_image',
                              on_delete=models.SET_NULL, null=True, blank=True)
    parent = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    class MPTTMeta:
        order_insertion_by = ['name']


class Product(models.Model):
    name = models.CharField(_("name"), max_length=255)
    price = models.FloatField(_("price"))
    short_description = models.TextField(_("short_description"))
    description = models.TextField(_("description"))
    quantity = models.IntegerField(_("quantity"))
    instructions = RichTextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    in_stock = models.BooleanField(_("in stock"), default=True)
    brand = models.CharField(_("brand"), max_length=255)
    discount = models.IntegerField(_("discount"), help_text=_("in percentage"))
    thumbnail = models.ForeignKey(Media, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.name


class ProductColor(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="colors")
    color = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"Product: {self.product.id} | Color: {self.color.id}"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ForeignKey(Media, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Product: {self.product.id}|Image: {self.image.id}"
    
    
class ProductSize(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="sizes")
    value = models.CharField(_("value"), max_length=255)
    
    def __str__(self):
        return f"Product: {self.product.id} | Size: {self.value}"
    
    
class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    text = models.TextField()
    
    def __str__(self):
        return f"Products: {self.product.id} | User: {self.user.id}"

    
class Wishlist(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="wishlists")
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name="wishlists")

    def __str__(self):
        return f"Product: {self.product.id}|User: {self.user.id}"
    
    
    
    