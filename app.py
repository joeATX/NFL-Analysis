import streamlit as st
import joblib
import pandas as pd

# Load my notebook data
model = joblib.load('random_forest_model.pkl')

st.title("NFL App")

# Example function to make predictions
def predict(input_data):
    return model.predict(input_data)

# Streamlit UI
st.title('NFL Game Predictor')

team_name = st.text_input('Enter Team Name:')
season = st.number_input('Season:', min_value=2020, max_value=2024, value=2024)
yards_away = st.number_input('Yards Away:', min_value=0, value=100)
yards_home = st.number_input('Yards Home:', min_value=0, value=120)
pass_yards_away = st.number_input('Pass Yards Away:', min_value=0, value=250)
pass_yards_home = st.number_input('Pass Yards Home:', min_value=0, value=300)
turnovers_away = st.number_input('Turnovers Away:', min_value=0, value=2)
turnovers_home = st.number_input('Turnovers Home:', min_value=0, value=1)
third_down_away = st.number_input('Third Down Away:', min_value=0, value=5)
third_down_home = st.number_input('Third Down Home:', min_value=0, value=3)
fourth_down__home = st.number_input('Fourth Down Home:', min_value=0, value=2)
fourth_down__away = st.number_input('Fourth Down Away:', min_value=0, value=1)
pass_percentage_away = st.slider('Pass Percentage Away:', min_value=0.0, max_value=1.0, value=0.65)
pass_percentage_home = st.slider('Pass Percentage Home:', min_value=0.0, max_value=1.0, value=0.70)
rush_avg_away = st.number_input('Rush Avg Away:', min_value=0.0, value=4.5)
rush_avg_home = st.number_input('Rush Avg Home:', min_value=0.0, value=4.0)
week_cleaned = st.number_input('Week Cleaned:', min_value=1, value=1)
home_encoded = st.number_input('Home Encoded (1 for home, 0 for away):', min_value=0, max_value=1, value=1)
away_encoded = st.number_input('Away Encoded (1 for away, 0 for home):', min_value=0, max_value=1, value=0)

# Prepare the input data
input_data = {
    'season': [season],
    'yards_away': [yards_away],
    'yards_home': [yards_home],
    'pass_yards_away': [pass_yards_away],
    'pass_yards_home': [pass_yards_home],
    'turnovers_away': [turnovers_away],
    'turnovers_home': [turnovers_home],
    'third_down_away': [third_down_away],
    'third_down_home': [third_down_home],
    'fourth_down__home': [fourth_down__home],
    'fourth_down__away': [fourth_down__away],
    'pass_percentage_away': [pass_percentage_away],
    'pass_percentage_home': [pass_percentage_home],
    'rush_avg_away': [rush_avg_away],
    'rush_avg_home': [rush_avg_home],
    'week_cleaned': [week_cleaned],
    'home_encoded': [home_encoded],
    'away_encoded': [away_encoded]
}

input_df = pd.DataFrame(input_data)

# Make prediction
if st.button('Predict Outcome'):
    prediction = model.predict(input_df)
    st.write(f'The predicted outcome for {team_name} is: {"Home Win" if prediction[0] == 1 else "Away Win"}')