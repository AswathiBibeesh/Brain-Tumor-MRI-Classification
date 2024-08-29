Brain Tumor MRI Image Classification

Project Overview:
This project focuses on developing an automated system for classifying brain tumors from MRI images using advanced deep learning techniques. Leveraging Convolutional Neural Networks (CNNs), the system is designed to distinguish between four categories: glioma, meningioma, pituitary tumor, and no tumor. The primary goal is to enhance the accuracy and efficiency of brain tumor diagnosis, providing a reliable tool that can assist radiologists and medical professionals.

Objectives

•	Model Performance Assessment: The objective is to evaluate and compare the performance of trained CNN models using metrics like accuracy, sensitivity, specificity, and F1-score to identify the most reliable model for brain tumor classification.

•	Model Comparision:  To compare the trained CNN models—ResNet50, Inception V3, and VGG16—based on their performance metrics to determine which model most effectively and accurately classifies brain tumors from MRI images.

•	Model accuracy: In this brain tumor MRI image classification project measures the proportion of correctly classified images, indicating the overall effectiveness of the trained CNN models.

•	Data utilization: In this brain tumor MRI image classification project involves preprocessing, training, and testing the models on the "Brain Tumor MRI Dataset" to optimize and evaluate their performance in accurately identifying tumor types.

Dataset Discription:

The "Brain Tumor MRI Dataset" contains MRI images labeled into four categories: glioma, meningioma, pituitary tumor, and no tumor. Images have been preprocessed to 224x224 pixels and augmented to improve model robustness. The dataset is split into training, validation, and test sets.

•	ID (integer): A unique identifier for each security, used for indexing and referenc-ing.

•	Symbol (string): The ticker symbol for the security, a unique code identifying pub-licly traded securities.

•	Name (string): The full name of the company associated with the security.

•	Market (string): The market where the security is listed (e.g., NYSE).

•	Sector (string): The sector in which the company operates (e.g., Technology, Healthcare).

•	Industry (string): The specific industry classification of the company (e.g., Biotech-nology, Software).

•	Country (string): The country where the company is based.

•	Currency (string): The currency in which the security is traded (e.g., USD for NYSE).

•	Date (date): The date when the security information was recorded or last updated.

•	Description (string): Additional information about the security, including business activities or relevant notes.

Project Structure

•	data/: Contains the MRI dataset, divided into subdirectories for training, validation, and testing.

•	notebooks/: Includes Jupyter notebooks for data preprocessing, model training, and evaluation.

•	models/: Stores the trained models, including the ResNet50, Inception V3, and both pretrained and scratch versions of VGG16.

•	scripts/: Contains Python scripts for data preprocessing (preprocess.py), training the models (train.py), and evaluating model performance (evaluate.py).

•	README.md: Provides an overview and instructions for the project.

•	requirements.txt: Lists the Python dependencies required to run the project.


Model Architectures

Four CNN architectures were implemented and trained for this project:

•	ResNet50: A deep residual network that uses skip connections to enable the training of very deep networks.

•	Inception V3: A network architecture that captures diverse spatial features using multiple convolutional filter sizes in parallel.

•	VGG16: A simple and widely used architecture known for its depth and uniform structure, consisting of 16 layers.

•	VGG16 (From Scratch): The VGG16 architecture implemented and trained from scratch, without any pretrained weights, to fully tailor it to the brain tumor classification task.

Preprocessing

The dataset was preprocessed using the following steps:

•	Resizing: All images were resized to 224x224 pixels.

•	Normalization: Pixel values were scaled to the range [0, 1].

•	Data Augmentation: Techniques such as rotation, zoom, and horizontal flipping were applied to artificially expand the dataset and improve model generalization.

Training

•	The models were trained on the preprocessed dataset using the Adam optimizer and categorical cross-entropy loss function. Training was conducted over 100 epochs with a batch size of 16. Validation data was used to monitor the training process and prevent overfitting.

Evaluation

•	Model performance was evaluated on the test set using metrics such as accuracy, sensitivity, specificity, precision, recall, and F1-score. Confusion matrices were also generated to visualize the models' predictions and identify any patterns of misclassification.

Results

•	Inception V3: Achieved an accuracy of 98%.

•	ResNet50: Achieved an accuracy of 91%.

•	VGG16 (From Scratch): Achieved an accuracy of 91.23%, making it the highest-performing VGG16 model.

•	VGG16 (Pretrained): Achieved an accuracy of 86.16%.

•	The VGG16 model trained from scratch outperformed the pretrained version, demonstrating that a tailored model without pretrained weights can be more effective for this specific task. Overall, the Inception V3 model achieved the highest accuracy among all models.

Installation
•	Clone the repository

•	Navigate to the project directory

•	Set up a virtual environment (optional but recommended)

•	Install the required dependencies

•	Download and place the dataset

•	Run the preprocessing script

•	Train the models

•	Evaluate the models

Usage

•	To use the project, start by preprocessing the dataset with the preprocess.py script, then train the CNN models using the train.py script, and finally, evaluate the performance of the trained models by running the evaluate.py script.


Contributing

•	Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes. Ensure that your code follows the existing style and includes appropriate tests.

License

•	This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements

•	This project was inspired by the need for advanced diagnostic tools in the medical field. Special thanks to the contributors and the open-source community for their valuable resources and tools. The "Brain Tumor MRI Dataset" is publicly available and serves as the foundation for this work.
















