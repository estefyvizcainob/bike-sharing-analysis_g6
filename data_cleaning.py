import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------- Function definition for the data cleaning page
def data_cleaning_page():

    st.write("Welcome to the data cleaning section. Here, we ensure data quality, visualize insights, and prepare data for further analysis.")

    st.markdown(
        """
        <h1 style='color: green;'>1.1 Data Cleaning </h1>
        """,
        unsafe_allow_html=True
    )

    st.title("")
    
    # Load your data (ensure the CSV file path is correct)
    data = pd.read_csv('hour.csv')


    # --------------------- Collapsible sections for each analysis step

    # ------ Initial Data Overview
    with st.expander("See details for Initial Data Overview"):
        st.markdown(
            """
            <h2 style='color: grey;'>Initial Data Overview</h2>
            """,
            unsafe_allow_html=True
        )
        st.write("This dataset comprises hourly data for bike rentals, including weather conditions, time details, and user types. Example of data (head):")
        st.dataframe(data.head())

    # Data Quality Assessment
    with st.expander("See details for Data Quality Assessment"):
        st.markdown(
            """
            <h2 style='color: grey;'>Data Quality Assessment</h2>
            """,
            unsafe_allow_html=True
        )
        st.write("### Data Structure")
        st.write("All features are correctly typed as `int64` or `float64`, with the exception of the `dteday` column, which holds date information.")
        st.write("### Missing Values")
        st.write("No missing values were found in the dataset, ensuring high data quality.")

    # -------------- Handling Outliers
    with st.expander("See details for Handling Outliers and Ensuring Integrity"):
        st.markdown(
            """
            <h2 style='color: grey;'>Handling Outliers and Ensuring Integrity</h2>
            """,
            unsafe_allow_html=True
        )
        st.write("We verified the data for outliers using visual methods like box plots and found no extreme values that would skew our analysis.")

    # Denormalizing Data
    with st.expander("See details for Denormalizing Data for Clarity"):
        st.markdown(
            """
            <h2 style='color: grey;'>Denormalizing Data for Clarity</h2>
            """,
            unsafe_allow_html=True
        )
        st.write("""
        The features `temp`, `atemp`, `hum`, and `windspeed` were denormalized to restore their original values:
        - Temperature by 41
        - `atemp` by 50
        - Humidity by 100
        - Windspeed by 67
        """)

    # --------------- Verifying Season Behavior
    with st.expander("See details for Verifying Season Behavior"):
        st.markdown(
            """
            <h2 style='color: grey;'>Verifying Season Behavior</h2>
            """,
            unsafe_allow_html=True
        )
        st.write("""
        The dataset claims to split the data by seasons (1: Spring, 2: Summer, 3: Autumn, 4: Winter). To validate this, we verified the actual start and end dates for each season.
        
        Observations:
        - **Season 1 (Winter)**: 20 December - 20 March
        - **Season 2 (Spring)**: 21 March - 20 June
        - **Season 3 (Summer)**: 21 June - 22 September
        - **Season 4 (Autumn)**: 23 September - 19 December
        
        The min and max dates for each season in the year 2011 were as follows:
        """)

        season_data = pd.DataFrame({
            'season': [1, 2, 3, 4],
            'min_day': ['2011-01-01', '2011-03-21', '2011-06-21', '2011-09-23'],
            'max_day': ['2011-12-31', '2011-06-20', '2011-09-22', '2011-12-20']
        })
        
        st.table(season_data)

    # Missing Data in Time Series
    with st.expander("See details for Checking Missing Data in Time Series"):
        st.markdown(
            """
            <h2 style='color: grey;'>1.1.5 Checking for Missing Data in Time Series</h2>
            """,
            unsafe_allow_html=True
        )
        st.write("""
        To verify the completeness of the time series data, we checked for any missing dates or specific hourly points. Ensuring no missing points in the time series is critical for accurate modeling and analysis.
        
        During our analysis, we found that while there were no missing dates in terms of days, there were specific **date-hour combinations** missing from the dataset. This raised one of our main challenges: how to best address these 165 cases without impacting the integrity of the data.
        
        Below are some examples of these missing date-hour combinations:
        """)

        missing_date_hours = pd.DataFrame({
            'dteday': ['2011-01-02', '2011-01-03', '2011-01-03', '2011-01-04', '2011-01-05',
                       '2012-10-30', '2012-11-08', '2012-11-29', '2012-12-24', '2012-12-25'],
            'hr': [5, 2, 3, 3, 3, 12, 3, 3, 4, 3]
        })

        st.table(missing_date_hours)

    # -------- Feature Engineering
    st.markdown("---")
    st.markdown(
        """
        <h1 style='color: green;'>1.2 Feature Engineering</h1>
        <p>This section covers the additional features we engineered to enhance our analysis and model performance.</p>
        """,
        unsafe_allow_html=True
    )

    # Adding Day Variable
    with st.expander("1.2.1 Adding Day Variable from Date Column"):
        st.markdown(
            """
            <h2 style='color: grey;'>1.2.1 Adding Day Variable from Date Column</h2>
            """,
            unsafe_allow_html=True
        )
        data['day_of_month'] = pd.to_datetime(data['dteday']).dt.day
        st.table(data.head())

    # Rush Hour Variable
    with st.expander("1.2.2 Rush Hour Variable"):
        st.markdown(
            """
            <h2 style='color: grey;'>1.2.2 Rush Hour Variable</h2>
            """,
            unsafe_allow_html=True
        )
        st.write("Data retrieved from: [Commute Patterns](https://www.commuterconnections.org/wp-content/uploads/SOC-2022-At-a-Glance-Commute-Patterns.pdf)")
        st.write("""
        To better categorize the time of day, we created a new variable to segment hours into different periods:
        - 0 = Early Morning (12 AM - 6 AM)
        - 1 = Morning Rush (6 AM - 10 AM)
        - 2 = Midday (10 AM - 3 PM)
        - 3 = Evening Rush (3 PM - 7 PM)
        - 4 = Night (7 PM - 12 AM)
        """)

        def categorize_hour(hour):
            if 0 <= hour < 6:
                return 0
            elif 6 <= hour < 10:
                return 1
            elif 10 <= hour < 15:
                return 2
            elif 15 <= hour < 19:
                return 3
            else:
                return 4

        data['hour_category'] = data['hr'].apply(categorize_hour)
        st.table(data.head())

    # Rain/Snow Variable
    with st.expander("1.2.3 Rain/Snow Variable"):
        st.markdown(
            """
            <h2 style='color: grey;'>1.2.3 Rain/Snow Variable</h2>
            """,
            unsafe_allow_html=True
        )
        st.write("Where: 0 = no rain or snow | 1 = rain or snow")
        
        def categorize_weather(weathersit):
            if 1 <= weathersit < 3:
                return 0
            else:
                return 1

        data['rain_snow'] = data['weathersit'].apply(categorize_weather)
        st.table(data.head())

    # Download button for the updated dataset
    csv = data.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Updated Dataset",
        data=csv,
        file_name='updated_hour_data.csv',
        mime='text/csv',
    )

# Run






