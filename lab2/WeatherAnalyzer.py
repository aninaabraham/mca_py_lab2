# WeatherAnalyzer.py

class WeatherAnalyzer:
    def __init__(self, data):
        self.data = data

    def find_highest_lowest_temps(self):
        """Find the highest and lowest temperatures recorded during the period."""
        highest_temp = max(self.data, key=lambda x: x['max_temp'])['max_temp']
        lowest_temp = min(self.data, key=lambda x: x['min_temp'])['min_temp']
        return highest_temp, lowest_temp

    def count_days_above_30(self):
        """Determine the number of days with temperatures above 30°C."""
        days_above_30 = sum(1 for day in self.data if day['max_temp'] > 30)
        return days_above_30

    def average_humidity(self):
        """Compute the average humidity over the specified period."""
        total_humidity = sum(day['humidity'] for day in self.data)
        average_humidity = total_humidity / len(self.data)
        return average_humidity
