from django.db import models

class Category(models.Model):
    name_EN = models.CharField(max_length=100)
    name_AR = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories/', null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcategories')

    def __str__(self):
        return self.name_AR
    class Meta:
        verbose_name = "Category"          # Singular form
        verbose_name_plural = "Category"    # Keep singular in admin

class Product(models.Model):
    name_EN = models.CharField(max_length=100)
    name_AR = models.CharField(max_length=100)
    description_EN = models.TextField()
    description_AR = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    pdf = models.FileField(upload_to='product_pdfs/', null=True, blank=True)  # PDF file field
    def __str__(self):
        return self.name_AR
    class Meta:
        verbose_name = "Product"          # Singular form
        verbose_name_plural = "Product" 

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return f"Image for {self.product.name_AR}"


class Projects(models.Model):
    name_EN = models.CharField(max_length=100)
    name_AR = models.CharField(max_length=100)
    description_EN = models.TextField()
    description_AR = models.TextField()
    image = models.ImageField(upload_to='Projects/')
    image2 = models.ImageField(upload_to='Projects/')
    class Meta:
        verbose_name = "Projects"          # Singular form
        verbose_name_plural = "Projects" 
    
    def __str__(self):
        return self.name_AR