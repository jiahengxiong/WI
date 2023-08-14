import csv

# 列表数据
list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]
list3 = [100, 200, 300, 400, 500]

# 打开 CSV 文件进行写操作
with open('output.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)

    # 写入每个列表作为一行数据
    csvwriter.writerow(list1)
    csvwriter.writerow(list2)
    csvwriter.writerow(list3)

print("数据已写入 CSV 文件")

