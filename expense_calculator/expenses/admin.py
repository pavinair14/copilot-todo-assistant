from django.contrib import admin
from .models import Expense


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'date', 'category','id')  # Include the id field in the list display
    list_filter = ('category', 'date')
    search_fields = ('name', 'category')