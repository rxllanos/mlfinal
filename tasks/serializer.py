from rest_framework import serializers
from .models import task, Task_name


class task_nameserializer(serializers.ModelSerializer):
    class Meta:
        model = Task_name
        fields = '__all__'


class taskserializer(serializers.ModelSerializer):
    empleado = serializers.CharField(source='responsable.first_name')
    group_set = serializers.CharField(source="category")
    class Meta:
        model = task
        fields = ['id','title','description','tcompletado', 'completado','group_set','empleado']