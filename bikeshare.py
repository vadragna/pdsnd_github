import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': './chicago.csv',
              'new york city' : './new_york_city.csv',
              'washington': './washington.csv' }

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    city = input("From which city you wish to get the data, you can choose between 'chicago', 'new york city' and 'washington': ").lower()
    while city != 'chicago' and city != 'new york city' and city != 'washington':
      print("Please insert 'chicago', 'new york city' or 'washington', no any other value")
      city = input("From which city you wish to get the data: ")
    print('Thanks for selecting the city: ', city)

    month = input("For which month you wish to get the data? Insert 'jan', 'feb', 'mar', 'apr', 'may' or 'jun'. If you wish to have the whole data independently from the month, instert 'all' ").lower()
    while month != 'jan' and  month != 'feb' and month != 'mar' and month != 'apr' and month != 'may' and month != 'jun' and month != 'all':
        print("Please insert 'jan', 'feb' or 'mar', 'apr', 'may', 'june' or 'all' no any other value")
        month = input("For which city you wish to get the data? Insert 'jan', 'feb', 'mar', 'apr', 'may' or 'jun'. If you wish to have the whole data independently from the month, instert 'all' ")
    print('Thanks for selecting the month: ', month)

    day = input("From which day you wish to get the data? Insert 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', or If you wish to have the whole data independently from the month, instert 'all' ").lower()
    while day != 'monday' and  day != 'tuesday' and day != 'wednesday' and  day != 'thursday' and  day != 'friday' and  day != 'saturday' and day != 'sunday' and  day != 'all':
        print("Please insert 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday' or 'all' no any other value")
        day = input("From which day you wish to get the data? Insert 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', or all If you wish to have the whole data independently from the month, instert 'all' ")
    print('Thanks for selecting the day: ', day)

    print('-'*40)
    return city, month, day

def load_data(city, month, day):

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    Days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    Months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('Most Popular Start Month:', Months[popular_month - 1])

    df['day_of_week'] = df['Start Time'].dt.dayofweek
    popular_day = df['day_of_week'].mode()[0]
    print('Most Popular Start day:', Days[popular_day])

    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    print("The most common start station is:", df['Start Station'].mode()[0])

    print("The most common end station is:", df['End Station'].mode()[0])

    df2 = "From " + df['Start Station'] + " to " + df['End Station']
    print('the most common combination is: ', df2.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    print('The total travel time is: ', df['Trip Duration'].sum())

    print("The avarege travel time is: ",df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    print("the user types distribution is the following: ", df['User Type'].value_counts())

    try:
        print('df(gender)', df['Gender'])
        print("the gender distribution is the following: ", df['Gender'].value_counts())
    except:
        print('No Gender data')

    try:
        print("the youngest user was bon in ", int(df['Birth Year'].max()))
        print("the eldest user was bon in ", int(df['Birth Year'].min()))
        print("the commonest year of birth of the users was ", int(df['Birth Year'].mode()[0]))
    except:
        print('No Age data')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def get_input():
    user_input = input('Do you wish to see 5 rows of row data? Insert y or n ')
    if user_input == 'y':
        return True
    elif user_input == 'n':
        return False
    else:
        print('Please insert y for yes and n for no, no any other values')
        get_input()


def main():
    first_row = 0
    last_row = 5


    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        while get_input() == True:
            print(df[first_row:last_row])
            first_row = first_row + 5
            last_row = last_row + 5


        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
