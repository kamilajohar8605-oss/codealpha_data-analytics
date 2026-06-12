import pandas as pd

quotes = [
    "It is our choices, Harry, that show what we truly are.",
    "Try not to become a man of success. Rather become a man of value."
]

df = pd.DataFrame(quotes, columns=["Quotes"])
df.to_csv("quotes.csv", index=False)

print("quotes.csv created successfully")