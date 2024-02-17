# Electric Car Data Analysis and Visualization

This Python program analyzes and visualizes electric car data using the Pandas, Matplotlib, and Seaborn libraries. The program explores various aspects of electric cars such as brand distribution, speed, efficiency, and acceleration.

## Data Source
The electric car dataset used in this project is obtained from [source](https://www.kaggle.com/datasets/geoffnel/evs-one-electric-vehicle-dataset), containing information on electric car brands, models, specifications, and performance metrics.

## Libraries Used
- Pandas: For data manipulation and analysis.
- Matplotlib: For creating static visualizations in Python.
- Seaborn: For enhancing the aesthetics of Matplotlib plots.

## Flow of the Program

### 1. Data Loading
The program reads the electric car dataset from a CSV file into a Pandas DataFrame.

### 2. Data Cleaning and Preprocessing
- Duplicate rows are removed from the dataset.
- Column names are standardized and units are stripped for specific columns.
- Values are replaced and data types are converted as necessary.

### 3. Data Visualization
The program generates various visualizations to analyze electric car data:

#### Bar Plot (Top 10 Brands with the Most Number of Electric Cars)
- Shows the distribution of electric cars among the top 10 brands based on the number of models.
- X-axis: Brand
- Y-axis: Number of Electric Cars

#### Bar Plot (Top 5 Fastest Electric Cars)
- Displays the top 5 fastest electric cars based on their maximum speed.
- X-axis: Speed (km/h)
- Y-axis: Car Model

#### Bar Plot (Top 5 Efficient Electric Cars)
- Illustrates the top 5 most efficient electric cars based on energy consumption.
- X-axis: Efficiency (Wh/km)
- Y-axis: Car Model

#### Scatter Plot (Acceleration vs. Top Speed of Electric Vehicles)
- Visualizes the relationship between acceleration and top speed of electric vehicles.
- X-axis: Acceleration (seconds)
- Y-axis: Top Speed (km/h)

#### Histogram (Distribution of Acceleration of Electric Vehicles)
- Shows the distribution of acceleration among electric vehicles.
- X-axis: Acceleration (seconds)
- Y-axis: Frequency

#### Histogram (Distribution of Top Speed of Electric Vehicles)
- Illustrates the distribution of top speed among electric vehicles.
- X-axis: Top Speed (km/h)
- Y-axis: Frequency

## Running the Program
To run the program:
1. Ensure you have Python installed on your system.
2. Install the required libraries using `pip install pandas matplotlib seaborn`.
3. Download the electric car dataset and save it as "ElectricCarData.csv" in the same directory as the script.
4. Run the Python script.

## Output
The program generates visualizations depicting various aspects of electric cars, providing insights into their distribution, performance, and efficiency.
