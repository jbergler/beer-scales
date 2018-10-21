from hx711 import HX711
from utime import sleep_ms

class Scales(HX711):
    def __init__(self, data_pin=14, clock_pin=12):
        super(Scales, self).__init__(data_pin, clock_pin)
        self.offset = 0

    def reset(self):
        self.power_off()
        self.power_on()
        sleep_ms(1000)
        self.offset = self.read()
        print(self.offset)
        print("done")

    def value(self, reads=10, delay_ms=1):
        values = []
        for _ in range(reads):
            values.append(self.read() - self.offset)
            sleep_ms(delay_ms)
        
        weights = []
        for prev in values:
            weights.append(sum([1 for current in values if abs(prev - current) / (prev / 100) <= 10]))
        return sorted(zip(values, weights), key=lambda x: x[1]).pop()[0]

def network():
    import urequests
    url = 'http://ifconfig.io/all.json'
    headers = {'content-type': 'application/json'}
    data = '' #{"state": "15", "attributes": {"friendly_name": "Kitchen Temperature", "unit_of_measurement": "°C"}}'
    resp = urequests.get(url, headers=headers)
    print(resp.json())

#network()

# sensor


print("starting up")
scales = Scales()
scales.reset()
while True:
    val = scales.value()
    print(val)
    sleep_ms(200)


