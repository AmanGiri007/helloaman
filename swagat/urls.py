from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='Home'),
    path('lists/',views.list,name='List'),
    path('lists/<int:list_id>/',views.delete),
    path('login/',views.LoginView.as_view(),name="login"),
    path('logout/',views.LogoutView.as_view(),name="logout"),
    path('register/',views.RegisterView.as_view(),name="register"),
    path('lists/edited/<int:list_id>/',views.edit),
]
