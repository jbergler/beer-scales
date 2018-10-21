PORT = /dev/ttyUSB0
VERSION = 20181020-v1.9.4-665-g7795b2e5c

micropython.bin:
	curl -o micropython.bin http://micropython.org/resources/firmware/esp32-${VERSION}.bin

erase:
	esptool.py --chip esp32 --port ${PORT} erase_flash

flash: micropython.bin
	esptool.py --chip esp32 --port ${PORT} write_flash -z 0x1000 micropython.bin

upload:
	mpfshell -o `echo ${PORT} | sed 's/.*\///g'` -n -c 'mput .*\.py'

monitor:
	picocom -b115200 ${PORT}


