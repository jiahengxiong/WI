import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import joblib

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
    youtube_path = "D:\\WI_origin\\dataset\\train\\youtube.csv"
    idle_path = "D:\\WI_origin\\dataset\\train\\idle.csv"
    web_path = "D:\\WI_origin\\dataset\\train\\web.csv"

    train_data, train_label = data_process(num=1000, youtube_path=youtube_path, idle_path=idle_path, web_path=web_path)

    # Create K-nearest neighbors classifier
    knn_classifier = KNeighborsClassifier(n_neighbors=10)  # You can adjust the n_neighbors parameter

    # Train the model
    knn_classifier.fit(train_data, train_label.values.ravel())

    model_filename = "D:\\WI_origin\\model\\knn_model.joblib"
    joblib.dump(knn_classifier, model_filename)

    print("Model saved as", model_filename)


