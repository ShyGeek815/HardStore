from django.db import models 

# СОТРУДНИКИ
class Employee(models.Model):

    # временная метка - когда запись была создана
    created_at = models.DateTimeField(auto_now_add=True)
    familia = models.CharField(max_length=50)
    imya = models.CharField(max_length=50) 
    otchestvo = models.CharField(max_length=50)
    adress = models.CharField(max_length=300)
    email = models.CharField(max_length=200, default='@mail')
    phone = models.CharField(max_length=50)
    male_choice = models.CharField(max_length=50)
    date_of_birth = models.CharField(max_length=10, default='00.00.2000')
    position =  models.CharField(max_length=300)

    # то, что мы видим на экране 
    def __str__(self):
        return(f"{self.familia} {self.imya} {self.otchestvo} {self.adress} {self.email} {self.phone} {self.male_choice} {self.date_of_birth} {self.position}")

# ПОКУПАТЕЛИ
class Record(models.Model):
    MALE='М'
    FEMALE='Ж'
    MALE_CHOICES = [
        (MALE, 'Мужской'),
        (FEMALE, 'Женский'),
    ]
    # временная метка - когда запись была создана
    created_at = models.DateTimeField(auto_now_add=True)
    familia = models.CharField(max_length=50)
    imya = models.CharField(max_length=50) 
    otchestvo = models.CharField(max_length=50)
    email = models.EmailField(max_length=200, default='@mail')
    phone = models.CharField(max_length=50)
    male_choice = models.CharField(
        max_length=1,
        choices=MALE_CHOICES,
        default=None,
    )
    date_of_birth = models.CharField(max_length=10, default='01.01.2000')
    date_pockypki = models.DateTimeField(auto_now=True)

    # то, что мы видим на экране 
    def __str__(self):
        return(f"{self.familia} {self.imya} {self.otchestvo}")
    
# ТОВАРЫ
class HardStore_record(models.Model):
    # временная метка - когда запись была создана
    created_at = models.DateTimeField(auto_now_add=True)
    # категория товара
    name_category = models.CharField(max_length=50)
    # наименование товара
    name_product = models.CharField(max_length=100) 
    # бренд
    brand = models.CharField(max_length=50)
    # модель
    model_product = models.CharField(max_length=50)
    # гарантия товара
    warranty = models.CharField(max_length=30)
    # размеры (габариты)
    contry_product = models.CharField(max_length=30)
    # цена
    price_product = models.FloatField()
    # описание товара
    description_product = models.TextField()

    # то, что мы видим на экране 
    def __str__(self):
        return(f"{self.name_category} {self.name_product} {self.brand} {self.model_product} {self.contry_product} {self.price_product}")
    

# СКЛАДЫ
class Storehouse(models.Model):
    # временная метка - когда запись была создана
    created_at = models.DateTimeField(auto_now_add=True)
    # наименование (название) склада
    name_storehouse = models.CharField(max_length=50)
    # адрес склада
    adress_storehouse = models.CharField(max_length=100) 
    # телефон склада
    phone_storehouse = models.CharField(max_length=50)
    

    # то, что мы видим на экране 
    def __str__(self):
        return(f"{self.name_storehouse} {self.adress_storehouse} {self.phone_storehouse} ")