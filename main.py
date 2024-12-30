import streamlit as st
from bills import get_bills, add_bill
from reminders import get_reminders

if "bills" not in st.session_state:
    st.session_state["bills"]=[]

st.title("Finance Management App - Bill Reminder")


st.subheader("Add New Bill")
with st.form("add_bill_form"):
    name= st.text_input("Bill Name")
    amount= st.number_input("Amount Due", min_value=0.01, format="%.2f")
    due_date= st.date_input("Due Date")
    submitted= st.form_submit_button("Add Bill")
    if submitted:
        add_bill(st.session_state["bills"], name, amount,due_date)
        st.success(f"Added bill:{name} (${amount:.2f}) due on {due_date}")

st.subheader("Upcoming Bills")
bills= get_bills(st.session_state["bills"])
st.table(bills)

st.subheader("Reminders")
reminders= get_reminders(bills)
if reminders:
    for reminder in reminders:
        st.warning(reminder)
else:
    st.write("No reminders at the time.")