import requests
from datetime import date
from urllib.parse import urljoin, urlencode


def get_period(period_years: int) -> tuple[str, str]:
    start_date = date(date.today().year - period_years, 1, 1).strftime('%d.%m.%Y')
    end_date = date.today().strftime('%d.%m.%Y')
    return start_date, end_date

def generate_api_url(andmestik_id: int, period_start: str, period_end: str) -> tuple[str, str]:
    BASE_URL = 'https://statistika.eestipank.ee/spring/'

    # URL Paths
    data_path = 'getRead' if andmestik_id == 2459 else 'getReadSumma'
    cols_path = 'getVeerud'

    # URL Parameters
    params = {
        'andmestikId': andmestik_id
        , 'parameetrid': ['kuupaevAlg', period_start, 'kuupaevLopp', period_end]
        , 'lang': 'eng'
        , 'fullDataMode': 'true'
    }

    data_url = f"{urljoin(BASE_URL, data_path)}?{urlencode(params, doseq=True)}"
    cols_url = f"{urljoin(BASE_URL, cols_path)}?{urlencode(params, doseq=True)}"

    return data_url, cols_url

def send_request(url: str) -> dict:
    HEADERS = {'Accept': 'application/json, text/plain, */*'}
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()
