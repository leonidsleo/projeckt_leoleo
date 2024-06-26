from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    age = models.IntegerField()


    def __str__(self) :
        return f'Имя: {self.name}, почта: {self.email}, возраст: {self.age}'

class Product(models.Model):
    namme = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)



# создание связей пример
class Autor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()


    def __str__(self) -> str:
        return f'Имя: {self.name}, эл.адрес: {self.email}'
    

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)


    def __str__(self):
        return f'Заголовок поста: {self.title}'
    
    """метод разбивает переменную content стр.41 на слова и извлекаем и возвращаем 8 первых слов
    для этого делаем изменения в запросе в файле get_post_by_autor_id"""
    def get_summary(self):
        words = self.content.split()
        return f'{" ".join(words[:8])}...'