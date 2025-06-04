from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField("Заголовок", max_length = 120)
    desc = models.TextField("Описание, текст")
    image = models.ImageField("Изображение", upload_to = "posts/")
    created_at = models.DateField("Дата создания", auto_now_add = True)

    def __str__(self) -> str:
        return self.title
    
    class Meta: 
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ["-created_at"]
