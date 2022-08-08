"""Fetch data from Garmin"""
import os
import datetime

import click
import garminconnect

from garmin_redis import redis_helpers


def garmin_connection():
    """Creates connection to Garmin Connect.
    
    Username and Password should be set to environment variables.

    #TODO find better way to do this
    """
    email = os.getenv('EMAIL')
    pw = os.getenv('PASSWORD')
    if email is None or pw is None:
        raise Exception("No email or password provided")
    gc = garminconnect.Garmin(email, pw)
    gc.login()
    return gc


def fetch_todays_data(read_only):
    """Fetch today's Garmin data. 

    This data should include some basic info about steps, sleep, body battery,
    heart rate, and any activities done today.


    Parameters:
    -----------
        read_only (bool): if true, commit results to db
    
    """
    garmin_con = garmin_connection()
    today = datetime.date.today()
    data_to_fetch = {
        'User Stats': garmin_con.get_stats,
        'Sleep': garmin_con.get_sleep_data,
        'Heart Rate': garmin_con.get_heart_rates,
        'Activities': garmin_con.get_user_summary,
    }
    for dtype, func in data_to_fetch.items():
        print(f"Fetching todays {dtype}")
        stats = func(today)
        if not read_only:
            data = {f"{today} {dtype}": stats}
            redis_helpers.redis_commit(data=data)

@click.command()
@click.option('--readonly', '-R', is_flag=True, default=False, help="Don't commit results to redis db.")
def cli(readonly):
    fetch_todays_data(readonly)

if __name__ == '__main__':
    cli()
