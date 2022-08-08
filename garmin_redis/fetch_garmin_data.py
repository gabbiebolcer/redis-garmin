"""Fetch data from Garmin"""
import os
import datetime

import garminconnect


def garmin_connection():
    email = os.getenv('EMAIL')
    pw = os.getenv('PASSWORD')
    if email is None or pw is None:
        raise Exception("No email or password provided")
    gc = garminconnect.Garmin(email, pw)
    gc.login()
    return gc


def get_today_activity_data(gc):
    today = datetime.date.today().isoformat()
    today_stats = gc.get_stats(today)
    print("Today's Activities:")
    print(today_stats)


def get_heartrate_data(gc):
    today = datetime.date.today().isoformat()
    todays_heartrate = gc.get_heart_rates(today)
    print("Today's Heart Rates:")
    print(todays_heartrate)


def get_sleep_data(gc):
    today = datetime.date.today().isoformat()
    todays_sleep_data = gc.get_sleep_data(today)
    print("Today's sleep data: ")
    print(todays_sleep_data)


def fetch_all_data():
    con = garmin_connection()
    get_today_activity_data(con)
    get_heartrate_data(con)
    get_sleep_data(con)


if __name__ == '__main__':
    fetch_all_data()