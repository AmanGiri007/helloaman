from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='Home'),
    path('lists/',views.list,name='List'),
    path('lists/<int:list_id>/',views.delete),
]
