import requests
import json

app_key = "4d4dde1f5c4fa95d72975bfc08bde904"
code = "pezcc1dZgbYv6e555InqM1YgTPr_cIjG1x4bupEIaBs-ixafYYDJMkOyKoPbxum5rVw__worDKYAAAF2XIq8Jg"


url = "https://kauth.kakao.com/oauth/token"

data = {
    "grant_type" : "authorization_code",
    "client_id" : app_key,
    "redirect_url" : "https://locallhost.com",
    "code" : code
}
response = requests.post(url, data=data)
tokens = response.json()

with open("kakao_code.json", "w") as fp:
    json.dump(tokens, fp)

with open("kakao_code.json", "r") as fp:
    ts = json.load(fp)

print(ts)


#code 받기 위한 주소
#https://kauth.kakao.com/oauth/authorize?client_id=4d4dde1f5c4fa95d72975bfc08bde904&redirect_uri=https://locallhost.com&response_type=code

#rest_api_key (app_key) : 4d4dde1f5c4fa95d72975bfc08bde904