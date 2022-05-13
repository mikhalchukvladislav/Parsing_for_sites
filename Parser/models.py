from django.db import models


class Url(models.Model):
    link = models.CharField(
        max_length=300,
        blank=True
    )
    
    def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
        return f'/{self.id}'

    def __str__(self):
        return f'{self.link}'

#     # def to_json(self):
#     #     return f'{self.link}'

class News(models.Model):
    url = models.URLField(max_length=300)
    domain = models.CharField(max_length=200)
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()
    country = models.CharField(max_length=200, null=True)
    is_dead = models.BooleanField()
    a = models.CharField(max_length=200, null=True)
    ns = models.CharField(max_length=200, null=True)
    cname = models.CharField(max_length=200, null=True)
    mx = models.CharField(max_length=200, null=True)
    txt = models.CharField(max_length=200, null=True)
    link = models.ForeignKey(Url, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.url}'