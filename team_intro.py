import streamlit as st

def introduction_page():
    # Add custom CSS for background color, title font, subtitle color, and font size for team member names
    st.markdown(
        """
        <style>
        .main {
            background-color: #e6f7e6; /* light green */
        }
        h1 {
            font-family: 'Verdana', sans-serif;
            font-size: 50px;
            color: #004d00; /* Dark green color for the main title */
            text-align: center; /* Center the main title */
        }
        h2 {
            color: #555555; /* Gray color for subtitles */
        }
        .member-name {
            font-size: 20px; /* Adjust the size to your preference */
            color: #333333; /* Dark grey for contrast */
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Page content
    st.title("Group Assignment - Bike Sharing")
    st.image("bike.jpg", use_column_width=True)

    st.subheader("Introduction")
    st.write("""
    The administration of Washington D.C. aims to better understand the bike-sharing service usage and improve its provision.
    This dashboard provides an in-depth analysis and predictive modeling using bike-sharing data from 2011 and 2012.
    """)

    st.subheader("Team Members:")
    
    team_members = [
        #{"name": "Matteo Becchis", "image_path": "images/matteo.jpg"},
        {"name": "James Dieter Clayfield", "image_path": "james.jpg"},
        #{"name": "Tom Jansen", "image_path": "images/tom.jpg"},
        #{"name": "Yousef Rimawi", "image_path": "images/yousef.jpg"},
        #{"name": "Luke Mercouris", "image_path": "images/luke.jpg"},
        {"name": "Estefanía Vizcaíno Bickford", "image_path": "estefy.jpg"},
    ]
    
    for member in team_members:
        col1, col2 = st.columns([1, 1])
        with col1:
            st.image(member["image_path"], width=300)
        with col2:
            st.markdown(f"<p class='member-name'><strong>{member['name']}</strong></p>", unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)  # To avoid text overlap over the picture



