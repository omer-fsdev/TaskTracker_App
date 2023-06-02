from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    todo_detail=serializers.HyperlinkedIdentityField(view_name='todo-detail')

    class Meta:
        model=Todo
        # fields=(__all__)
        fields=('id',
                'todo_detail',
                'task',
                'description',
                'is_done',
                'created_date',
                'update_date',
                'priority'
        )


