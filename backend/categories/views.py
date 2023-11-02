from .serializers import IncomeCategorySerializer, ExpensesCategorySerializer
from rest_framework.viewsets import ModelViewSet
from .models import IncomeCategory , ExpensesCategory


class IncomeCategoryView(ModelViewSet):
    serializer_class = IncomeCategorySerializer
    queryset = IncomeCategory.objects.all()

class ExpensesCategoryView(ModelViewSet):
    serializer_class = ExpensesCategorySerializer
    queryset = ExpensesCategory.objects.all()
