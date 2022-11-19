from django.db import models

# Create your models here.
        
        
class Category(models.Model):
    title = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.title
    
    
class SubCategory(models.Model):
    main_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.main_category.title + " - " + self.title
    
    
class Product(models.Model):
    product_name = models.CharField(max_length=200,null=True)
    product_description = models.TextField()
    image = models.ImageField(upload_to='product_images')
    price = models.IntegerField(null=True,default=0)
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True)
    deleted_on = models.DateTimeField(blank=True,null=True)

    
    def __str__(self):
        return self.product_name