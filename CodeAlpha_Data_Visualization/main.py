import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    "Category": ["A", "B", "C", "D", "E"],
    "Values": [10, 15, 7, 20, 12]
}

df = pd.DataFrame(data)

plt.bar(df["Category"], df["Values"])
plt.title("Sample Data Visualization")
plt.xlabel("Category")
plt.ylabel("Values")

plt.show()