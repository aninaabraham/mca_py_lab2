from WeatherAnalyzer import WeatherAnalyzer

# Sample data: list of dictionaries containing weather data
weather_data = [
    {'date': '2024-08-01', 'max_temp': 32, 'min_temp': 25, 'humidity': 60},
    {'date': '2024-08-02', 'max_temp': 30, 'min_temp': 24, 'humidity': 65},
    {'date': '2024-08-03', 'max_temp': 29, 'min_temp': 23, 'humidity': 70},
    {'date': '2024-08-04', 'max_temp': 31, 'min_temp': 26, 'humidity': 55},
    {'date': '2024-08-05', 'max_temp': 35, 'min_temp': 28, 'humidity': 50},
  
]

# Initialize the WeatherAnalyzer with the weather data
analyzer = WeatherAnalyzer(weather_data)

# Find highest and lowest temperatures
highest, lowest = analyzer.find_highest_lowest_temps()
print(f"Highest temperature: {highest}°C")
print(f"Lowest temperature: {lowest}°C")

# Count days with temperatures above 30°C
days_above_30 = analyzer.count_days_above_30()
print(f"Number of days with temperatures above 30°C: {days_above_30}")

# Compute average humidity
avg_humidity = analyzer.average_humidity()
print(f"Average humidity: {avg_humidity:.2f}%")
