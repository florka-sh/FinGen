from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IncomeCategoryView, ExpensesCategoryView


router = DefaultRouter()
router.register(r'income-category', IncomeCategoryView, basename='income-category')
router.register(r'expenses-category', ExpensesCategoryView, basename='expenses-category')


urlpatterns = [
    path('', include(router.urls)),
]