import requests
from datetime import datetime
import locale
API_KEY = "30fe9a818eee311372d043e62778e29e"
URL = "https://api.openweathermap.org/data/2.5/weather"

class Weather():

    def __init__(self, *args, **kwargs):

        if kwargs.get('country') and kwargs.get('city'):
            self.url = "{0}?{1}&appid={2}&units=metric&lang=ru".format(
                URL,
                f"q={kwargs['city']},{kwargs['country']}",
                API_KEY
            )
        elif kwargs.get('latitude') and kwargs.get('longitude'):
            self.url = "{0}?{1}&appid={2}&units=metric&lang=ru".format(
                URL,
                f"lat={kwargs['latitude']},&lon={kwargs['longitude']}",
                API_KEY
            )
        else:
            self.url = "{0}?{1}&appid={2}&units=metric&lang=ru".format(
                URL,
                'q=London,UK',
                API_KEY
            )

    def get_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            self.result = response.json()
        else:
            self.result = {}

    def send_db(self):
        pass

    def create_response(self):
        locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
        template = f"""Сегодня, {datetime.utcfromtimestamp(self.result['dt']+self.result['timezone']).strftime('%A %d/%m/%Y %H:%M:%S')}
        Погода в {self.result["name"]} {self.result['sys']['country']}:
          {self.result["weather"][0]["main"]}, {self.result["weather"][0]["description"]}.
          Температура воздуха: {self.result["main"]["temp"]}.
          Атмосферное давление: {self.result["main"]["pressure"]} мм/рс.
          Влажность воздуха: {self.result["main"]["humidity"]}%.
          Ветер: {self.result["wind"]["deg"]}.
          Скорость ветра: {self.result["wind"]["speed"]} м/c.
        """
        print(template)

    def get_response(self):
        return None#self.respose


if __name__ == '__main__':
    obj = Weather(country='BY', city='Minsk')
    print(obj.url)
    obj.get_data()
    print(obj.result)
    obj.create_response()
