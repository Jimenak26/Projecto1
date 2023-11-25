from django.db import models
from django.db.models import BooleanField


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=20)
    correo = models.EmailField()
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    numero_de_pedido = models.ForeignKey('Pedido', on_delete=models.SET_NULL, blank=True, null=True, related_name='pedidos')
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.id} - {self.apellido} {self.nombre}'


class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_pedido = models.DateField()
    descripcion = models.TextField()
    estado = models.CharField(max_length=20, choices=[('pendiente', 'Pendiente'), ('en_proceso', 'En Proceso'),
                                                      ('completado', 'Completado')], default='pendiente')
    total = models.DecimalField(max_digits=10, decimal_places=2)
    pagado: BooleanField = models.BooleanField(default=False)

    numero = models.PositiveIntegerField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.numero:
            max_numero_cliente = Pedido.objects.filter(cliente=self.cliente).aggregate(models.Max('numero'))['numero__max']
            self.numero = max_numero_cliente + 1 if max_numero_cliente else 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.cliente}'


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    existencias = models.PositiveIntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
