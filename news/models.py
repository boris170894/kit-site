from django.db import models
from django.urls import reverse

class NewsModel(models.Model):

    category = models.ForeignKey('NewsCategoryModel', on_delete=models.SET_NULL, blank=False, null=True, verbose_name='Категория') #Вот тут хз будет ли работать
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    img = models.ImageField(verbose_name='Изображение новости', upload_to='uploads/news/%Y/%m/%d/')
    content = models.TextField(verbose_name='Содержимое')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(verbose_name='Опубликовано', default=False)

    def __str__(self):
        return(self.title)
    
    def get_absolute_url(self):
        return reverse('news-detail-view', args=[str(self.pk)])
    
    class Meta:

        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'


class NewsCategoryModel(models.Model):

    name = models.CharField(max_length=100, verbose_name='Наименование категории')

    def __str__(self):
        return(self.name)
    
    class Meta:

        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
