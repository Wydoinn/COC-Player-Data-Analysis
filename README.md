# Clash of Clans Player Data Analysis

![banner](https://github.com/user-attachments/assets/00231982-6c1e-4fd6-8d77-884b7647f9a4)

This project analyzes a dataset of Clash of Clans player and clan data to uncover insights into player behavior, performance, and clan dynamics. The analysis uses Python libraries like Pandas, Matplotlib, Seaborn, and SciPy to explore various aspects of the game, including:

* **Player Performance:** Trophy distribution, top players, experience levels, war stars.
* **Clan Performance:** Top clans by average trophies and war stars, clan member distribution.
* **Donations:** Most generous players, donation ratios.
* **League Distribution:** Player distribution across different leagues.
* **Town Hall Levels:** Distribution of players across town hall levels.
* **Statistical Tests:** T-tests and ANOVA to compare performance across different groups.

## Data Source

The data used in this analysis was obtained through the Clash of Clans API and processed using a Python script. The script retrieves clan and player data, handles API rate limits, and saves the results to a CSV file.

## Key Findings

* **Top Clans:** Identified the top-performing clans based on average trophies and total war stars.
* **Top Players:** Highlighted the top individual players by trophy count and war stars.
* **Generous Players:** Recognized players with the highest donations and donation ratios.
* **Town Hall Distribution:** Analyzed the distribution of players across different town hall levels.
* **League Performance:** Calculated the average trophy count for each league.
* **Correlation:** Found a positive correlation between player experience level and trophy count.
* **Perfect Win Ratios:** Identified players with perfect attack/defense win ratios.

## Analysis Techniques

The analysis utilizes various techniques, including:

* **Descriptive Statistics:** Mean, median, standard deviation, percentiles.
* **Data Visualization:** Histograms, scatter plots, box plots, bar charts, pie charts.
* **Correlation Analysis:** Examining relationships between variables.
* **Statistical Tests:** T-tests and ANOVA to compare performance across different groups.

## Usage

To run the analysis:

1. **Install Dependencies:** Ensure you have the necessary Python libraries installed. You can install them using `pip install pandas matplotlib seaborn scipy`.
2. **Download Data:** Download the `Clan_and_Player_Details.csv` file.
3. **Run the Script:** Execute the Python script provided in this repository.

## Conclusion

This analysis provides valuable insights into the Clash of Clans player base and the factors contributing to success in the game. The findings can be used by players to improve their strategies, by clans to recruit effectively, and by game developers to understand player behavior and potentially make adjustments to the game.
