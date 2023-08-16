import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from NN import data_process

label_mapping = {
    "YouTube": 0,
    "Web": 1,
    "Idle": 2
}

if __name__ == "__main__":
    youtube_path = "D:\\WI_origin\\dataset\\test\\youtube.csv"
    idle_path = "D:\\WI_origin\\dataset\\test\\idle.csv"
    web_path = "D:\\WI_origin\\dataset\\test\\web.csv"
    model_filename = "D:\\WI_origin\\model\\random_forest_model.joblib"

    test_data, test_label = data_process(num=100, youtube_path=youtube_path, idle_path=idle_path, web_path=web_path)

    loaded_rf_classifier = joblib.load(model_filename)

    y_pred = loaded_rf_classifier.predict(test_data)
    print(test_data)
    print(y_pred)
    accuracy = accuracy_score(test_label, y_pred)
    print("Test accuracy:", accuracy)

    # Generate a confusion matrix
    confusion_mat = confusion_matrix(test_label, y_pred)
    print(confusion_mat)

    class_names = ["YouTube", "Web", "Idle"]

    # Create a heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(confusion_mat, annot=True, fmt="d", cmap="Blues", xticklabels=class_names, yticklabels=class_names)
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.title('Confusion Matrix')

    # Save the image as a jpg
    confusion_mat_filename = "D:\\WI_origin\\result\\confusion_matrix.jpg"
    plt.savefig(confusion_mat_filename)

    print("Confusion matrix saved as", confusion_mat_filename)





