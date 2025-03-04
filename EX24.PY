def display_invoice(username,amount, due_date):
    print(f"Hello {username}!")
    print(f"Your bill of ${amount:.2f} is due on {due_date}.")
    
display_invoice("Ashutosh", 100.00, "2020-01-01")