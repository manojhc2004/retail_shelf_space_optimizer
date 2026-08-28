import requests
from config import API_URL


def run_pipeline(
    file,
    min_support,
    greater_than,
    threshold,
    shelf_capacity,
):

    files = {
        "file": (
            file.name,
            file.getvalue(),
            "text/csv"
        )
    }

    data = {
        "min_support": min_support,
        "greater_than": greater_than,
        "threshold": threshold,
        "shelf_capacity": shelf_capacity,
    }

    response = requests.post(
        API_URL,
        files=files,
        data=data,
    )

    if response.status_code == 200:
        return response.json()

    raise Exception(response.text)