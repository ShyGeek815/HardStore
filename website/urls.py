from django.urls import path, include
from . import views

# URL adress
urlpatterns = [
    # Ссылки на главную страницу
    path('', views.home, name='home'),
    # создаем новую страницу (вход)
    #path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    # создаем новую страницу 
    path('record/<int:pk>', views.customer_record, name='record'),
    # создаем ссылку на страницу с товарами
    path('product/', views.hardstore_record, name='product'),
    # создаем ссылку на страницу с сотрудниками
    path('employee/', views.employee_record, name='employee'),
    # ссылка на удаление товара
    path('delete_product/<int:pk>', views.delete_record, name='delete_product'),
    # ссылка на добавение товара
    path('add_product', views.add_product, name='add_product'),
    # ссылка на добавение человека
    path('add_record', views.add_record, name='add_record'),
    # ссылка на удаление человека
    path('delete_record/<int:pk>', views.delete_record_home, name='delete_record'),
    # ссылка на изменение человека
    path('update_record/<int:pk>', views.update_record, name='update_record'),
    # ссылка на изменение товара
    path('update_product/<int:pk>', views.update_product, name='update_product'),

    # создаем ссылку на страницу склады
    path('storehouse/', views.storehouse, name='storehouse'),
    
    
]
