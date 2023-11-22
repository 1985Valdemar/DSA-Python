import pandas as pd

countries_df = pd.DataFrame(
    {
        "Country": ["Nepal", "Switzerland", "Germany", "Canada"],
        "Continent": ["Asia", "Europe", "Europe", "North America"],
        "Primary Language": ["Nepali", "French", "German", "English"],
    }
)
print("Countries DataFrame:")
print(countries_df, "\n")

capitals = ["Kathmandu", "Zurich", "Berlin", "Ottawa"]

countries_df.insert(2, "Capital", capitals)

print("Countries DataFrame after inserting Capital column:")
print(countries_df)