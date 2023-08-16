import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from NN import  data_process

# Load test data
youtube_path = "D:\\WI_origin\\dataset\\test\\youtube.csv"
idle_path = "D:\\WI_origin\\dataset\\test\\idle.csv"
web_path = "D:\\WI_origin\\dataset\\test\\web.csv"
test_data, test_label = data_process(num=100, youtube_path=youtube_path, idle_path=idle_path, web_path=web_path)
test_label_onehot = pd.get_dummies(test_label['encoded_label']).values

# Preprocess test data
scaler = StandardScaler()
test_data_scaled = scaler.fit_transform(test_data)

# Load the saved model
model_filename = "D:\\WI_origin\\model\\neural_network_model.h5"
loaded_model = tf.keras.models.load_model(model_filename)

# Evaluate the model on test data
loss, accuracy = loaded_model.evaluate(test_data_scaled, test_label_onehot, verbose=1)
print("Test accuracy:", accuracy)
