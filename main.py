from utils import parser, chart
from utils.http import fetch_data

OVERDUE_LOANS_ID = 2459

def main():
    # Get data
    data_json, cols_json = fetch_data(andmestik_id=OVERDUE_LOANS_ID)
    if not all([data_json, cols_json]):
        print('Failed to fetch data')
        return

    # Parse data
    title = parser.get_title(cols_json)
    raw_df = parser.prepare_raw_dataframe(data_json, cols_json)
    result = parser.return_result_df(raw_df)

    # Open chart
    chart.show_overdue_loans_graph(result, title)

if __name__ == '__main__':
    main()
