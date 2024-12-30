from datetime import datetime

def get_reminders(bills):
    """Generate reminders for bills."""
    today = datetime.today().date()
    reminders = []

    for bill in bills:
        days_left = bill["Days Left"]
        if days_left == 0:
            reminders.append(f" **{bill['Name']}** is due **today** (${bill['Amount']})!")
        elif 0 < days_left <= 7:
            reminders.append(f"**{bill['Name']}** is due in **{days_left} days** (${bill['Amount']}).")

    return reminders
