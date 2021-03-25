from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    slug = models.SlugField(unique=True, verbose_name='Ссылка')
    image = models.ImageField(upload_to="blog/%Y%m%d")
    body = models.TextField()
    publish = models.DateField(verbose_name='Дата публикации')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', args=[self.slug])

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Education(models.Model):
    year = models.IntegerField()
    educational_institution = models.CharField(max_length=50)
    faculty = models.CharField(max_length=50)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.educational_institution

    class Meta:
        verbose_name = 'Обучение'
        verbose_name_plural = 'Обучение'


class Experience(models.Model):
    date_of_beginning = models.IntegerField()
    end_date = models.IntegerField()
    place_of_work = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.place_of_work

    class Meta:
        verbose_name = 'Опыт'
        verbose_name_plural = 'Опыт'


class Certificates(models.Model):
    image = models.ImageField(upload_to='certificates/')
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'


class Skills(models.Model):
    skill = models.CharField(max_length=50)

    def __str__(self):
        return self.skill

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'
