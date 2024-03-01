from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    path('contact/<int:contact_id>/', views.contact, name='contact'),
    path('contact/create/', views.create, name='create'),
    path('user/create/', views.register, name='register'),
    path('user/login/', views.login_view, name='view'),
    path('user/logout/', views.logout_view, name='logout'),
    path('contact/<int:contact_id>/update/', views.update, name='update'),
    path('', views.index, name='index'),
    path('livro/', views.livro, name='livro'),
    path('search/', views.search, name='search'),
]
