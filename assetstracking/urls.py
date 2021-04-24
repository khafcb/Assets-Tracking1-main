from django.urls    import path
from .              import views


urlpatterns = [
    path('', views.index, name="index"),
    path('assets', views.home, name="assets"),
    path('rfid/', views.rfid, name="rfid"),
    path('tags/<str:idd>/', views.tags, name="tags"),
    path('packet/', views.packet),
    path('welcome', views.index),
    path('login', views.login, name="login"),

    path('employee/<str:employee_test>/', views.employee, name="employee"),
    path('subscriber/<str:subscriber_test>/', views.subscriber, name="subscriber"),


    path('createBorrowing/<str:pk>/', views.createBorrowing, name="createBorrowing"),
    path('deleteBorrowing/<str:pk>/', views.deleteBorrowing, name="deleteBorrowing"),
    path('extendBorrowing/<str:pk>/', views.extendBorrowing, name="extendBorrowing"),

    path('createAsset/<str:asset11>/', views.createAsset, name="createAsset"),
    path('updateAsset/<str:pk>/', views.updateAsset, name="updateAsset"),
    path('deleteAsset/<str:pk>/', views.deleteAsset, name="deleteAsset"),
    
    path('createReader/<str:reader>/', views.createReader, name="createReader"),
    
    path('SendingEmail/', views.SendingEmail, name="SendingEmail"),


]
