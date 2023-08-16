# This is a sample Python project for WI
# Author: Jiaheng Xiong


from scapy.all import *
import numpy as np
import csv
import pandas as pd

import joblib


MAC = 'a0:29:42:f2:b0:52'
model_filename = "D:\\WI_origin\\model\\best_random_forest_model.joblib"

column_names = ["up", "down", "mean_length", "var_length", "mean_time", "var_time"]
csv_filename = "data.csv"
state = ['YouTube', 'Web Browsing', 'Idle']

def data_process(num, csv):
    # Read data
    data = pd.read_csv(csv).head(num)


    feature_column = ['up', 'down', 'mean_length', 'var_length', 'mean_time', 'var_time']


    # Get feature and label data
    data = data[feature_column]


    return data

def data_processing(up, down, interval_time, length):
    # print(up, down, interval_time, length)
    data = []
    time = []
    for i in range(0, len(interval_time) - 1):
        time.append(10*(interval_time[i + 1] - interval_time[i]))

    if len(length) > 0:
        mean_length = np.mean(length)
        var_length = np.var(length)
    else:
        mean_length = 0
        var_length = 0

    if len(time) > 0:
        mean_time = np.mean(time)
        var_time = np.var(time)
    else:
        mean_time = 0
        var_time = 0
    data.append(up)
    data.append(down)
    data.append(mean_length)
    data.append(var_length)
    data.append(mean_time)
    data.append(var_time)
    return data
def packet_callback(pack):
    if pack['Ethernet'].dst == MAC or pack['Ethernet'].src == MAC:

        interval_time.append(time.time())

loaded_rf_classifier = joblib.load(model_filename)

while 1 == 1:
    if os.path.exists("stop_flag.txt"):
        print("Stop flag detected. Exiting data_collect.py.")
        break
    interval_time = []
    up = 0
    down = 0
    length = []
    dpkt = sniff(iface="Intel(R) Wi-Fi 6 AX201 160MHz", count=0, timeout=10, prn=packet_callback)
    for pack in dpkt:
        if pack['Ethernet'].dst == MAC or pack['Ethernet'].src == MAC:
            length.append(len(pack))
            if pack['Ethernet'].dst == MAC:
                down = down + 1
            if pack['Ethernet'].src == MAC:
                up = up + 1
    data = data_processing(up, down, interval_time, length)
    # Convert data array to CSV-like string format
    with open(csv_filename, mode='w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(column_names)
        csv_writer.writerow(data)
    data = data_process(1, csv_filename)

    y_pred = loaded_rf_classifier.predict(data)

    print("The statement of user is " + str(state[y_pred[0]]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
