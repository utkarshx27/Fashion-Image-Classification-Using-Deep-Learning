# Fashion Image Classification Using Deep Learning

This project focuses on fashion image classification using deep learning, leveraging ResNet50V2 as the feature extractor. The model is trained on a labeled dataset of fashion images with data augmentation techniques to improve generalization. The training pipeline is implemented using TensorFlow and Keras, with key features such as learning rate scheduling, early stopping, and model checkpointing for optimal performance. After training, the best-performing model is deployed locally using FastAPI and Docker, enabling a scalable and efficient API for real-time image classification.

# Key Features:
- Deep Learning Model: ResNet50V2-based CNN trained on fashion images
- Data Augmentation: Rotation, zoom, brightness adjustments, and more using ImageDataGenerator
- Training Optimizations: Learning rate scheduling, early stopping, and best model checkpointing
- Performance Evaluation: Accuracy and loss visualization using Matplotlib
- Deployment: FastAPI-based RESTful API containerized with Docker for local inference.

# Technologies Used:
- Python, TensorFlow/Keras, OpenCV, NumPy, Pandas, Seaborn, Matplotlib
- FastAPI for model serving
- Docker for containerized deployment.

## UI
![Test Image](https://raw.githubusercontent.com/utkarshx27/Fashion-Image-Classification-Using-Deep-Learning/e12e21757a9e84ea4ce421cce3cbebae06636157/images/img1.png)
![Test Image](https://raw.githubusercontent.com/utkarshx27/Fashion-Image-Classification-Using-Deep-Learning/e12e21757a9e84ea4ce421cce3cbebae06636157/images/img2.png)
