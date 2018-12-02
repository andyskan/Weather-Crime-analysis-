#Import Library of Gaussian Naive Bayes model
from sklearn.naive_bayes import GaussianNB
import numpy as np

#assigning predictor and target variables
x= np.array([[-3,7],[1,5], [1,2], [-2,0], [2,3], [-4,0], [-1,1], [1,1], [-2,2], [2,7], [-4,1], [-2,7]])
y = np.array([3, 3, 3, 3, 4, 3, 3, 4, 3, 4, 4, 4])

#Create a Gaussian Classifier
model = GaussianNB()

# Train the model using the training sets 
model.fit(x, y)

#Predict Output 
predicted= model.predict([[1,2],[3,4]])
print(predicted)

#Output: ([3,4])

"""
#####Features/Parameters used:
#1. area     ->  1-21, OR Mungkin agar lebih detail bisa menggunakan Location.1
#2. date     ->  holiday is 1 vs non holiday is 2
#3. hours    ->  1-9 is 1,9-17 is 2,17-1 is 3
#4. weather  ->   sort it by how disastrous
#5. day      ->  1-7, OR month 1-12
#6. graph cuaca


#####Labels/Results:
#give number to each crime


#####Methods:
1. Naive Bayesian with GaussianNB
2. KNN with neighbors.KNeighbors


#####Weaknesses in our method:
1. holiday dipilih berdasarkan hari nasional yang dirayakan di los angeles, california, sehingga mungkin tidak mengikuti event yang bukan tahunan
2. Cuaca yang diambil harian per daerah, dengan koordinat rata2 tiap kejadian, karena keterbatasan API call yang bisa dilakukan
3. pengkategrorian crime ke tiap tipe secara manual, bukan melalui text-mining


#####Joining in pandas
multiple index:indexed_df = df.set_index(['A', 'B'])
caller.set_index('key').join(other.set_index('key'))
"""