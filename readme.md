# Potato Blight Image Classifier

## Overview
This project aims to develop an end-to-end Potato Blight Image Classifier to help farmers in East Africa identify blight in their crops and recommend possible solutions. The classifier will leverage machine learning techniques to analyze images of potato plants and detect signs of blight.

## Objectives
- Develop a machine learning model to classify images of potato plants.
- Create a user-friendly interface for farmers to upload images and receive diagnoses.
- Provide actionable recommendations to farmers based on the classification results.

## Steps to Build the Classifier

1. **Data Collection**
    - Gather a dataset of potato plant images, including healthy plants and those affected by blight.
    - Label the images accordingly.

2. **Data Preprocessing**
    - Clean and preprocess the images.
    - Augment the dataset to improve model robustness.

3. **Model Development**
    - Choose an appropriate machine learning model(CNN).This model will be build using TF.
    - Train the model using the preprocessed dataset.
    - Model will be optimized with quantization and TF-Lite.
    - Evaluate the model's performance and fine-tune as necessary.

4. **Interface Development**
    - Develop a web or mobile application for farmers to upload images.
    - This will be built using the React Framework!
    - Integrate the trained model into the application to provide real-time classification.

5. **Recommendation System**
    - Based on the classification results, provide tailored recommendations to farmers.
    - The back end will be built using TF serving and Fast API.
    - Include information on treatment options and preventive measures.

## Potential Impact
By providing an accessible tool for early detection of potato blight, this project aims to:
- Reduce crop losses due to blight.
- Improve the livelihoods of farmers in East Africa.
- Promote sustainable agricultural practices.

## Contributing
We welcome contributions from the community. Please feel free to submit issues and pull requests.

## License
This project is licensed under the MIT License.

## Contact
For any questions or suggestions, please contact us at [samzwana@gmail.com].
