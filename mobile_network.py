from datetime import datetime

class Subscriber:
    def __init__(self, last_name, initials, phone, tariff, gigabytes, minutes, sms, payment, start_date):
        self.last_name = last_name
        self.initials = initials
        self.phone = phone
        self.tariff = tariff
        self.gigabytes = gigabytes
        self.minutes = minutes
        self.sms = sms
        self.payment = payment
        self.start_date = datetime.strptime(start_date, "%d.%m.%Y").date()

class MobileNetwork:
    def __init__(self):
        self.subscribers = []
    
    def load_from_file(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split('/')
                    self.subscribers.append(Subscriber(
                        parts[0], parts[1], parts[2], parts[3], 
                        int(parts[4]), int(parts[5]), int(parts[6]), 
                        float(parts[7]), parts[8]
                    ))
        #self.sort_by_name()
    
    def sort_by_name(self):
        self.subscribers.sort(key=lambda x: x.last_name)
