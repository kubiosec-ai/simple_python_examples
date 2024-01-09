import pandas as pd
from sklearn.ensemble import IsolationForest

# Step 1: Read and parse the data
def read_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            ip = parts[0]
            ports = parts[1:]
            data.append([ip, len(ports), ports])
    return pd.DataFrame(data, columns=['IP', 'PortCount', 'Ports'])

# Step 2: Outlier Detection
def detect_outliers(df):
    # Using Isolation Forest for outlier detection
    clf = IsolationForest(contamination=0.05)  # adjust contamination as needed
    df['Outlier'] = clf.fit_predict(df[['PortCount']])
    return df

# Example Usage
file_path = './stats.csv'
df = read_data(file_path)
outlier_df = detect_outliers(df)

# Display outliers
print(outlier_df[outlier_df['Outlier'] == -1])
