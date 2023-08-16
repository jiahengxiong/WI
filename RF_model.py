import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.utils import shuffle
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler, MinMaxScaler
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

    train_data, train_label = data_process(num=2000, youtube_path=youtube_path, idle_path=idle_path, web_path=web_path)


    # Define the candidate values for parameters
    param_grid = {
        'n_estimators': [100, 500, 1000],
        'max_depth': [None, 10, 20, 30],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4],
        'max_features': ['auto', 'sqrt', 'log2'],
        'random_state': [99]
    }

    # 创建随机森林分类器
    rf_classifier = RandomForestClassifier()

    # 训练模型
    rf_classifier.fit(train_data, train_label.values.ravel())

    # 保存模型
    model_filename = "D:\\WI_origin\\model\\random_forest_model.joblib"
    joblib.dump(rf_classifier, model_filename)

    print("Model saved as", model_filename)
