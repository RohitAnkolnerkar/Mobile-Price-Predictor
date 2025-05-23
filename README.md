# 📱 Mobile Price Predictor

This project predicts the **price range** of mobile phones based on their specifications using machine learning techniques. It's a classification problem where the model learns patterns from features like RAM, internal memory, screen size, etc.

## 🚀 Features

- 🔍 Predicts the price range of a mobile device
- 📊 Analyzes hardware specs like RAM, camera, battery, etc.
- 🧠 Trained with supervised learning algorithms
- 📈 Supports evaluation with accuracy, precision, and confusion matrix
- 🖥️ Optional web interface using Streamlit or Flask

## 🛠️ Tech Stack

- **Python 3**
- **Pandas, NumPy** – Data manipulation
- **Scikit-learn** – ML models and preprocessing
- **Matplotlib / Seaborn** – Visualization
- **Streamlit / Flask** – Optional web UI

## 📂 Dataset

We use a publicly available dataset (e.g., from Kaggle: [Mobile Price Classification](https://www.kaggle.com/iabhishekofficial/mobile-price-classification)) with the following features:

- `battery_power` – Total energy capacity of the battery (mAh)
- `blue` – Bluetooth support
- `clock_speed` – CPU speed (GHz)
- `dual_sim` – Dual SIM support
- `fc` – Front camera (MP)
- `four_g` – 4G capability
- `int_memory` – Internal memory (GB)
- `m_dep` – Mobile depth (cm)
- `n_cores` – Number of CPU cores
- `pc` – Primary camera (MP)
- `px_height` – Pixel height
- `px_width` – Pixel width
- `ram` – RAM (MB)
- `talk_time` – Battery talk time (hours)
- `three_g`, `touch_screen`, `wifi` – Connectivity features
- `price_range` – Target variable (0 to 3)

## 📈 ML Approach

1. **Data Preprocessing**
   - Handle missing data
   - Feature scaling (e.g., StandardScaler)
   - Train-test split

2. **Model Training**
   - Logistic Regression / Random Forest / SVM
   - Cross-validation
   - Hyperparameter tuning (GridSearchCV)

3. **Evaluation**
   - Accuracy, Precision, Recall
   - Confusion Matrix

## 💻 How to Run

1. **Clone the repo**
   ```bash
   git clone https://github.com/yourusername/mobile-price-predictor.git
   cd mobile-price-predictor

