from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from.serializers import ExpenseSerializer
from .models import Expense


class ExpenseViewSet(ModelViewSet):
    """
    A viewset for viewing and editing expense instances.
    """
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()
