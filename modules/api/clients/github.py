import requests

class GitHub:

    def get_user(self, username):
        r = requests.get(f'https://api.github.com/users/{username}')
        body = r.json()

        return body


    def search_repo(self, name):
        r = requests.get('https://api.github.com/search/repositories', 
                         params={'q':name}) #Означає що разом з адресою ми передаємо параметр q
        body = r.json() #записуємо тіло респонсу

        return body #повертаємо його
    

    
