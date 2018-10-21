import esp
import network
import webrepl

# required for things to work properly
esp.osdebug(None)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    print('connecting to network...')
    wlan.connect('lemon', 'pineapple')
    while not wlan.isconnected():
        pass
    print('network config:', wlan.ifconfig())

webrepl.start()

