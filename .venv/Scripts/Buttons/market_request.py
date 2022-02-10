import requests

def auth():
    with open('C:\\Users\\Timothy\\Desktop\\wframe_cookie.txt') as wframe_auth:
        auth = wframe_auth.readline()
    return auth

auth = auth()

def user_search():
    try:
        search = input("Type search item and hit enter: ")
    except Exception as e:
        print(f'oops.\n\n{e}')
    return search

def get_item_orders(item,auth):
    url = f"https://api.warframe.market/v1/items/{item}/orders"
    payload={}
    headers = {'Cookie': auth}
    try:
        response = requests.request("GET", url, headers=headers, data=payload)
        json_response = response.json()
    except Exception as e:
        json_response = e
    return json_response

def json_grab_fields(json_response):
    review_list = []
    for item in json_response["payload"]["orders"]:
        quantity = item["quantity"]
        order_type = item["order_type"]
        platinum = item["platinum"]
        user = item["user"]["ingame_name"]
        reputation = item["user"]["reputation"]
        status = item["user"]["status"]
        if order_type == "sell" and status != "offline":
            row = [platinum,quantity,reputation,status,user]
            review_list.append(row)
    review_list.sort()
    return review_list

search = user_search()
json_response = get_item_orders(search,auth)
review_list = json_grab_fields(json_response)
comment_text = f"\n\nActive Sell Orders for {search}\n\n"

for line in review_list:
    comment_text += f"{line}\n"
    
print(comment_text)