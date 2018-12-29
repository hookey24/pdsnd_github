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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print('Choose a city')
    city = input().lower()
    
    while CITY_DATA.get(city) is None:
        print('Incorrect city name, try again')
        city = input().lower()
    

    # TO DO: get user input for month (all, january, february, ... , june)
    Months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    print('Choose a month, or type all')
    month = input()
    
    while month not in Months:
        print('Incorrect month name, try again')
        month = input()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    Dows = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    print('Choose a day, or type all')
    day = input()
    
    while day not in Dows:
        print('Incorrect day name, try again')
        day = input()    
    
    

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
    filename = CITY_DATA[city]
    df = pd.read_csv(filename)
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    if month != 'all':
        df['Month'] = df['Start Time'].dt.month                             #Create Month column in dataframe
        Months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = Months.index(month) + 1
        df = df[df['Month'] == month]
        #print('month success: ' + str(month))
    
    if day != 'all':
        df['Day'] = df['Start Time'].dt.weekday_name
        df = df[df['Day'] == day.title()]
        #print('Day success: ' + day)
    
    

    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    Months = ['january', 'february', 'march', 'april', 'may', 'june']
    # TO DO: display the most common month
    if month == 'all':
        
        df['Month'] = df['Start Time'].dt.month
        most_common_month = df['Month'].mode()[0]
        print('The most common month is: ' + Months[most_common_month - 1].title())
        
    else:
        print('The current month is: ' + month.title())

    # TO DO: display the most common day of week
    if day == 'all':
        df['Day'] = df['Start Time'].dt.weekday_name
        print('The most common day is: ' + str(df['Day'].mode()[0]))
    else:
        print('The current day is: ' + day.title())


    # TO DO: display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    print('The most common start hour is: ' + str(df['Hour'].mode()[0]))
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most common start station is: ' + str(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print('Most common end station is: ' + str(df['End Station'].mode()[0]))


    # TO DO: display most frequent combination of start station and end station trip
    df['Start-End Stations'] = df['Start Station'] + ' - ' + df['End Station']
    print('The most common frequent combonation of start and end stasions is: ' + str(df['Start-End Stations'].mode()[0]))
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time is: ' + str(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print('The mean travel time is: ' + str(df['Trip Duration'].mean()))
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if city != 'washington':
        print('The number of user types are:\n' + str(df['User Type'].value_counts()) + '\n')
    else:
        print('The type of users are not recorded in ' + city.title())


    # TO DO: Display counts of gender
    if city != 'washington':
        print('The number of genders are the following:\n' + str(df['Gender'].value_counts()))
    else:
        print('Gender is not recorded in ' + city.title())

    # TO DO: Display earliest, most recent, and most common year of birth
    #df['Birth of Year'] = df.to_datetime(df['Birth of Year'])
    if city != 'washington':
        print('Youngest person\'s birth year is: ' + str(df['Birth Year'].max()))
        print('Oldest person\'s birth year is: ' + str(df['Birth Year'].min()))
        print('The average person\'s birth year is: ' + str(df['Birth Year'].mean()))
    else:
        print('Year of birth is not recorded in ' + city.title())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
