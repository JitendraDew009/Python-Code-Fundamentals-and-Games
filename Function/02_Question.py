# Splitting Complex Tasks
# You are crating a monthly report for a cafe's sales.
# Instead of putting all logic in one place, break it down.
# Task:
    # write a function generate_report() that calls:
    # fetch_sales()
    # filter_valid_orders()
    # summarize_data()

def fetch_sales():
    print("Fetching the sales data")

def filter_vaild_sales():
    print("Filtering the sales data")

def summarize_data():
    print("Summarizing sales data")

def generate_report():
        
        
        fetch_sales()
        filter_vaild_sales()
        summarize_data()
    
        print("Report is Ready")

generate_report()