from django.urls import path,include
from .views import welcome,todo_list_create,todo_get_update_delete,Todos,TodosRUD,TodoMVS
from rest_framework import routers
router=routers.DefaultRouter()
router.register('todo',TodoMVS)

urlpatterns = [
    # path('', welcome),

    # #fbv
    # path('todos/',todo_list_create),
    # path('todos/<int:id>/',todo_get_update_delete),

    # #cbv
    # path('todo/',Todos.as_view()),
    # # path('todo/<int:pk>/',TodosRUD.as_view()),
    # path('todo/<int:id>/',TodosRUD.as_view()),
    
    # #MVS
    path('',include(router.urls))

]   