import requests
import json

server_invite = input("Сервер: ")

def join(token):
    header = {
    "authorization": token,
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    }
    username = requests.get("https://discord.com/api/v9/users/@me", headers=header)
    print("Пользователь:", username.json()['username'])
    response = requests.post("https://discord.com/api/v9/invites/{}".format(server_invite), headers=header)
    print("Ответ:", response.json())


if __name__ == "__main__":
    file = open("token.txt", "r")

    while True:
        line = file.readline()
        if not line:
            break
        join(line.strip())

    file.close