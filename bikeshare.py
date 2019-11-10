import time
import pandas as pd

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

    # Get user input for city (chicago, new york city, washington).
    # Using a while loop to handle invalid inputs
    city = input('Choose city from the list (chicago, new york city, washington): ')
    while city != 'chicago' and city != 'new york city' and city != 'washington':
        print('Try again !\nPlease enter correct city to analyze (choose from the list and small letters) !')
        city = input('Choose city from the list (chicago, new york city, washington):')

    # Get user input for month (all, january, february, ... , june)
    month = input('Enter (all) or choose month from the list (january, february, march, april, may, june): ')
    while month != 'all' and month != 'january' and month != 'february' and month != 'march' and month != 'april' and month != 'may' and month != 'june':
        print('WRONG MONTH ! ! \nPlease enter correct month (choose from the list and small letters) !')
        month = input('Enter (all) or choose the month from the list (january, february, March, April, May, june): ')

    # Get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Enter (all) or choose a day of week (monday, tuesday, ... sunday): ')
    while day != 'all' and day != 'sunday' and day != 'monday' and day != 'tuesday' and day != 'wednesday' and day != 'thursday' and day != 'friday' and day != 'saturday':
        print('Try again with small letters !')
        day = input('Enter (all) or choose a day of week (monday, tuesday, ... sunday): ')

    print('-' * 40)
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
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Display the most common month
    df['month'] = df['Start Time'].dt.month
    month = df['month'].mode()[0]
    print('Month:', month)

    # Display the most common day of week
    df['day'] = df['Start Time'].dt.weekday_name
    day = df['day'].mode()[0]
    print('Day:', day)

    # Display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station

    print('Start ', df['Start Station'].value_counts().head(1))

    # Display most commonly used end station
    print('End ', df['End Station'].value_counts().head(1))

    # Display most frequent combination of start station and end station trip
    df['Popular Trip'] = df['Start Station'] + ' , ' + df['End Station']
    print('Trip: (', df['Popular Trip'].value_counts().head(1), ')')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    print('Total Duration: ', df['Trip Duration'].sum())
    # Display mean travel time
    print('Avg Duration: ', df['Trip Duration'].sum() / df['Trip Duration'].count())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

























def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        answer = input('Do you want to see first look to data before analyze? (yes OR no) ')
        NumOfRows = 0
        while answer:
            # Display first look of the data before analyze
            if answer == 'yes':
                print(df.iloc[NumOfRows:NumOfRows+5])
                NumOfRows += 5
                answer = input('Do you want to see first look to data before analyze? (yes OR no) ')
            elif answer == 'no':
                print('Now we will work on analyzing the data in period you choose')
                break
            else:
                print('Please Enter (yes) or (no)')
                answer = input('Do you want to see first look to data before analyze? (yes OR no) ')
        # Call the functions to do analyzing
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
