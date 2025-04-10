import pickle
from sklearn.preprocessing import LabelEncoder

# All locations used
locations = ['Delhi', 'Mumbai', 'Chennai', 'Kolkata', 'Bangalore', 'Hyderabad', 'Pune', 'Ahmedabad']

# Create & fit encoder
label_encoder = LabelEncoder()
label_encoder.fit(locations)

# Save using pickle
with open('model/label_encoder.pkl', 'wb') as f:
    pickle.dump(label_encoder, f)

print("label_encoder.pkl created successfully!")
