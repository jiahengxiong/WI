import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.utils import shuffle
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import tensorflow as tf
from sklearn.preprocessing import StandardScaler

# Create label mapping dictionary
label_mapping = {
        "YouTube": 0,
        "Web": 1,
        "Idle": 2
    }

def data_process(num, youtube_path, idle_path, web_path):
    # Read data
    youtube_data = pd.read_csv(youtube_path).head(num)
    idle_data = pd.read_csv(idle_path).head(num)
    web_data = pd.read_csv(web_path).head(num)

    # Add label column
    youtube_data["label"] = "YouTube"
    web_data["label"] = "Web"
    idle_data["label"] = "Idle"

    # Concatenate datasets
    all_data = pd.concat([youtube_data, web_data, idle_data], ignore_index=True)

    # Encode labels using the label mapping dictionary
    all_data["encoded_label"] = all_data["label"].map(label_mapping)

    # Shuffle the dataset
    shuffled_data = shuffle(all_data)

    feature_column = ['up', 'down', 'mean_length', 'var_length', 'mean_time', 'var_time']
    label_column = ['encoded_label']

    # Get feature and label data
    train_data = shuffled_data[feature_column]
    train_label = shuffled_data[label_column]

    return train_data, train_label

if __name__ == "__main__":
    youtube_path = "D:\\WI_origin\\dataset\\test\\youtube.csv"
    idle_path = "D:\\WI_origin\\dataset\\train\\idle.csv"
    web_path = "D:\\WI_origin\\dataset\\train\\web.csv"

    train_data, train_label = data_process(num=1000, youtube_path=youtube_path, idle_path=idle_path, web_path=web_path)

    # One-hot encode labels
    train_label_onehot = pd.get_dummies(train_label['encoded_label']).values

    # Standardize feature data
    scaler = StandardScaler()
    train_data_scaled = scaler.fit_transform(train_data)

    # Create a neural network model
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(128, activation='selu', input_shape=(len(train_data.columns),)),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(64, activation='selu'),
        tf.keras.layers.Dense(3, activation='softmax')  # Output layer, 3 represents three categories
    ])

    # Compile the model
    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

    # Train the model
    model.fit(train_data_scaled, train_label_onehot, epochs=20, batch_size=4, verbose=2, validation_split=0.1)

    # Save the model
    model_filename = "D:\\WI_origin\\model\\neural_network_model.h5"
    model.save(model_filename)

    print("Model saved as", model_filename)
