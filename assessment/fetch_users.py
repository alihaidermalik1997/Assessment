import requests
from assessment.customers.models import Customer

url = "https://demo.mifos.io/fineract-provider/api/v1/clients?limit=15&offset=0"
username = "mifos"
password = "password"


def parse_user_data(page_items):
    user_list = []
    for page_item in page_items:
        if page_item.get("mobileNo", None):
            user = {}
            user["client_id"] = page_item["id"]
            user["full_name"] = page_item["displayName"]
            user["status"] = page_item["status"]
            user["mobile_number"] = page_item["mobileNo"]
            user["office_name"] = page_item["officeName"]
            user_list.append(user)
    return user_list


def fetch_user():
    try:
        response = requests.get(
            url, auth=requests.auth.HTTPBasicAuth(username, password)
        )
        data = response.json()
        return parse_user_data(data["pageItems"])
    except Exception:
        return None


def save_user():
    user_list = fetch_user()
    if user_list:
        users_data = [Customer(**user_data) for user_data in user_list]
        Customer.objects.bulk_create(users_data, ignore_conflicts=True)
        return True
    return False
