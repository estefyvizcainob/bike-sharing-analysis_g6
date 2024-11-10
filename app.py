import streamlit as st
from data_cleaning import data_cleaning_page
from team_intro import introduction_page
from ml_model import ml_model_page
from business_insights import business_insights_page


# Custom CSS for sidebar customization
st.markdown(
    """
    <style>
    /* Sidebar background color */
    [data-testid="stSidebar"] {
        background-color: #ffeed6; /* Light purple - you can change to any color */
    }

    /* Sidebar text color */
    [data-testid="stSidebar"] .css-1d391kg {
        color: #4b0082; /* Dark purple - change to your preferred color */
    }

    /* Sidebar toggle button (if you added a custom toggle) */
    .sidebar-toggle-btn {
        background-color: #4b0082; /* Color of the button */
        color: white;
        border: none;
        padding: 8px;
        border-radius: 4px;
        cursor: pointer;
        margin: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Your existing app code
def main():
    st.sidebar.title("Menu")
    selection = st.sidebar.radio(
        "Choose a page:",
        ["Introduction", "Data Cleaning & Analysis", "ML Model Creation", "Business Insights"]
    )
    if selection == "Introduction":
        introduction_page()
    elif selection == "Data Cleaning & Analysis":
        data_cleaning_page()
    elif selection == "ML Model Creation":
        ml_model_page()
    elif selection == "Business Insights":
        business_insights_page()

if __name__ == "__main__":
    main()
