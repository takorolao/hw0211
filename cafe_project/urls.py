from django.contrib import admin
from django.urls import path, include
from cafe.views import cafe_list, transaction_list, cancel_transaction

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cafe_list, name='cafe_list'),  # Добавляем URL-маршрут для корневого пути
    path('cafe/', include('cafe.urls')),
     path('cafe/<int:cafe_id>/', transaction_list, name='transaction_list'),
    path('transaction/<int:transaction_id>/cancel/', cancel_transaction, name='cancel_transaction')
]
