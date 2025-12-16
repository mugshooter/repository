from flask import Flask, render_template, request, make_response
import base64
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    # Возвращает информацию о пользователе (в данном случае логин)
    return {"author": "1140096"}

@app.route('/makeimage', methods=['GET', 'POST'])
def make_image():
    if request.method == 'POST':
        try:
            # Получаем ширину и высоту изображения из формы
            width = int(request.form['width'])
            height = int(request.form['height'])
        except ValueError:
            # Возвращаем сообщение об ошибке, если введены некорректные значения
            return render_template('makeimage.html', message="Invalid image size")

        # Получаем текст из формы
        text = request.form['text']
        # Создаем изображение
        image = create_image(width, height, text)
        
        # Кодируем изображение в base64
        buffered = BytesIO()
        image.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')

        # Возвращаем HTML с отображением изображения
        response = make_response(render_template('image_display.html', image=img_str))
        response.headers['Content-Type'] = 'text/html'
        return response

    return render_template('makeimage.html')

def create_image(width, height, text):
    # Создаем пустое изображение заданных размеров
    image = Image.new('RGB', (width, height), color='pink')

    # Инициализируем объект ImageDraw
    draw = ImageDraw.Draw(image)
    # Рисуем текст на изображении
    draw.text((width/2, height/2), text, fill=(0, 0, 0),)
    font_size = 30
    return image

if __name__ == '__main__':
    app.run(debug=True)
