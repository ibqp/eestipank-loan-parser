from utils import parser, chart
from utils.http import fetch_data

YEARS = 5
OVERDUE_LOANS_ID = 2459

def main():
    # Get data
    data_json, cols_json = fetch_data(period_years=YEARS, andmestik_id=OVERDUE_LOANS_ID)
    if not all([data_json, cols_json]):
        return

    # Parse data
    title, df = parser.prepare_raw_dataframe(data_json, cols_json)
    result = parser.return_result(df)

    # Open chart
    chart.show_overdue_loans_graph(result, title)

if __name__ == '__main__':
    main()
