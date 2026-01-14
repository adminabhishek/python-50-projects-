            #  splitting the complex task
# you are creating a monthly report for a cafe sales .
# instead of putting al logic in one place ,break iti down .
# write a function generate_report() that calls :
# fetch_sales()
# filter_valid_orders()
# # summerise_date() 

def fetch_sales():
    print("fetching the sals data")

def filter_valid_orders():
    print("filtering vlid sales data ")

def summerise_data():
    print("summerising sales data") 

def generate_reports():
    fetch_sales()
    filter_valid_orders()
    summerise_data()
    print("report is ready")

generate_reports()