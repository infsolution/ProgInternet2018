from django.urls import path
from accounts import views
urlpatterns = [
    path('accounts',views.account_list, name='list'),
    path('accounts/<int:account_id>',views.account_detail, name='detail'),
]