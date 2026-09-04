# imports for django_rest_framework tests
from rest_framework.test import APITestCase

from .models import Expense

class ExpenseAPITestCase(APITestCase):
    def setUp(self):
       # create 3 expenses
        Expense.objects.bulk_create([
            Expense(name='Food', amount=10.00, category='Food'),
            Expense(name='Transport', amount=20.00, category='Transport'),
            Expense(name='Entertainment', amount=30.00, category='Entertainment')
        ])

    def test_expense_list(self):
        response = self.client.get('/api/expenses/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)

    def test_expenses_detail(self):
        expense = Expense.objects.first()
        response = self.client.get(f'/api/expenses/{expense.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], expense.name)
        self.assertEqual(float(response.data['amount']), float(expense.amount))
        self.assertEqual(response.data['category'], expense.category)

    def test_create_expense(self):
        data = {
            'name': 'New Expense',
            'amount': 50.00,
            'category': 'Food'
        }
        response = self.client.post('/api/expenses/', data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Expense.objects.count(), 4)
        self.assertEqual(Expense.objects.last().name, 'New Expense')

    def test_update_expense(self):
        expense = Expense.objects.first()
        data = {
            'name': 'Updated Expense',
            'amount': 100.00,
            'category': 'Entertainment'
        }
        response = self.client.put(f'/api/expenses/{expense.id}/', data)
        self.assertEqual(response.status_code, 200)
        expense.refresh_from_db()
        self.assertEqual(expense.name, 'Updated Expense')
        self.assertEqual(float(expense.amount), 100.00)
        self.assertEqual(expense.category, 'Entertainment')

    def test_delete_expense(self):
        expense = Expense.objects.first()
        response = self.client.delete(f'/api/expenses/{expense.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Expense.objects.count(), 2)

    def tearDown(self):
        Expense.objects.all().delete()  