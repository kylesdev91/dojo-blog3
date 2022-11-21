import tensorflow as tf 
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
# from tf.keras.optimizers import RMSprop
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import RMSprop, Adam
from tensorflow.keras.layers import GaussianNoise, Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
import pickle
from tensorflow.keras.constraints import max_norm
from keras.models import model_from_json
from keras.models import load_model
import matplotlib.pyplot as plt
import numpy as np
import cv2

IMG_SIZE_W = 212
IMG_SIZE_H = 120

# Opening the files about data
X = pickle.load(open("X.pickle", "rb"))
y = pickle.load(open("y.pickle", "rb"))
y = np.array(y)

# normalizing data (a pixel goes from 0 to 255)
X = X/255.0

def create_model(learning_rate=0.001, dropout_rate=0.2, a=16, b=32, c=512):
	model = Sequential()
	model.add(Conv2D(a, kernel_size=3, activation='relu', input_shape = (IMG_SIZE_H, IMG_SIZE_W, 3)))
	model.add(MaxPooling2D(pool_size=(2, 2)))
	model.add(Dropout(dropout_rate))

	model.add(Conv2D(b, kernel_size=3, activation='relu'))
	model.add(MaxPooling2D(pool_size=(2, 2)))
	model.add(Dropout(dropout_rate))
	
	# model.add(Conv2D(64, kernel_size=3, activation='relu'))
	# model.add(MaxPooling2D(pool_size=(2, 2)))
	# model.add(Dropout(dropout_rate))
	
	# model.add(Conv2D(64, kernel_size=3, activation='relu'))
	# model.add(MaxPooling2D(pool_size=(2, 2)))
	# model.add(Dropout(dropout_rate))
	
	# model.add(Conv2D(64, kernel_size=3, activation='relu'))
	# model.add(MaxPooling2D(pool_size=(2, 2)))
	# model.add(Dropout(dropout_rate))

	model.add(Flatten())
	model.add(Dense(c))
	# model.add(Dense(2, activation='softmax'))
	model.add(Dense(1, activation='sigmoid'))
	# model.compile(optimizer=Adam(learning_rate=0.001), loss='binary_crossentropy', metrics=['accuracy'])
	model.compile(optimizer=RMSprop(learning_rate=learning_rate), loss='binary_crossentropy', metrics=['accuracy'])
	return model


# validation_split corresponds to the percentage of images used for the validation phase compared to all the images

# Training the model, with 40 iterations
# validation_split corresponds to the percentage of images used for the validation phase compared to all the images
# model = KerasClassifier(build_fn=create_model, verbose=1)
# param_grid = dict(
# 	dropout_rate = [0.1, 0.2, 0.3],
# 	a = [8, 16, 32, 64],
# 	b = [16, 32, 64, 96],
# 	c = [256, 512, 756],
# 	learning_rate = [0.0003, 0.0005, 0.0007],
# 	epochs = [11]
# )
# grid = GridSearchCV(
# 	estimator=model, 
# 	param_grid=param_grid, 
# 	n_jobs=2, 
# )
# grid = RandomizedSearchCV(
# 	estimator=model, 
# 	param_distributions=param_grid, 
# 	n_jobs=-1,
# 	n_iter=5,
# 	return_train_score=True,
# 	verbose=1
# )
# grid_result = grid.fit(X, y)
model = create_model(
	learning_rate=0.0001, dropout_rate=0.4, a=32, b=16, c=256
)

# TODO: try with 100 epochs
history = model.fit(X, y, batch_size=64, epochs=50, validation_split=0.2)

# print("Best: %f using %s" % (grid_result.best_score_, grid_result.best_params_))
# means = grid_result.cv_results_['mean_test_score']
# stds = grid_result.cv_results_['std_test_score']
# params = grid_result.cv_results_['params']
# for mean, stdev, param in zip(means, stds, params):
#     print("%f (%f) with: %r" % (mean, stdev, param))

# Saving the model
model_json = model.to_json()
with open("models/model.json", "w") as json_file :
	json_file.write(model_json)

model.save_weights("models/model.h5")
print("Saved model to disk")

model.save('models/CNN.model')

# Printing a graph showing the accuracy changes during the training phase
# print(history.history.keys())
plt.figure(1)
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'validation'], loc='upper left')
plt.show()




# .3778
# model = Sequential()
# model.add(Conv2D(64, kernel_size=3, activation='relu', input_shape = (IMG_SIZE_H, IMG_SIZE_W, 3)))
# model.add(MaxPooling2D(pool_size=(2, 2)))
# model.add(Conv2D(8, kernel_size=3, activation='relu'))
# model.add(Flatten())
# model.add(Dense(32))
# model.add(Dense(5, activation='softmax'))
# model.compile(optimizer='Adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
