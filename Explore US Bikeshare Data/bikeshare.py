import time
import pandas as pd
import numpy as np
from datetime import datetime
from datetime import timedelta

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or  "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True: 
        city = input("Please enter the name of the city you wish to analyze the data: ").lower()
        if city not in ('chicago', 'new york city', 'washington'):
            print("Invalid city, Please try a valid city for this program.")
            continue
        else:
            break
    
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Please choose the name of the month you wish to filter the data or select 'all' to view all months data: ").lower()
        if month not in ('all','january', 'february', 'march','april','may', 'june', 'july', 'august','september','october','november','december'):
            print("Invalid month, Please try again")
            continue
        else:
             break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Please choose the name of the day of week you wish to filter the data or select 'all' to view all days data: ").lower()
        if day not in ('all','monday', 'tuesday', 'wednesday','thrusday','friday', 'saturday', 'sunday'):
            print("Invalid option for day of week, please try again")
            continue
        else:
             break         
    
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
    #try:
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june','july', 'august','september','october','november','december']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
        if day != 'all':
        # filter by day of week to create the new dataframe
            df = df[df['day_of_week'] == day.title()]
   
    #except IndexError:
    #    print("Your input has no derived no outputs. Please try another month and day combination! :)")
    #    continue
    return df
    
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    months = ['january', 'february', 'march', 'april', 'may', 'june','july', 'august','september','october','november','december']
    common_month = months[common_month -1]    
    print("The most common month is:", common_month.title())
    
    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]   
    print("The most common day is:", common_day.title())   

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]   
    print("The most common hour is:", common_hour) 
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df.groupby('Start Station')['Start Station'].count().idxmax()
    print("Most commonly used start station is: ",common_start_station)
    
    # TO DO: display most commonly used end station
    common_end_station = df.groupby('End Station',sort=True)['End Station'].count()
    #print(common_end_station.sort_values(ascending=False))
    common_end_station = common_end_station.idxmax()
    print("Most commonly used end station is: ",common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    common_both = df.groupby(['Start Station', 'End Station']).size().nlargest(1).reset_index(name='count')
    print("\nMost common combination of start station:\n", common_both[['Start Station','End Station']])
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_travel_time = df['Trip Duration'].sum()
    print('\nTotal time travel is:\n',timedelta(seconds = int(Total_travel_time)))
    
    # TO DO: display mean travel time
    Mean_travel_time = df['Trip Duration'].mean()
    print('\nMean travel time is:\n',timedelta(seconds = int(Mean_travel_time)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("\nThese are the different types of users that use the bikes:\n" ,user_types)
      
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def age_stats(df):
    """Displays statistics on bikeshare user gender."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
     
    # TO DO: Display counts of gender
    gender_type = df['Gender'].value_counts()
    print("\nThese are the counts of users based on gender:\n" ,gender_type)
    
    # TO DO: Display earliest, most recent, and most common year of birth
    most_recent_birth_year = df['Birth Year'].max()
    print("\nThe youngest persont to ride the bike was born in:\n",int(most_recent_birth_year))
    
    earliest_birth_year = df['Birth Year'].min()
    print("\nThe oldest person to ride the bike was born in:\n",int(earliest_birth_year))
    
    common_year_birth = df['Birth Year'].mode()
    print("\nThe bike is commonly ridden by people born in:\n",int(common_year_birth))
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        #print(df)
        if not df.empty:
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            if city in ('chicago','new york city'):
                age_stats(df)
        else:
            print("No data for the options chosen")
            
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
