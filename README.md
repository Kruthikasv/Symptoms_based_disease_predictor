# Symptoms Based Disease Predictor Documentation

## Overview

The Symptoms Based Disease Predictor is an application designed to predict potential diseases based on user-entered symptoms. Utilizing a machine learning model, this system provides probable diagnoses, helping users understand possible health conditions and take appropriate action. The project employs a trained model to analyze symptoms and suggest corresponding diseases.

## Features

- **User Input**: Users can enter multiple symptoms they are experiencing.
- **Disease Prediction**: The system predicts potential diseases based on the symptoms provided.
- **Probability Scores**: The application provides probability scores for each predicted disease, indicating the likelihood of each condition.
- **Extensive Symptom Database**: Comprehensive list of symptoms for accurate predictions.
- **User-Friendly Interface**: Simple and intuitive interface for ease of use.

## Technologies Used

- **Backend**: Python (Flask)
- **Frontend**: HTML, CSS, JavaScript
- **Machine Learning**: Scikit-learn
- **Database**: SQLite

## Installation

### Prerequisites

- Python 3.x
- Flask
- Scikit-learn
- SQLite

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Kruthikasv/Symptoms_based_disease_predictor.git
   ```

2. **Set Up a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**
   - Initialize the SQLite database.
     ```bash
     flask db init
     flask db migrate -m "Initial migration."
     flask db upgrade
     ```

5. **Train the Machine Learning Model**
   - Run the script to train the model on the dataset provided.
     ```bash
     python train_model.py
     ```

6. **Run the Application**
   ```bash
   flask run
   ```

7. **Access the Application**
   - Open your web browser and navigate to `http://localhost:5000`.

## Usage

### Predicting Diseases

1. **Enter Symptoms**: Users can input multiple symptoms in the provided text fields.
2. **Submit**: Click on the 'Predict' button to get the results.
3. **View Predictions**: The application will display a list of potential diseases along with their probability scores.

### Updating the Database

- **Adding Symptoms**: Admins can add new symptoms to the database.
- **Updating Disease Information**: Admins can update information about diseases and their corresponding symptoms.

## Machine Learning Model

The machine learning model used in this project is based on a decision tree classifier trained on a dataset of diseases and symptoms. The model has been fine-tuned to provide accurate predictions based on the input symptoms.

## Database Schema

- **Symptoms**: Stores symptom information.
- **Diseases**: Stores disease information and associated symptoms.
- **Predictions**: Stores prediction history for analysis and improvement.

## Contributions

Contributions to the project are welcome. Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -am 'Add your feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

For any inquiries or support, please contact:

- **Name**: Kruthika Vasisht
- **Email**: kruthikasvasisht@gmail.com
