# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class GoodsGroupbuying(models.Model):
    goods_id = models.CharField(max_length=16, blank=True, null=True)
    goods_name = models.CharField(max_length=64, blank=True, null=True)
    goods_price = models.CharField(max_length=8, blank=True, null=True)
    group_purchase_price = models.CharField(max_length=8)
    group_purchase_number = models.CharField(max_length=8, blank=True, null=True)
    goods_url = models.CharField(max_length=1024, blank=True, null=True)
    goods_begin_date = models.DateTimeField(blank=True, null=True)
    goods_end_date = models.DateTimeField(blank=True, null=True)
    inventory_number = models.CharField(max_length=8, blank=True, null=True)
    sold_number = models.CharField(max_length=8, blank=True, null=True)
    remain_number = models.CharField(max_length=8, blank=True, null=True)
    generalize_long_url = models.CharField(max_length=1024, blank=True, null=True)
    generalize_short_url = models.CharField(max_length=1024, blank=True, null=True)
    commission_rate = models.CharField(max_length=8, blank=True, null=True)
    commission_price = models.CharField(max_length=8, blank=True, null=True)
    primary_categories_id = models.CharField(max_length=64, blank=True, null=True)
    primary_categories_name = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return self.goods_id + ':' + self.goods_name + ':' + str(self.goods_price)

    class Meta:
        managed = False
        db_table = 'goods_groupbuying'
        verbose_name = '商品团购'
        verbose_name_plural = "商品团购2"
