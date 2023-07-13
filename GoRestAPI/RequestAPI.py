import requests
import random
import json
import string

#baseURL
base_url = "https://gorest.co.in"

#Auth Token
auth_token = "Bearer 59d3f6b90c6f9d3e573906b16892971edaf1efe7ad068a5e2588e78b8497155a"

#Get Random email id
def generate_random_email():
    domain = "automation.com"
    email_length = 10
    random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(email_length))
    email = random_string + "@" + domain
    return email
#GET Request
def get_request():
    url = base_url + "/public/v2/users"
    headers = {"Authorization": auth_token}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("Json response body: ", json_str)

#POST Request
def post_request():
    url = base_url + f"/public/v2/users"
    print("POST URL ===>", url)
    headers = {"Authorization": auth_token}
    data = {
    "name": "Anusha",
    "email": generate_random_email(),
    "gender": "female",
    "status": "active"
    }
    response = requests.post(url, json=data, headers=headers)
    assert response.status_code == 201
    json_data = response.json()
    json_str = json.dumps(json_data,indent=4)
    print("Json PUT body:", json_str)
    user_id = json_data["id"]
    assert "name" in json_data
    assert json_data["name"] == "Anusha"
    return user_id

#PUT Request
def put_request(user_id):
    url = base_url + f"/public/v2/users/{user_id}"
    print("PuT URL ===>", url)
    headers = {"Authorization": auth_token}
    data = {
    "name": "Anusha Palla",
    "email": generate_random_email(),
    "gender": "female",
    "status": "active"
    }
    response = requests.put(url, json=data, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("Json body PUT body:", json_str)

    assert "name" in json_data
    assert json_data["name"] == "Anusha Palla"
    assert json_data["id"] == user_id
    print("USER PUT request")
    print("------------------------")


#DELETE Request
def delete_request(user_id):
    url = base_url + f"/public/v2/users/{user_id}"
    headers = {"Authorization": auth_token}
    response = requests.delete(url, headers=headers)
    assert response.status_code == 204
    print("USER DELETED")
    print("------------------------")


#call
get_request()
user_id = post_request()
put_request(user_id)
delete_request(user_id)