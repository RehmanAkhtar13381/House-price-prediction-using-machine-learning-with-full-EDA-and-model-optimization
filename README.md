🏠 House Price Prediction App
Overview
The House Price Prediction App is a web-based application built with Python, Streamlit, and Scikit-learn that predicts the price of a house based on its key features:
Bedrooms
Bathrooms
Area (sqft)
The app uses a Linear Regression model trained on historical housing data to provide accurate price predictions. It’s a beginner-friendly yet professional project demonstrating the integration of machine learning models with interactive web applications.
Features
Predict house prices in real-time by entering property details.
Handles missing values in the dataset using mean imputation.
Simple and intuitive Streamlit-based user interface.
Fully modular: easy to expand with additional features (e.g., floors, waterfront, grade).
Saves the trained model and preprocessing object for reproducibility.
Project Structure
House-Price-Prediction/
│
├── house_data.csv          # Dataset containing house features and prices
├── train_model.py          # Script to train Linear Regression model
├── main.py                 # Streamlit app for predicting house prices
├── house_model.pkl         # Saved trained Linear Regression model
├── imputer.pkl             # Saved SimpleImputer for missing value handling
├── requirements.txt        # List of required Python packages
└── README.md               # Project documentation
Dataset
The project uses a CSV dataset house_data.csv with the following columns:
Column	Description
bedrooms	Number of bedrooms in the house
bathrooms	Number of bathrooms
area	Total area of the house in sqft
price	Price of the house (target variable)
⚠️ Ensure the dataset contains these columns exactly, otherwise the app may throw errors.
Installation & Setup
Clone the repository:
git clone <your-repo-url>
cd House-Price-Prediction
Create a virtual environment (optional but recommended):
python -m venv .venv
source .venv/bin/activate   # Linux / macOS
.venv\Scripts\activate      # Windows
Install dependencies:
pip install -r requirements.txt
Training the Model
Before using the app, train the model using the train_model.py script:
python train_model.py
This will train a Linear Regression model on house_data.csv.
It will save the model as house_model.pkl and the imputer as imputer.pkl.
Running the App
Start the Streamlit web app:
streamlit run main.py
The app will open in your browser.
Enter Bedrooms, Bathrooms, and Area.
Click Predict House Price to see the estimated price.
Example Usage
Bedrooms	Bathrooms	Area (sqft)	Predicted Price
3	2	1500	$250,000
4	3	2000	$350,000
Requirements
Make sure the following Python packages are installed:
streamlit
numpy
pandas
scikit-learn
A requirements.txt is included for easy installation.
Future Improvements
Add more features: floors, grade, waterfront, condition.
Use advanced regression models like RandomForestRegressor or GradientBoostingRegressor.
Add visualizations: scatter plots, price distribution charts.
Deploy as a web application using Streamlit sharing or Heroku.
License
This project is open-source and free to use for learning and demonstration purposes.
Author
Rehman Akhtar – passionate about Machine Learning, Data Science, and Python development.
