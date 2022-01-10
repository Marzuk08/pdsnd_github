import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # Get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        print(['Chicago','New york city','Washington'])
        city = input("Which city from the list of cities do you want to analyze? \n").lower()

        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print("Sorry!, you have entered wrong input. Please try again.\n")
    # Get user input for month (all, january, february, ... , june)
    while True:
        print(['january', "february", "march", "april", "may", "june"])

        month = input("Enter a month from the list of months to explore, type 'all' to explore all months. \n").lower()

        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break
        else:
            print("Sorry!, you have entered wrong input. Please try again.")
    # Get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        print(["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"])
        day = input("Enter day from the list of days to explore, type 'all' for all days \n").lower()

        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            break
        else:
            print("Sorry!, you have entered wrong input. Please try again.")
    print('<>'*40)
    return city, month, day

# Load data
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
     # Read city data into pandas dataframe
    df = pd.read_csv(CITY_DATA[city])

    # Changing Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Creating month column from Start Time column
    df['month'] = df['Start Time'].dt.month

    # Creating Day Of Week column from Start Time column
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # Creating a new dataframe for specific month if selected
    if month != 'all':
        # using the index of the months list to get the corresponding int
        months_list = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months_list.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # #Creating a new dataframe for specific day if selected
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    print("most common month is: {}\n".format(df['month'].mode()[0]))

    # Display the most common day of week
    print("most common day of week  is: {}\n ".format(df['day_of_week'].mode()[0]))

    # Display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("most common start hour is: {}\n ".format( df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('<>'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    print("The most commonly used start station is {}\n ".format( df['Start Station'].mode()[0]))

    # Display most commonly used end station
    print("The most commonly used end station is {}\n".format( df['End Station'].mode()[0]))

    # Display most frequent combination of start station and end station trip
    df['Most Frequent Combination'] = df['Start Station'] + " " + df['End Station']
    print("The most frequent combination of start station and end station trip is: ", df['Most Frequent Combination'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('<>'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    print("The total travel time is {} seconds \n".format( df['Trip Duration'].sum()))

    # Display mean travel time
    print("The mean travel time is {} seconds \n".format( df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("User Types\n", user_types, "\n")
    if city != 'washington':
        # Display counts of gender
        gender = df['Gender'].value_counts()
        print(gender, '\n')
        # Display earliest, most recent, and most common year of birth
        mr_yob = df['Birth Year'].max()
        print("The most recent year of birth is {}\n".format(mr_yob))

        e_yob = df['Birth Year'].min()
        print("The earliest year of birth is {}\n ".format(e_yob))

        mc_yob = df['Birth Year'].mode()[0]
        print("The most common year of birth is {}\n".format(mc_yob))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('<>'*40)
    i = 1
    while True:
        raw_data = input('\nWould you like to disply five lines of raw data? Enter yes or no.\n')
        if raw_data.upper() == 'YES':
            print(df[i:i+5])
            i = i+5
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.upper() != 'YES':
            break


if __name__ == "__main__":
	main()
