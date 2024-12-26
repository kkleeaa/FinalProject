import streamlit as st
from finance import add_income, add_expenses, view_summary
from utils import print_summary

def main():
    st.title("Finance Manager")
    menu=["Add income", "Add expense", "View Financial Summary"]
    choice= st.sidebar.selectbox("Select Option", menu)

    if choice=="Add income":
        amount= st.number_input("Enter income amount:", min_value=0.0, step=0.01)
        source= st.text_input("Enter source of income:")
        if st.button("Add income"):
            add_income(amount, source)
            st.success(f"Income of {amount} from {source} added")
    elif choice=="Add expense":
        amount= st.number_input("Enter expense amount:", min_value=0.0, step=0.1)
        category=st.text_input("Enter expense category:")
        if st.button("Add expense"):
            add_expenses(amount, category)
            st.success(f"Expense of {amount} for {category} added")

    elif choice=="View Financial Summmary":
        summary=view_summary()
        print_summary(summary)

if __name__=="__main__":
    main()



