from . import views 
from django.urls import path

app_name = 'transaction'

urlpatterns = [
    path("", views.transaction_list, name = 'list'), #пустий шлях, щоб зайти на головну "транзакції"
    path("<int:tr_id>/", views.transaction_detail, name = "detail"),
    path("category/<int:category_id>/", views.transaction_by_category, name="transaction_by_category"),
    path("sorted/", views.soreted_transaction, name="sorted_transaction")
]