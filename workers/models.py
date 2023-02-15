from django.db import models

class WorkerModel(models.Model):

    POST_LEVEL = (
        ('0', 'Руководитель'),
        ('1', 'Заместитель руководителя'),
        ('2', 'Заведующий отделением'),
        ('3', 'Преподаватель')
    )

    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=50, verbose_name='Отчество', blank=True)
    post = models.ForeignKey('PostModel', on_delete=models.SET_NULL, null=True, verbose_name='Должность')
    post_level = models.CharField(choices=POST_LEVEL, max_length=1, verbose_name='Уровень') #для отображения в списке на сайте
    foto = models.ImageField(verbose_name='Фото', upload_to='uploads/workers/foto')
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    info = models.TextField(verbose_name='Информация')

    def __str__(self):
        return(f'{self.last_name}  {self.first_name} {self.middle_name}')
    
    class Meta:

        verbose_name = 'Сотрудники'
        verbose_name_plural = 'Сотрудники'


class PostModel(models.Model):

    post_name = models.CharField(max_length=100, verbose_name='Наименование должности')

    def __str__(self):
        return(self.post_name)
    
    class Meta:

        verbose_name = 'Должности'
        verbose_name_plural = 'Должности'