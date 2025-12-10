# RDKAcademyAssessment
Open Weather CLI app and SortAndFindMedian scripts
# Weather CLI – Coding Activity 1

This repository contains my solution for **Coding Activity 1** of the RDK Academy assessment.

The application is a simple command-line tool that interacts with the **OpenWeather** API to manage and view weather details for cities.

---

## Features

The app implements all requested functionality:

1. **Search for weather details of a city**  
   - Enter a city name and see current conditions using the OpenWeather API.

2. **Add a city to favourites (max 3)**  
   - Store up to three favourite cities in memory for quick access.

3. **List favourite cities with current weather**  
   - For each favourite city, the app fetches and displays current weather info.

4. **Update favourite cities**  
   - Remove a favourite city and add another, while enforcing the limit of three.

5. **List favorite cities (names only)**  
   - List simply the names of the cities saved as favorites.

6. **Unit toggling (extra)**  
   - Toggle between **metric** (°C, m/s) and **imperial** (°F, mph) units.

---

## Tech Stack

- **Language:** Python 3.x  
- **HTTP client:** `requests`  
- **API:** [OpenWeather – Current Weather Data](https://openweathermap.org/current)

---

## Setup

1. **Clone or download** this repository.

2. **Install dependencies** (preferably in a virtual environment):

   ```bash
   pip install -r requirements.txt

3. **Obtain an OpenWeather API key**

   - Create a free account on [OpenWeather](https://home.openweathermap.org/users/sign_up).
   - After logging in, generate an API key from your account dashboard.

4. **Provide the API key**

   You can either:

   - Set an environment variable:

     ```bash
     # Linux / macOS
     export OPENWEATHER_API_KEY="your_api_key_here"

     # Windows (PowerShell)
     setx OPENWEATHER_API_KEY "your_api_key_here"
     ```

   - **Or** simply run the script and enter the key when prompted on startup.

5. **Run the Application**

    Enter the directory of the python script

    ```bash
    python openweatherCLI.py

--------

# Sorting & Median - Coding Activity 2

This part of the assessment implements the provided pseudocode:

- A function to **sort** an array of numbers in ascending order.
- A function to **sort the array and compute its median**.

The solution is provided as a command-line program that lets you either enter your own numbers or use predefined test arrays.

---

## Files

- `sortAndFindMedian.py` – main script for Activity 2.

---

## Features

- **Manual input mode**
  - Enter numbers in a single line (e.g. `3 1 4 1 5` or `1, 2, 3 4`).
  - The program parses the input, ignores invalid tokens, sorts the valid numbers, and prints:
    - The original list
    - The sorted list
    - The median

- **Predefined test arrays**
  - A set of built-in arrays to quickly demonstrate behavior, including:
    - Odd-length lists
    - Even-length lists
    - Negative values
    - Floating-point values and duplicates
  - You can select any test case from a menu and see its sorted version and median.

- **Manual sorting algorithm**
  - Implements **insertion sort**:
    - Time complexity: O(n²) in the worst case
    - Simple, readable, and appropriate for small inputs in this context
  - Sorting is done in a dedicated function separate from median calculation, matching the spirit of the pseudocode.

---

### Running the Program

    Enter the directory of the python script

    ```bash
    python sortAndFindMedian.py