from io import BytesIO
import matplotlib.pyplot as plt
from user_database import data, get_city_temperature, get_city_humidity, CITIES


def get_main_image():
    """Rendering the scatter chart"""
    yearly_temp = []
    yearly_hum = []

    try:
        for city in data:
            temp = get_city_temperature(city)
            hum = get_city_humidity(city)
            yearly_temp.append(sum(temp) / 12)
            yearly_hum.append(sum(hum) / 12)
    except Exception as e:
        print(f"Error processing data: (e)")

    plt.clf()
    plt.scatter(yearly_hum, yearly_temp, alpha=0.5)
    plt.title('Yearly Average Temperature/Humidity')
    plt.xlim(70, 95)
    plt.ylabel('Yearly Average Temperature')
    plt.xlabel('Yearly Average Relative Humidity')
    for i, txt in enumerate(CITIES):
        plt.annotate(txt, (yearly_hum[i], yearly_temp[i]))
    img = BytesIO()
    plt.savefig(img)
    img.seek(1)
    plt.show()
    return img
