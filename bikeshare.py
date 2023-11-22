import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        cities = ['chicago', 'new york city', 'washington']
        city = input(
            'Would you like to see data for chicago, new york city or washington\n').lower()
        if city in cities:
            break
        else:
            print(
                'This is not a valid city. Please enter either chicago, new york city or washington')

    # get user input for month (all, january, february, ... , june)
    while True:
        months = ['january', 'february', 'march',
                  'april', 'may', 'june', 'all']
        month = input(
            'Which month would you like to filter the data by?\nPlease enter from january - june or all\n').lower()
        if month != 'all' and month in months:
            break
        else:
            print('This is not a valid month. Please enter a month from january - june')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        days = ['sunday', 'monday', 'tuesday', 'wednesday',
                'thursday', 'friday', 'saturday', 'all']
        day = input(
            'Which day of the week would you like to filter the data by?\nPlease enter from sunday - saturday\n').lower()
        if day != 'all' and day in days:
            break
        else:
            print('This is not a valid day. Please enter a day from sunday - saturday\n')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def display_first_five(df):

    index = 0
    first_five = input(
        'Would you like to display the first five rows of the bikeshare data? Yes/No: ').lower()
    pd.set_option('display.max_columns', None)

    while True:
        if first_five == 'No':
            break
        print(df[index:index+5])
        next_five = input(
            'Would you like to display the next five rows of the bikeshare data? Yes/No: ').lower()
        index += 5


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    polular_month = df['month'].mode()[0]
    print('The most common month is: ', polular_month)

    # display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('The most common day of week is: ', popular_day_of_week)

    # display the most common start hour
    popular_start_hour = df['Start Time'].dt.hour.mode()[0]
    print('The most common start hour is: ', popular_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('The most common start station is: ', popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('The most common end station is: ', popular_end_station)

    # display most frequent combination of start station and end station trip
    popular_start_end_station = df['Start Station'] + \
        '-' + df['End Station'].mode()[0]
    print('The most common start hour and end station trip is: ',
          popular_start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is: ', total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time is: ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The counts of user types is: ', user_types)

    # Display counts of gender
    if ('Gender' in df):
        gender = df['Gender'].value_counts()
        print('The counts of gender is: ', gender)

    # Display earliest, most recent, and most common year of birth
    if ('Birth Year' in df):
        earliest_year_of_birth = df['Birth Year'].min()
        print('The earliest year of birth is: ', earliest_year_of_birth)

        most_recent_year_of_birth = df['Birth Year'].max()
        print('The most recent year of birth is: ', most_recent_year_of_birth)

        most_common_year_of_birth = df['Birth Year'].value_counts()
        print('The most common year of birth is: ', most_common_year_of_birth)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_first_five(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
