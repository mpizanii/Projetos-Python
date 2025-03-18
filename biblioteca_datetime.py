from datetime import datetime
import pytz

data = datetime.now(pytz.timezone("Europe/Oslo"))
data_2 = datetime.now(pytz.timezone("Asia/Tokyo"))


data_convertida = datetime.strftime(data, "%Hh%M")
data_convertida_2 = datetime.strftime(data_2, "%Hh%M")

print(f"O horário em Oslo é : {data_convertida}")
print(f"O horário em Tokyo é : {data_convertida_2}")
