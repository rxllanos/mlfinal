from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Task_name(models.Model):
    class Meta:
        verbose_name = 'TaskName'
        verbose_name_plural = 'TaskNames'
    name = models.CharField(max_length=100, null=False, blank=False)
    def __str__(self):
        return self.name

class task(models.Model): 
    responsable = models.ForeignKey(User, on_delete=models.CASCADE, default="TBA" , null=True, blank=True, related_name="asignee")
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Task_name, on_delete=models.SET_NULL, null=True, blank=True)
    tcompletado = models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.now)
    fecha_terminado = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}... Completado? {self.tcompletado} (Y/N)"

    def completado(self):
        if self.tcompletado:
            return "SI"
        else:
            return "NO"
        
    class Meta:
        ordering = ['tcompletado']


