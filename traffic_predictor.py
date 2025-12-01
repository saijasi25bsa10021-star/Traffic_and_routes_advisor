
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle
import os

MODEL_PATH = "models/traffic_model.pkl"

def train_dummy_traffic_model():
    data = {
        'start': ['Delhi', 'Noida', 'Gurgaon', 'Faridabad'],
        'end': ['Noida', 'Gurgaon', 'Faridabad', 'Delhi'],
        'time': [8, 9, 17, 18],
        'traffic': [2, 3, 4, 5]
    }
    df = pd.DataFrame(data)
    X = pd.get_dummies(df[['start','end','time']])
    y = df['traffic']
    model = RandomForestRegressor()
    model.fit(X,y)
    os.makedirs("models", exist_ok=True)
    with open(MODEL_PATH,'wb') as f:
        pickle.dump(model,f)
    print("Traffic model trained successfully!")

def predict_traffic(start,end,time):
    if not os.path.exists(MODEL_PATH):
        train_dummy_traffic_model()
    with open(MODEL_PATH,'rb') as f:
        model = pickle.load(f)
    df = pd.DataFrame([[start,end,time]],columns=['start','end','time'])
    X = pd.get_dummies(df)
    X_train_cols = pd.get_dummies(pd.DataFrame({
        'start': ['Delhi','Noida','Gurgaon','Faridabad'],
        'end': ['Noida','Gurgaon','Faridabad','Delhi'],
        'time': [8,9,17,18]
    })).columns
    X = X.reindex(columns=X_train_cols, fill_value=0)
    traffic_level = model.predict(X)[0]
    return round(traffic_level,1)
