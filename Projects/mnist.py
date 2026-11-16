import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# 1. Load MNIST dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# 2. Normalize the data
x_train, x_test = x_train / 255.0, x_test / 255.0

# 3. Reshape for ImageDataGenerator (needs 4D: batch, height, width, channels)
x_train_gen = x_train.reshape(-1, 28, 28, 1)
x_test_gen = x_test.reshape(-1, 28, 28, 1)

# 4. Data Augmentation
datagen = ImageDataGenerator(
    rotation_range=10,
    zoom_range=0.1,
    width_shift_range=0.1,
    height_shift_range=0.1
)
datagen.fit(x_train_gen)

# 5. Build the model (using Flatten to take 28x28 images directly, or Input(shape=(784,)) if pre-flattened)
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28, 1)),
    layers.Dense(128, activation=tf.keras.layers.LeakyReLU(alpha=0.1)),
    layers.Dense(64, activation=tf.keras.layers.LeakyReLU(alpha=0.1)),
    layers.Dense(10, activation='softmax')
])

# 6. Compile the model
model.compile(optimizer='rmsprop',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 7. Train the model with augmented data
model.fit(datagen.flow(x_train_gen, y_train, batch_size=32), epochs=10)

# 8. Evaluate the model (pass the 4D or flattened test set matching the model input)
test_loss, test_acc = model.evaluate(x_test_gen, y_test)
print(f"Test accuracy: {test_acc}")

# 9. Make predictions
predictions = model.predict(x_test_gen)

# 10. Display the first image and prediction
plt.imshow(x_test[0], cmap=plt.cm.binary)
plt.title(f"Predicted: {predictions[0].argmax()}")
plt.show()