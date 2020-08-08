from django.db import models
from datetime import datetime  

class Goods(models.Model):
    CATEGORY = (
        ('furniture', _('Furniture')),
        ('cell_phones', _('Cell phones')),
    )

    goods_name = models.CharField(max_length=200)
    goods_category.CharField(max_length=32, choices=CATEGORY)
    pub_date = models.DateTimeField(auto_now_add=True, blank=False)





