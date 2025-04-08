from utils import http

url = "https://statistika.eestipank.ee/#/en/p/FINANTSSEKTOR/147/650" # reference page
andmestik_ids=[770,802,2459] # stock_of_loans, turnover_of_loans, overdue_loans

start_date, end_date = http.get_period(3)
data_url, cols_url = http.generate_api_url(andmestik_id=802, period_start=start_date, period_end=end_date)
data_json = http.send_request(data_url)
cols_json = http.send_request(cols_url)
if data_json and cols_json:
    print("Data received successfully")
