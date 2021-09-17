from django.db import models
from datetime import datetime
from django.forms import model_to_dict
from config.settings import STATIC_URL, MEDIA_URL
from core.erp.choices import type_identification, type_person, responsibility

#Modelos de clientes
class Country(models.Model):
    id_country = models.AutoField(verbose_name='Código país', primary_key=True, unique=True)
    name_country = models.CharField(verbose_name='País', max_length=210, null=True, blank=True)

    def __str__(self):
        return self.name_country

    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Paises'
        ordering = ['id_country']

class Dptos(models.Model):
    id_dpto = models.AutoField(verbose_name='Código dpto', primary_key=True, unique=True)
    id_country_fk = models.ForeignKey(Country, on_delete=models.CASCADE)
    name_dpto = models.CharField(verbose_name='Departamento', max_length=210, null=True, blank=True)

    def __str__(self):
        return self.name_dpto

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        ordering = ['id_dpto']

class City(models.Model):
    id_city = models.AutoField(verbose_name='Código ciudad', primary_key=True, unique=True)
    id_dpto_fk = models.ForeignKey(Dptos, on_delete=models.CASCADE)
    name_city = models.CharField(verbose_name='Ciudad', max_length=210, null=True, blank=True)

    def __str__(self):
        return self.name_city

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'
        ordering = ['id_city']

class Contact(models.Model):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    type_identification = models.CharField(verbose_name='Tipo de identificación', max_length=210, choices=type_identification, default='', blank=False, null=False)
    identification = models.CharField(max_length=10, unique=True, verbose_name='Identificación', blank=False, null=False)
    dv = models.CharField(verbose_name='Dv', max_length=2, blank=False, null=False, )
    name_client_1 = models.CharField(verbose_name='Nombre', max_length=150,  blank=False, null=False)
    name_client_2 = models.CharField(verbose_name='Segundo nombre', max_length=150, blank=True, null=True)
    last_names_cliente = models.CharField(verbose_name='Apellidos', max_length=150, blank=False, null=False)
    type_person = models.CharField(verbose_name='Tipo de persona', max_length=210, choices=type_person, default='', blank=False, null=False)
    type_responsibility = models.CharField(verbose_name='Tipo de responbilidad', max_length=210, choices=responsibility, default='', blank=False, null=False)
    address = models.CharField(verbose_name='Dirección', max_length=150, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    departament = models.ForeignKey(Dptos, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    email = models.EmailField(verbose_name='Correo', max_length=210, blank=False, null=False)
    tel_1 = models.CharField(verbose_name='Teléfono 1', max_length=10, null=True, blank=True)
    tel_2 = models.CharField(verbose_name='Teléfono 2', max_length=10, null=True, blank=True)
    mobile = models.CharField(verbose_name='Celular', max_length=10, blank=False, null=False)
    client = models.BooleanField(verbose_name='Cliente')
    provider = models.BooleanField(verbose_name='Proveedor')

    def __str__(self):
        return self.name_client_1

    def toJSON(self):
        item = model_to_dict(self)
        item['id'] = self.id
        return item

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

#Modelo de producto

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    desc = models.CharField(max_length=500, null=True, blank=True, verbose_name='Descripción')

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']

class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    reference = models.CharField(max_length=10, verbose_name='Referencia', unique=True)
    cost = models.DecimalField(verbose_name='Costo', decimal_places=2, default=0.00, max_digits=13)
    price = models.DecimalField(verbose_name='Precio', decimal_places=2, default=0.00, max_digits=13)
    description = models.TextField(verbose_name='Descripción', max_length=450)
    cate = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True)
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    inventory = models.BooleanField(verbose_name='¿Inventariable?')

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']

class Sale(models.Model):
    cli = models.ForeignKey(Contact, on_delete=models.CASCADE)
    date_joined = models.DateField(default=datetime.now)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.cli.name_client_1

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['id']

class DetSale(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    prod = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cant = models.IntegerField(default=0)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.prod.name

    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalle de Ventas'
        ordering = ['id']
