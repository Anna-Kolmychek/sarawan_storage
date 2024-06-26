from django.urls import path

from categories.apps import CategoriesConfig
from categories.views import CategotyListAPIView

app_name = CategoriesConfig.name

urlpatterns = [
    path('', CategotyListAPIView.as_view(), name='category-list'),
]

