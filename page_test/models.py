from django.db import models

# Create your models here.
class Areasinfo(models.Model):
    atitle = models.CharField(max_length=50)
    aParent = models.ForeignKey('self',null=True,blank=False) # 自关联属性

    class Meta:
        db_table = 'areas'