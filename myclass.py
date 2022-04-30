import os
import cv2
import numpy as np
from sklearn.preprocessing import LabelEncoder
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam

x = []
y = []

for folder in os.listdir('flowers'):
  for file in os.listdir(os.path.join('flowers', folder)):
    if file.endswith('jpg'):
      y.append(folder)
      img = cv2.imread(os.path.join('flowers', folder, file))
      img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
      im2 = cv2.resize(img_rgb, (64, 64))
      x.append(im2)

data_arr = np.array(x)
label_arr = np.array(y)

print(data_arr[0])

encoder = LabelEncoder()
y = encoder.fit_transform(label_arr)
y = to_categorical(y, 5)
x = data_arr / 255

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=10)

SIZE = 64

model = Sequential()
model.add(Conv2D(filters = 32, kernel_size = (3,3),padding = 'Same',activation ='relu', input_shape = (SIZE,SIZE,3)))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(filters = 64, kernel_size = (3,3),padding = 'Same',activation ='relu'))
model.add(Conv2D(filters = 128, kernel_size = (3,3),padding = 'Same',activation ='relu'))
model.add(Conv2D(filters = 128, kernel_size = (3,3),padding = 'Same',activation ='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dropout(rate=0.5))
model.add(Dense(5, activation = "softmax"))

model.summary()

datagen = ImageDataGenerator(
        rotation_range=20,
        zoom_range = 0.20,
        width_shift_range=0.3,
        height_shift_range=0.3,
        horizontal_flip=True,
        vertical_flip=True)

datagen.fit(X_train)

model.compile(optimizer=Adam(lr=0.0001),loss='categorical_crossentropy',metrics=['accuracy'])

model.fit(X_train, y_train,batch_size = 32 , epochs = 30)

model.evaluate(X_test, y_test)

from sklearn.metrics import classification_report
labels_name = ['daisy', 'dandelion', 'rose', 'sunflower', 'tulip']

y_pred = (model.predict(X_test) > 0.5).astype("int32")
print(classification_report(y_test, y_pred,target_names=labels_name))