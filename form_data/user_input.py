# ['season', 'yr', 'mnth', 'holiday', 'weekday', 'workingday', 'weathersit', 'temp', 'atemp', 'windspeed',
#                'qtrs']]

# This class handles user data
try:
    from application_logging.logger import App_Logger
    import pandas as pd
    from pandas.io.json import json_normalize

except ImportError as e:
    print('Import Error occured: ', e)

class user_input:
    def __init__(self,df):
        self.df = pd.DataFrame(json_normalize(df))
        self.logger = App_Logger()
        print('Data Frame is created')
        print(self.df)

    def get_user_input(self,df):
        print('User requesting for input data')
        print(df[['season', 'yr','qtrs','mnth', 'holiday', 'weekday', 'workingday', 'weathersit', 'temp', 'atemp', 'windspeed',
                ]])

        print(type(df[['season', 'yr','qtrs','mnth', 'holiday', 'weekday', 'workingday', 'weathersit', 'temp', 'atemp', 'windspeed',
                ]]))

        print('Before assigning to input variable')

        # inp = df.copy()

        return df
    # def __init__(self,season, yr, qtrs, mnth, holiday, weekday, workingday, weathersit, temp, atemp, windspeed):
    #     self.season = season
    #     self.yr = yr
    #     self.qtrs = qtrs
    #     self.mnth = mnth
    #     self.holiday = holiday
    #     self.weekday = weekday
    #     self.workingday = workingday
    #     self.weathersit = weathersit
    #     self.temp = temp
    #     self.atemp = atemp
    #     self.windspeed = windspeed
    #     self.logger = App_Logger()