from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "7a0d793e87b52331c2d534f8b885d371"   # 👉 तुमची key टाका

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None

    if request.method == 'POST':
        city = request.form.get('city')

        if city:
            city = city.strip()   # 👉 space remove

            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

            response = requests.get(url)
            data = response.json()

            print(data)   # 👉 terminal मध्ये बघा

            if str(data.get("cod")) != "200":
                result = {"error": f"Error: {data}"}
            else:
                result = {
                    "city": city,
                    "temp": data['main']['temp'],
                    "humidity": data['main']['humidity']
                }

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)