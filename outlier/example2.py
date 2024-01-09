import pandas as pd
from sklearn.ensemble import IsolationForest

# Step 1: Read and parse the data
def read_data(file_path):
    data_dict = {}
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            ip = parts[0]
            ports = parts[1:]

            if ip not in data_dict:
                data_dict[ip] = set()

            for port in ports:
                if port:  # Check if port is not empty
                    data_dict[ip].add(port)

    # Convert the dictionary to a list format
    data = [[ip, len(data_dict[ip]), list(data_dict[ip])] for ip in data_dict]
    return pd.DataFrame(data, columns=['IP', 'PortCount', 'Ports'])

# Step 2: Outlier Detection
def detect_outliers(df):
    # Using Isolation Forest for outlier detection
    clf = IsolationForest(contamination=0.05)  # adjust contamination as needed
    df['Outlier'] = clf.fit_predict(df[['PortCount']])
    return df

# Example Usage
file_path = './stats2.csv'
df = read_data(file_path)
outlier_df = detect_outliers(df)
print(df)

# Display outliers
print(outlier_df[outlier_df['Outlier'] < 1])
