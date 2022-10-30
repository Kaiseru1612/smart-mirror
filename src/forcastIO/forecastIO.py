from forecastiopy import *
import apikey

api_key = apikey.API_KEY

Lisbon = [38.7252993, -9.1500364]

fio = ForecastIO.ForecastIO(api_key,
                            units=ForecastIO.ForecastIO.UNITS_SI,
                            lang=ForecastIO.ForecastIO.LANG_ENGLISH,
                            latitude=Lisbon[0], longitude=Lisbon[1])
                            
print('Latitude', fio.latitude, 'Longitude', fio.longitude)
print ('Timezone', fio.timezone, 'Offset', fio.offset)
print(fio.get_url()) # You might want to see the request url
if fio.has_hourly() is True:
	hourly = FIOHourly.FIOHourly(fio)
	print('Hourly')
	print('Summary:', hourly.summary)
	print('Icon:', hourly.icon)
	print
	for hour in range(0, hourly.hours()):
		print('Hour', hour+1)
		for item in hourly.get_hour(hour).keys():
			print(item + ' : ' + str(hourly.get_hour(hour)[item]))
		print
		# Or access attributes directly for a given minute. 
		# hourly.hour_5_time would also work
		print(hourly.hour_3_time)
		print
	print
else:
	print('No Hourly data')