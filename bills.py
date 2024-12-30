from datetime import datetime

def add_bill(bill_list, name, amount, due_date):
    """Add a bill to the list."""
    bill={"name": name, "amount": amount,"due_date": due_date}
    bill_list.append(bill)
def get_bills(bill_list):
    """Retrieve a list of bills formatted for display."""
    today= datetime.today().date()
    return [{"Name": bill["name"],"Amount": f"${bill['amount']:.2f}","Due Date": bill["due_date"], "Days left": (bill["due_date"]- today).days} for bill in bill_list]
