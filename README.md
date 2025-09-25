# Airbus Uçak Görüntü Sınıflandırma Projesi  
# Airbus Aircraft Image Classification Project

## Projenin Amacı  
Bu proje, derin öğrenme teknikleri kullanarak Airbus uçak modellerini görüntüler üzerinden otomatik olarak sınıflandırmayı hedeflemektedir. Amaç, farklı uçak modellerini yüksek doğrulukla ayırt edebilen bir görüntü sınıflandırma modeli geliştirmektir.

## Project Objective  
This project aims to classify Airbus aircraft models from images using deep learning techniques. The goal is to develop an image classification model capable of distinguishing between different aircraft types with high accuracy.

---

## Veri Seti Hakkında  
Kullanılan veri seti, Kaggle üzerinde yayımlanmış olan Airbus uçak görsellerinden oluşmaktadır. Veri seti, farklı Airbus modellerine ait binlerce etiketlenmiş JPG formatında görüntü içermektedir. Her sınıfa ait örnek sayısı farklılık göstermektedir.

## About the Dataset  
The dataset used in this project consists of Airbus aircraft images published on Kaggle. It includes thousands of labeled images in JPG format, representing different Airbus models. The number of samples per class varies.

---

## Kullanılan Yöntemler  
- Görüntü ön işleme ve veri artırma (Data Augmentation)  
- Convolutional Neural Networks (CNN) tabanlı model mimarisi  
- TensorFlow/Keras kütüphaneleri ile modelin eğitilmesi  
- Performans değerlendirmesi için doğruluk (accuracy), karışıklık matrisi (confusion matrix) ve sınıflandırma raporu (classification report) 1. Image Preprocessing and Data Augmentation

Images were normalized and resized.

Data augmentation techniques were applied to improve the model's generalization capacity, including rotation, shifting, flipping, and zooming.

from tensorflow.keras.preprocessing.image import ImageDataGenerator

datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True,
    zoom_range=0.2
)

2. Convolutional Neural Networks (CNN) Based Model Architecture

The model consists of Conv2D, MaxPooling2D, Flatten, and Dense layers.

ReLU activation and dropout layers are used between layers to improve learning and reduce overfitting.

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(img_height, img_width, 3)),
    MaxPooling2D(2,2),
    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D(2,2),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(num_classes, activation='softmax')
])

3. Model Training with TensorFlow/Keras

The model was compiled using the Adam optimizer and categorical cross-entropy loss function.

Accuracy was monitored as the performance metric during training.

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

history = model.fit(train_generator, epochs=epochs, validation_data=validation_generator)

4. Performance Evaluation

Model performance was evaluated using accuracy.

A confusion matrix and classification report were generated for detailed analysis.

from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Get predictions
y_pred = model.predict(validation_generator)
y_pred_classes = np.argmax(y_pred, axis=1)
y_true = validation_generator.classes

# Confusion matrix
cm = confusion_matrix(y_true, y_pred_classes)
plt.figure(figsize=(8,6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()

# Classification report
report = classification_report(y_true, y_pred_classes, target_names=class_names)
print('Classification Report:\n', report)

## Methods Used  
- Image preprocessing and data augmentation  
- Convolutional Neural Networks (CNN)-based model architecture  
- Model training using TensorFlow/Keras libraries  
- Evaluation through accuracy, confusion matrix, and classification report

---

## Elde Edilen Sonuçlar  
Model, test veri seti üzerinde yaklaşık **%XX doğruluk** elde etmiştir. Özellikle [başarılı olunan sınıflar buraya yazılabilir] sınıflarında yüksek başarı gözlemlenmiştir. Bu sonuçlar, Airbus uçaklarının görüntü tabanlı derin öğrenme modelleriyle sınıflandırılabileceğini göstermektedir.

## Results  
The model achieved approximately **XX% accuracy** on the test dataset. It performed particularly well on [you can mention strong-performing classes here]. These results demonstrate that Airbus aircraft can be effectively classified using image-based deep learning models.

---

## Ek Bilgiler  
- Eğitim sürecinde aşırı öğrenme (overfitting) problemi gözlemlenirse dropout ve erken durdurma (early stopping) gibi teknikler kullanılmıştır.  
- Eğitim ve doğrulama sonuçları görsellerle desteklenmiştir.  
- Grad-CAM ile modelin karar verirken görüntünün hangi bölgelerine odaklandığı görselleştirilmiştir.

## Additional Notes  
- If overfitting was observed during training, techniques like dropout and early stopping were used.  
- Training and validation metrics were visualized using graphs.  
- Grad-CAM was used to visualize which parts of the image the model focused on when making predictions.

https://www.kaggle.com/code/zeynepersoy/eda-airbus-aircraft-detection-dataset-sample
