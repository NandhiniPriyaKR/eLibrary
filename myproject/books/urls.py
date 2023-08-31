from django.urls import path
from . import views

urlpatterns = [
    # /books/
    path('', views.index.as_view(), name='index'),
    # /books/id
    path('register/',views.UserFormView.as_view(),name='username'),
    # registration
    path('<pk>/', views.details.as_view(), name='details')
   
]
