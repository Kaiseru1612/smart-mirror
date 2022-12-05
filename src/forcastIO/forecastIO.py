from forecastiopy import *
# from . import apikey
import environtment_variable

BKUni = environtment_variable.BKUni
API_KEY='e2fea81b36c2588f1315c4ad2b721989'

# fio = ForecastIO.ForecastIO(api_key,
#                             units=ForecastIO.ForecastIO.UNITS_SI,
#                             lang=ForecastIO.ForecastIO.LANG_ENGLISH,
#                             latitude=BKUni[0], longitude=BKUni[1])

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

# if fio.has_currently() is True:
#     currently = FIOCurrently.FIOCurrently(fio)
#     print('Currently')
#     for item in currently.get().keys():
#         print(item + ' : ' + str(currently.get()[item]))
#     print()
#     # Or access attributes directly
#     print('current temperature: ' + str(currently.temperature))
#     print('current humidity; ' + str(currently.humidity))
#     print()
# else:
#     print('No Currently data')


class Weather:
	def __init__(self, lat, long) -> None:
		self.api_key = API_KEY
		self.location = [lat, long]
		self.temperature=0
		self.humidity=0

	def create_fio(self):
		self.fio = ForecastIO.ForecastIO(self.api_key, units=ForecastIO.ForecastIO.UNITS_SI,
						lang=ForecastIO.ForecastIO.LANG_ENGLISH, 
						latitude=self.location[0], 
						longitude=self.location[1])


	def get_current_weatherforecast(self):
		if self.fio.has_currently() is True:
			currently = FIOCurrently.FIOCurrently(self.fio)
			# print('Currently')
			# for item in currently.get().keys():
			# 	print(item + ' : ' + str(currently.get()[item]))
			# print()
        	# Or access attributes directly
			self.temperature = currently.temperature
			self.humidity  = currently.humidity
			# print('current temperature: ' + str(currently.temperature))
			# print('current humidity; ' + str(currently.humidity))
			# print()
		else:
			print('No Currently data')
