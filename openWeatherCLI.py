#!/usr/bin/env python3
"""
By Mark Boutros

Simple command-line app for working with the OpenWeather API.

Features:
- Search for current weather for a city
- Add a city to favourites (max 3)
- List favourite cities with current weather
- Update favourites by removing and adding cities

"""

import os
import sys
import requests

# URL for openWeather API
API_BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


class WeatherApp:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.favourites: list[str] = []

        # Units: "metric" (Celsius, m/s) or "imperial" (Fahrenheit, mph) Allows switching between units.
        self.units = "metric"
        self.temp_unit_label = "°C"
        self.wind_unit_label = "m/s"

    def fetch_weather(self, city: str) -> dict | None:
        """Call OpenWeather API and return JSON data for the given city."""
        params = {
            "q": city,
            "appid": self.api_key,
            "units": self.units,  # use current unit setting
        }

        #Call API, Handle exceptions
        try:
            response = requests.get(API_BASE_URL, params=params, timeout=5)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"\nError calling OpenWeather API: {e}")
            return None

        data = response.json()
        #if API returns and code which is not "200 - good"
        if str(data.get("cod")) != "200":
            message = data.get("message", "Unknown error from API")
            print(f"\nAPI error for city '{city}': {message}")
            return None

        return data


    def display_weather(self, data: dict) -> None:
        """Print a short summary of the weather, including wind, with current units."""
        name = data.get("name", "Unknown location")
        main = data.get("main", {})
        weather_list = data.get("weather", [])
        wind = data.get("wind", {})

        description = weather_list[0].get("description", "N/A") if weather_list else "N/A"  #classical descriptions of weather
        temp = main.get("temp", "N/A")  #current temp of current city
        feels_like = main.get("feels_like", "N/A")  #compound measure of temp, humidity, and other factors
        humidity = main.get("humidity", "N/A")  #air moisture measure

        wind_speed = wind.get("speed", "N/A")    # units depend on self.units
        wind_deg = wind.get("deg")  #wind direction in degrees (should investigate cardinal direction mappings)
        wind_gust = wind.get("gust")  #wind speed peaks

        #format output for human consumption
        print(f"\nWeather for {name}:")
        print(f"  Description : {description}")
        print(f"  Temperature : {temp} {self.temp_unit_label} (feels like {feels_like} {self.temp_unit_label})")
        print(f"  Humidity    : {humidity}%")

        wind_line = f"  Wind        : {wind_speed} {self.wind_unit_label}"
        if wind_deg is not None:
            wind_line += f", {wind_deg}°"
        if wind_gust is not None:
            wind_line += f" (gusts up to {wind_gust} {self.wind_unit_label})"
        print(wind_line)

    def search_city_weather(self) -> None:
        """Ask user for a city and show its weather."""
        city = input("\nEnter city name: ").strip()
        if not city:
            print("No city entered.")
            return

        data = self.fetch_weather(city)
        if data:
            self.display_weather(data)

    def add_favourite(self) -> None:
        """Add a city to favourites, respecting the max of 3."""
        city = input("\nEnter city name to add to favourites: ").strip()
        if not city:
            print("No city entered.")
            return

        if city in self.favourites:
            print(f"'{city}' is already in favourites.")
            return

        if len(self.favourites) >= 3:
            print("\nYou already have 3 favourite cities:")
            self.list_favourites_names()
            print("To add a new one, remove an existing favourite first.")
            self.update_favourites()
            # After update, check again
            if len(self.favourites) >= 3:
                print("Favourites list is still full. Cannot add a new city right now.")
                return

        self.favourites.append(city)
        print(f"Added '{city}' to favourites.")

    def list_favourites_names(self) -> None:
        """List favourite city names only."""
        if not self.favourites:
            print("\nNo favourite cities yet.")
            return

        print("\nFavourite cities:")
        for index, city in enumerate(self.favourites, start=1):
            print(f"  {index}. {city}")

    def list_favourites_with_weather(self) -> None:
        """List favourite cities and show current weather for each."""
        if not self.favourites:
            print("\nNo favourite cities yet.")
            return

        print("\nFavourite cities with current weather:")
        for city in self.favourites:
            data = self.fetch_weather(city)
            if data:
                self.display_weather(data)

    def update_favourites(self) -> None:
        """
        Allow the user to remove a favourite city.

        The spec mentions updating favourites by removing and adding cities,
        so this function handles removing one city.
        """
        if not self.favourites:
            print("\nNo favourite cities to update.")
            return

        self.list_favourites_names()
        choice = input("\nEnter the number of the city to remove (or press Enter to cancel): ").strip()
        if not choice:
            print("No changes made.")
            return

        try:
            index = int(choice)
        except ValueError:
            print("Invalid choice.")
            return

        if 1 <= index <= len(self.favourites):
            removed = self.favourites.pop(index - 1)
            print(f"Removed '{removed}' from favourites.")
        else:
            print("Choice out of range.")

    def toggle_units(self) -> None:
        """Toggle between metric and imperial units."""
        if self.units == "metric":
            self.units = "imperial"
            self.temp_unit_label = "°F"
            self.wind_unit_label = "mph"
            print("\nUnits set to imperial (Fahrenheit, mph).")
        else:
            self.units = "metric"
            self.temp_unit_label = "°C"
            self.wind_unit_label = "m/s"
            print("\nUnits set to metric (Celsius, m/s).")

    #input loop section
    def main_loop(self) -> None:
        """Main menu loop."""
        while True:
            print("\n--- Weather App Menu ---")
            print(f"(Current units: {self.units})")
            print("1. Search for weather details of a city")
            print("2. Add a city to favourites")
            print("3. List favourite cities with current weather")
            print("4. Update favourites (remove a city)")
            print("5. List favourite cities (names only)")
            print("6. Toggle units (metric/imperial)")
            print("0. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.search_city_weather()
            elif choice == "2":
                self.add_favourite()
            elif choice == "3":
                self.list_favourites_with_weather()
            elif choice == "4":
                self.update_favourites()
            elif choice == "5":
                self.list_favourites_names()
            elif choice == "6":
                self.toggle_units()
            elif choice == "0":
                print("Goodbye.")
                break
            else:
                print("Unknown choice, please try again.")

#secret key mgmt
def get_api_key() -> str:
    """
    Get OpenWeather API key from environment or user input.
    This keeps the key out of source control by default.
    """
    key = os.getenv("OPENWEATHER_API_KEY")
    if key:
        return key.strip()

    key = input("Enter your OpenWeather API key: ").strip()
    if not key:
        print("An API key is required to run this application.")
        sys.exit(1)
    return key

#classic main function
def main() -> None:
    api_key = get_api_key()
    app = WeatherApp(api_key)
    app.main_loop()


if __name__ == "__main__":
    main()
