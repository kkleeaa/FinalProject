import plotly.express as px

def expense_pie_chart(expenses):
    """Generate a pie chart for expenses by category using plotly.express."""
    if not expenses:
        print("No expenses provided for the data.")
        return None

    data={"Category": [e["category"] for e in expenses], "Amount":[e["amount"] for e in expenses]}

    fig=px.pie(data, names="Category", values="Amount", title="Expenses by category")
    return fig
def income_bar_chart(incomes):
    """Generate a bar chart for income over time using plotly.express."""
    if not incomes:
        print("No income provided for the data.")
        return None
    data={"Date":[i["date"] for i in incomes], "Amount": [i["amount"] for i in incomes]}
    print("Income data for chart:", data)
    fig= px.bar(data,x="Data",y="Amount", title="Income over time", labels={"Date", "Amount", "Income Amount"})
    return fig
