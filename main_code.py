import  requests , time

# \\ Importing functions from flet module -- 
from flet import (
icons,
flet,
Page,
Text,
TextField,
Image,
Row,
IconButton
)


# \\ Takes the locations and collect information from the API -- and returns a dictionary of weather_info.
def getWeather(location):
    api_id = 'a81442b129ff26e3f19849d089b4bba5' 
    api = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_id
    json_data = requests.get(api).json()

    # \\ {"cod":"404","message":"city not found"} -- {"cod":"400","message":"Nothing to geocode"}.
    if json_data.get('cod') != '404' and json_data.get('cod') != '400':
        dict_info = {
            'weather_desc'   : json_data['weather'][0]['main'],
            'weather_icon'   : json_data['weather'][0]['icon'],
            'temp_C'         : int(json_data['main']['temp'] - 273.15),
            'feels_like_C'   : int(json_data['main']['feels_like'] - 273.15),
            'wind_speed'      : json_data['wind']['speed'],
            'pressure'       : json_data['main']['pressure'],
            'humidity'       : json_data['main']['humidity'],
            'sunrise'        : time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600)),
            'sunset'         : time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600)),
            'name'           : json_data['name'],
            'country'        : json_data['sys']['country'],                                                
        }

    else:
        dict_info = json_data

    return dict_info


