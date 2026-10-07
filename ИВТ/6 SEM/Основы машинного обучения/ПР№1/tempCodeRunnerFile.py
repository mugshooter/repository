from flask import Flask, request, jsonify, render_template
import numpy as np
import pickle

app = Flask(__name__)

# Загрузка модели и скейлера при старте приложения
with open('best_wine_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)
    
with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# Порядок признаков (должен соответствовать порядку при обучении)
FEATURE_ORDER = [
    'fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
    'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
    'pH', 'sulphates', 'alcohol'
]

@app.route('/')
def home():
    """Главная страница с формой ввода"""
    return render_template('index.html', features=FEATURE_ORDER)

@app.route('/predict', methods=['POST'])
def predict():
    """API-эндпоинт для предсказания"""
    try:
        # Получение данных из формы
        data = request.form if request.form else request.get_json()
        
        # Сбор признаков в правильном порядке
        features = [float(data[col]) for col in FEATURE_ORDER]
        
        # Масштабирование признаков
        scaled_features = scaler.transform([features])
        
        # Предсказание
        prediction = model.predict(scaled_features)
        
        return jsonify({
            'status': 'success',
            'prediction': int(prediction[0]),
            'features': dict(zip(FEATURE_ORDER, features))
        })
    
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)