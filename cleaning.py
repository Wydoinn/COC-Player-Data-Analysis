import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('datasets/player_details.csv')

# Remove rows with missing values in role, name, league, and builderBaseLeague columns
df.dropna(subset=['role', 'name', 'league', 'builderBaseLeague'], inplace=True)

# Save the updated DataFrame back to the CSV file
df.to_csv('datasets/player_details_clean.csv', index=False)