telegram_bot_token = "1793454317:AAEzG0o7-vtW2WpkUwdCq73YiGHYJYTViTw"
side_weather_token = "886705b4c1182eb1c69f28eb8c520e20"
weather_token = "274e16bcd29fc6003638a44b00f207cd"

weather_root_url = "http://api.openweathermap.org/data/2.5/weather"

ok_codes = (200, 201, 202, 203, 204, 205)
available_currency_countries = ("uk", "rb")
currency_necessary_keys = {"uk": ('txt', 'rate', 'cc', 'exchangedate'),
                           "rb": ('Date', 'Cur_Abbreviation', 'Cur_Scale', 'Cur_Name', 'Cur_OfficialRate')}

bank_root_urls = {"rb_root_url": "https://www.nbrb.by/api/exrates/rates/",
                  "uk_root_url": "https://bank.gov.ua/NBUStatService/v1/statdirectory/"}

message_unknown_country = """Введите, пожалуйста, код страны,курс валют которой вас интересует.Пока доступны Беларусь (br) и Украина (uk).\n
							 Для этого отправьте сообщение /country uk или /country rb """

user_country = ""
hello_message = """Привет! Пока доступен следующий функцонал:\n
                    /start - начало работы \n
				    /country - задать боту свою страну для получения курса валют, доступны uk и rb \n
				    /курс - узнать урс валюты на сегодня, для выбранной страны, через аббревиатуру. Например /курс USD 
				    /weather - узнать погоду для выбранного города, например /weather Minsk или /weather Lviv.
				    """
