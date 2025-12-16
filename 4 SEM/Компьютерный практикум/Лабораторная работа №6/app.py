from flask import Flask, request, jsonify, render_template
from PIL import Image
import io
import imghdr

app = Flask(__name__)

# Маршрут для главной страницы:
@app.route('/')
def index():
    return render_template('index.html')

# Маршрут для обработки POST-запроса
@app.route('/size2json', methods=['POST'])
def size2json():
    # Проверка загружен ли файл
    if 'image' not in request.files:
        return jsonify({'result': 'no file provided'}), 400
    
    # Получение изображения из запроса
    image_file = request.files['image']

    # Проверка является ли файл изображением
    if imghdr.what(image_file) is None:
        return jsonify({'result': 'invalid filetype'}), 400

    try:
        # Открываем изображение 
        img = Image.open(io.BytesIO(image_file.read()))
        # Получаем высоту и ширину изображения
        width, height = img.size
        # Формируем JSON с информацией о размерах изображения
        image_info = {'width': width, 'height': height}
        # Возвращаем JSON-ответ с информацией о размерах изображения
        return jsonify(image_info), 200
    except Exception as e:
        # Ошибка при обработке изображения
        print("Error processing image:", e)
        return jsonify({'result': 'error processing image'}), 500

# Маршрут для вывода логина Moodle 
@app.route('/login')
def login():
    return jsonify({'author': '1140096'}), 200

# Запуск сервера
if __name__ == '__main__':
    app.run(debug=True)
