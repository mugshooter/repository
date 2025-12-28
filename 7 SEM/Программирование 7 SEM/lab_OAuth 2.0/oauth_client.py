import os
from requests_oauthlib import OAuth2Session

# Данные приложения GitHub (замените на свои)
CLIENT_ID = "ВАШ_CLIENT_ID"
CLIENT_SECRET = "ВАШ_CLIENT_SECRET"

# URL-адреса GitHub OAuth
AUTHORIZATION_BASE_URL = "https://github.com/login/oauth/authorize"
TOKEN_URL = "https://github.com/login/oauth/access_token"

def run_oauth_flow():
    # 1. Создание сессии и получение URL для авторизации
    github = OAuth2Session(CLIENT_ID)
    authorization_url, state = github.authorization_url(AUTHORIZATION_BASE_URL)

    print(f"--- Шаг 1: Перейдите по ссылке для авторизации ---\n{authorization_url}\n")

    # 2. Пользователь авторизуется и перенаправляется на redirect_uri
    redirect_response = input("Вставьте полный URL, на который вас перенаправили: ")

    # 3. Обмен кода авторизации на access token
    token = github.fetch_token(
        TOKEN_URL,
        client_secret=CLIENT_SECRET,
        authorization_response=redirect_response
    )

    print("\n--- Шаг 2: Токен получен успешно ---")
    print(f"Access Token: {token['access_token']}")

    # 4. Использование токена для доступа к защищенному ресурсу
    r = github.get("https://api.github.com/user")
    user_data = r.json()

    print("\n--- Шаг 3: Данные пользователя из GitHub API ---")
    print(f"Логин: {user_data.get('login')}")
    print(f"Имя: {user_data.get('name')}")
    print(f"Публичные репозитории: {user_data.get('public_repos')}")

if __name__ == "__main__":
    run_oauth_flow()