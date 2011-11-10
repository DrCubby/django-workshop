# encoding: utf-8
from django.db import models

from cookbook.basemodels import DateTimeInfo


class Article(DateTimeInfo):
    headline = models.CharField('Überschrift', max_length=100)
    body = models.TextField('Inhalt')

    class Meta:
        verbose_name = 'Artikel'
        verbose_name_plural = 'Artikel'
        ordering = ['-date_updated']

    def __unicode__(self):
        return self.headline