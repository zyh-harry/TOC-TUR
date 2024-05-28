import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

#Reading sample data
file_path = 'TUR_combined_with_discharge_SAMPLE_DATA.csv'
df = pd.read_csv(file_path)

#Defining the X and y
#X is all the data from 'pnwa' and 'wmth' including discharge
#y is the turbidity load at Pine falls
y_columns = [col for col in df.columns if 'turbidity' in col and 'load' in col]
y = df[y_columns[0]]

x_columns = [col for col in df.columns if 'pnwa' in col or 'wmth' in col or 'discharge' in col]
X = df[x_columns]

#Fill missing values (if any)
X = X.fillna(X.mean())
y = y.fillna(y.mean())

#Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

#Initialize the RandomForestRegressor
model = RandomForestRegressor(n_estimators=100, random_state=42)

#Train the model
model.fit(X_train, y_train)

#Predictions
y_pred = model.predict(X_test)

#Model error and r squared
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R^2 Score: {r2}")
