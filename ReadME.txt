\\ Desc -- Weather_App v.2.4.5

Python : 3.8.10 64-bit
Last-Updated  = (
    28_Oct_2022 ,
    '17_00'.format{24H},
)




\\ Data structures -- 

    dict_info = {
        'weather_desc'    : json_data['weather'][0]['main'],
        'weather_icon'    : json_data['weather'][0]['icon'],
        'temp_C'          : int(json_data['main']['temp'] - 273.15),
        'feels_like_C'    : int(json_data['main']['feels_like'] - 273.15),
        'wind_speed'      : json_data['wind']['speed'],
        'pressure'        : json_data['main']['pressure'],
        'humidity'        : json_data['main']['humidity'],
        'sunrise'         : time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600)),
        'sunset'          : time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600)),
        'name'            : json_data['name'],
        'country'         : json_data['sys']['country'],                                                
    } 

                    

   
\\ API Errors --       

    \\ When given location is unkown by the API.
    {"cod":"404","message":"city not found"}

    \\ When given location or (str) is a black (str) == ''.
    {"cod":"400","message":"Nothing to geocode"}

    \\ When not connected to internet.
    HTTPSConnectionPool(
        host='api.openweathermap.org',
        port=443): 

    Max retries exceeded with url: /data/2.5/weather?q={}&appid=a81442b129ff26e3f19849d089b4bba5 
    (Caused by NewConnectionError(
        '<urllib3.connection.HTTPSConnection object at 0x000001120F473AF0>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed'
        )
    )




\\ modules required --

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
                                                                                          

flet.docs = 'https://flet.dev/docs/'                                                                                               