def main(page: Page):

    page.theme_mode = 'dark'

    # \\ Row_01 -- weather_desc = [city_weather_desc,city_weather_icon,city_weather_temp].
    city_weather_desc = Text(
                            value = 'N/A',
                            size=30,
                            weight='bold',
                            color='white',
    )

    city_weather_icon =  Image(
                            src="http://openweathermap.org/img/wn/{}@2x.png".format('03d'),
                            width=300,
                            height=300,
                            fit='contain',
    )

    tmp_tup = ('N/A','N/A','N/A','N/A')
    temp_values_str = 'Temp  : {} °C / {}  °F \n Feels like  :  {} °C / {}  °F'.format(tmp_tup[0],tmp_tup[1],tmp_tup[2],tmp_tup[3])


    city_weather_temp = Text(
                        value =temp_values_str,
                        size=20,
                        weight='bold',
                        color='white',
    )

    weather_desc = Row([city_weather_desc,city_weather_icon,city_weather_temp],alignment='center')


    # \\ Row_02 -- sun_desc = [sunrise_icon,sunrise_time,sunset_icon,sunset_time].
    sunrise_icon = Image(
                    src= f'https://cdn-icons-png.flaticon.com/512/8098/8098385.png',
                    width=80,
                    height=80,
                    fit="contain",
                    color='orange',
    )
    
    sunrise_time = Text(
                    value = 'Sunrise   :   {}  AM{}'.format('N/A',' '*20),
                    size = 30,
                    weight='bold',
                    color='white',
    )

    
    sunset_icon =  Image(
                    src= f'https://cdn-icons-png.flaticon.com/512/3815/3815179.png',
                    width=80,
                    height=80,
                    fit="contain",
                    color='orange',
    )

    sunset_time = Text(
                    value = 'Sunset   :   {}  PM'.format('N/A'),
                    size = 30,
                    weight='bold',
                    color='white',
    )

    sun_desc = Row([sunrise_icon,sunrise_time,sunset_icon,sunset_time],alignment='center')

    # \\ Row_03 -- city_weather = [humidity_icon,humidity_details,wind_icon,wind_speed,pressure_icon,pressure_details]
    humidity_icon = Image(
                        src= f'https://cdn-icons-png.flaticon.com/512/727/727790.png',
                        width=55,
                        height=55,
                        fit="contain",
                        color='orange',
    )

    humidity_details = Text(
                        value = 'Humidity  :   {} %{}'.format('N/A',' '*5),
                        size = 25,
                        weight='bold',
                        color='white',
    )
    
    
    wind_icon  = Image(
                    src= f'https://cdn-icons-png.flaticon.com/512/5532/5532947.png',
                    width = 55,
                    height = 55,
                    fit = "contain",
                    color = 'orange',
    )

    wind_speed = Text(
                    value = 'Wind Speed    :   {} m/s{}'.format('N/A',' '*5),
                    size = 25,
                    weight='bold',
                    color='white',
    )

    
    pressure_icon = Image(
                        src= f'https://cdn-icons-png.flaticon.com/512/3093/3093409.png',
                        width=55,
                        height=55,
                        fit="contain",
                        color = 'orange',
    )

    pressure_details = Text(
                        value = 'Pressure  :   {} hPa'.format('N/A'),
                        size = 25,
                        weight='bold',
                        color='white',
    )
    

    city_weather = Row([humidity_icon,humidity_details,wind_icon,wind_speed,pressure_icon,pressure_details],alignment='center')


    # \\ Triggers the program -- when the search icon clicked or enter_key is pressed.
    def search_clicked(city):
        city_weather_icon.src = "http://openweathermap.org/img/wn/{}@2x.png".format('03d')

        try:
            weather_info = getWeather(city_name.value)

            if weather_info.get('cod') != '404' and weather_info.get('cod') != '400':
                info.value='{} {} , {}'.format(' '*10,weather_info['name'],weather_info['country'])
                city_weather_desc.value = weather_info['weather_desc']
                city_weather_icon.src = "http://openweathermap.org/img/wn/{}@2x.png".format(weather_info['weather_icon'])

                tmp_tup = (
                    str(weather_info['temp_C']),
                    str(int((weather_info['temp_C']*1.8) + 32)),
                    str(weather_info['feels_like_C']),
                    str(int((weather_info['feels_like_C']*1.8) + 32))
                    )

                temp_values_str = 'Temp  : {} °C / {}  °F \n Feels like  :  {} °C / {}  °F'.format(tmp_tup[0],tmp_tup[1],tmp_tup[2],tmp_tup[3])
                city_weather_temp.value = temp_values_str

                # \\ Row_02.value.update -- {sunrise_time,sunset_time}.value.update.
                sunrise_time.value = 'Sunrise   :   {}  AM{}'.format(str(weather_info['sunrise'])[:5],' '*20)
                sunset_time.value = 'Sunset   :   {}  PM'.format(str(weather_info['sunset'])[:5])
            
                # \\ Row_03.value.update -- {humidity_details,wind_speed,pressure_details}.value.update.
                humidity_details.value = 'Humidity  :   {} %{}'.format(weather_info['humidity'],' '*5)
                wind_speed.value = 'Wind Speed    :   {} m/s{}'.format(weather_info['wind_speed'],' '*5)
                pressure_details.value = 'Pressure  :   {} hPa'.format(weather_info['pressure'])

            else:
                info.value = '{} *{}'.format(' '*10,weather_info['message'])

                # \\ All values set to default -- with Error msg.
                default_values()

        except Exception as _err:
            # \\ All values set to default -- with Error msg.
            default_values()

            if 'Failed to establish a new connection' in str(_err):
                info.value = '{} *{}'.format(' '*10,"You're not connected\n" + 'ERR_INTERNET_DISCONNECTED')
               
            else:
                info.value = '{} *{}'.format(' '*10,'unknown Error\n'+ str(_err))
    

        page.update()
    

    def default_values():
        # \\ Row_01.value.default -- {city_weather_desc,city_weather_temp}.value.default.
        city_weather_desc.value = 'N/A'
        tmp_tup = ('N/A','N/A','N/A','N/A')
        temp_values_str = 'Temp  : {} °C / {}  °F \n Feels like  :  {} °C / {}  °F'.format(tmp_tup[0],tmp_tup[1],tmp_tup[2],tmp_tup[3])
        city_weather_temp.value = temp_values_str

        # \\ Row_03.value.default -- {sunrise_time,sunset_time}.value.default.
        sunrise_time.value = 'Sunrise   :   {}  AM{}'.format('N/A',' '*20)
        sunset_time.value = 'Sunset   :   {}  PM'.format('N/A')
            
        # \\ Row_03.value.default -- {humidity_details,wind_speed,pressure_details}.value.default.
        humidity_details.value = 'Humidity  :   {} %{}'.format('N/A',' '*5)
        wind_speed.value = 'Wind Speed    :   {} m/s{}'.format('N/A',' '*5)
        pressure_details.value = 'Pressure  :   {} hPa'.format('N/A')

    
    info = Text(
            value='{} {} , {}'.format(' '*10,'N/A','N/A'),
            size = 20,
            weight='bold',
            color='white',
    )

    city_name = TextField(
                    label="Name of the City",
                    icon = icons.LOCATION_ON,
                    color='white', 
                    border_color='white',
                    on_submit=search_clicked,
    )

    city_desc = Row(
        [city_name,
            IconButton(
            icon=icons.SEARCH,
            icon_color="orange",
            icon_size=40,
            tooltip="Search",
            on_click=search_clicked),info],
            alignment = 'center',
    )


    page.add(city_desc,
             weather_desc,
             sun_desc,
             city_weather,
    )
    
    page.update()

    
flet.app(target=main)