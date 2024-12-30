from models import Income, Expense
from database import save_income, save_expense, get_incomes, get_expenses
from database import incomes, expenses

def add_income(amount, source):
    income= Income(amount, source)
    save_income(income)
    print(f"Income of {amount} from {source} has been added")

def add_expenses(amount, category):
    expense= Expense(amount, category)
    save_expense(expense)
    print(f" Expense of {amount} for {category} has been added ")

def view_summary():
    total_income= sum(income.amount for income in get_incomes())
    total_expense=sum(expense.amount for expense in get_expenses())
    balance= total_income - total_expense
    return {"total_income": total_income, "total_expense": total_expense, "balance": balance}

def get_incomes():
    """Retrieve incomes as dictionaries for visualization."""
    return[{"amount": income.amount,"source": income.source,"date":income.date} for income in incomes]
def get_expenses():
    """Retrieve expenses as dictionaries for visualization."""
    return[{"amount": expense.amount, "category": expense.category, "date": expense.date} for expense in expenses]

