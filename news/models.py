from django.db import models

class News(models.Model):
    title = models.CharField("Заголовок", max_length=200)
    content = models.TextField("Содержание")
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)
    author = models.CharField("Имя пользователя", max_length=100)

    def __str__(self):
        return self.title
