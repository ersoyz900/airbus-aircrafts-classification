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
- Performans değerlendirmesi için doğruluk (accuracy), karışıklık matrisi (confusion matrix) ve sınıflandırma raporu (classification report)

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
