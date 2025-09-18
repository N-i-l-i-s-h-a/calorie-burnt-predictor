# Calorie Prediction Application

This project is a web application that predicts calories burned during a workout. It uses a pre-trained XGBoost model and is built with the Streamlit framework in Python.

---

## How to Run Locally

Follow these steps to set up and run the application on your local machine.

1.  **Clone the Repository**
    Navigate to the application directory after cloning.
    ```bash
    git clone https://github.com/N-i-l-i-s-h-a/calorie-burnt-predictor.git
    cd calories-burnt-project/calorie-predictor-app
    ```

2.  **Set Up the Environment**
    Create and activate a Python virtual environment.
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
    *On Windows, use `venv\Scripts\activate`*

3.  **Install Dependencies**
    Install all required packages from the requirements file.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Launch the Application**
    Run the Streamlit server.
    ```bash
    streamlit run app.py
    ```
    The application will open in a new tab in your web browser.
