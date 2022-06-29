import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from IPython.display import Image
from six import StringIO
import pydotplus
import os
os.environ["PATH"] += os.pathsep + 'C:\Program Files (x86)\Graphviz2.38/bin/'
#Đọc dữ liệu đầu vào từ file excel
input_tuyendung = "Hosotd_data.csv"
datafile = pd.read_csv(input_tuyendung, header = 0)
datafile.head()


#Thực hiện chuyển đổi dữ liệu các thuộc tính về dạng số
d ={'Dai hoc': 2,'Cao dang':1,'Trung tam tin hoc': 0}
datafile['Level'] = datafile['Level'].map(d)
d = {'Co': 1,'Khong': 0}
datafile['Job'] = datafile['Job'].map(d)
datafile['Top_Train'] = datafile['Top_Train'].map(d)
datafile['Project'] = datafile['Project'].map(d)
datafile['Result'] = datafile['Result'].map(d)
datafile.head()

#Xác định thuộc tính tham gia vào xây dựng cây quyết định
field = list(datafile.columns[:5])

axis_y = datafile["Result"]# xác định thuộc tính phân lớp
axis_x = datafile[field]

field

#xây dựng cây quyết định
datafile = tree.DecisionTreeClassifier()
datafile = datafile.fit(axis_x,axis_y)


#Hiển thị cây quyết định dạng đồ họa
dot_data1 = StringIO()
tree.export_graphviz(datafile, out_file = dot_data1,
                    feature_names=field)
Tree_graph = pydotplus.graph_from_dot_data(dot_data1.getvalue())
Image(Tree_graph.create_png())

#Đọc dữ liệu Training vào từ file excel
input_train = "Training_data.csv"
datatrain = pd.read_csv(input_train, header = 0)
datatrain.head()


#Thực hiện chuyển đổi dữ liệu các thuộc tính về dạng số
d ={'Dai hoc': 2,'Cao dang':1,'Trung tam tin hoc': 0}
datatrain['Level'] = datatrain['Level'].map(d)
d = {'Co': 1,'Khong': 0}
datatrain['Job'] = datatrain['Job'].map(d)
datatrain['Top_Train'] = datatrain['Top_Train'].map(d)
datatrain['Project'] = datatrain['Project'].map(d)
#datatrain['Result'] = datatrain['Result'].map(d)
datatrain.head()

#Đếm số lượng dòng của training data
df = pd.DataFrame(datatrain)
rows = df.shape[0]
#Sử dụng tập luật để xét
for i in range(rows):
    if(df.at[i,'Project'] == 1):
        df.at[i,'Result'] = 1
    elif(df.at[i,'Project'] == 0 ):
        if(df.at[i,'Level'] <2):
            df.at[i,'Result'] = 0
        if(df.at[i,'Level'] ==2):
            if(df.at[i,'Top_Train'] == 1):
                df.at[i,'Result'] = 1
            elif(df.at[i,'Top_Train'] == 0):
                if(df.at[i,'Job']==1):
                    df.at[i,'Result'] =1
print(df)
