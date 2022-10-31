from forecastiopy import *
import apikey

api_key = apikey.API_KEY

BKUni = [10.77305970058611, 106.65934269345048]

fio = ForecastIO.ForecastIO(api_key,
                            units=ForecastIO.ForecastIO.UNITS_SI,
                            lang=ForecastIO.ForecastIO.LANG_ENGLISH,
                            latitude=BKUni[0], longitude=BKUni[1])
                            
# print('Latitude', fio.latitude, 'Longitude', fio.longitude)
# print ('Timezone', fio.timezone, 'Offset', fio.offset)
# print(fio.get_url()) # You might want to see the request url
# if fio.has_hourly() is True:
# 	hourly = FIOHourly.FIOHourly(fio)
# 	print('Hourly')
# 	print('Summary:', hourly.summary)
# 	print('Icon:', hourly.icon)
# 	print()
# 	for hour in range(0, hourly.hours()):
# 		print('Hour', hour+1)
# 		for item in hourly.get_hour(hour).keys():
# 			print(item + ' : ' + str(hourly.get_hour(hour)[item]))
# 		print
# 		# Or access attributes directly for a given minute. 
# 		# hourly.hour_5_time would also work
# 		print(hourly.hour_3_time)
# 		print()
# 	print()
# else:
# 	print('No Hourly data')

if fio.has_currently() is True:
	currently = FIOCurrently.FIOCurrently(fio)
	print('Currently')
	for item in currently.get().keys():
		print(item + ' : ' + str(currently.get()[item]))
	print()
	# Or access attributes directly
	print('current temperature: ' + str(currently.temperature))
	print('current humidity; ' + str(currently.humidity))
	print()
else:
	print('No Currently data')