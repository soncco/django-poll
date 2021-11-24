from django.db import models


class Encuesta(models.Model):
    titulo = models.CharField(max_length=255)
    vencimiento = models.DateTimeField(null=True, blank=True)
    activo = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo


class Opcion(models.Model):
    encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE)
    opcion = models.CharField(max_length=255)
    votos = models.IntegerField(default=0)


class Ip(models.Model):
    encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE)
    ip = models.CharField(max_length=255)
