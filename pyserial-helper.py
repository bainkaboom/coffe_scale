# python3
# Import Serial (pyserial)
import serial
import time

# Globals
BAUDRATE = 115200
PORT = 'COM5'


class Scale:
    """ Class to read the scale, handles the serial connection using a context manager."""

    def __init__(self):
        # Attribs
        self.ready = False

        # Set up Serial port to begin reading, taring out scale immediately
        time.sleep(3)
        ser.write(b'x')
        time.sleep(1)
        ser.write(b'1')
        time.sleep(1)
        ser.write(b'x')
        time.sleep(1)

    def genreading(ser):
        while True:
            line = ser.read()
            yield line

def main():
    ser = serial.Serial()
    ser.baudrate = 115200
    ser.port = 'COM5'

    ser.open()
    time.sleep(5)
    ser.write(b'x')
    time.sleep(1)
    ser.write(b'1')
    time.sleep(1)
    ser.write(b'x')
    time.sleep(1)

    test = True
    while test:
        ser.reset_input_buffer()
        print(ser.readline().decode('utf-8'), end='')


    while ser.isOpen():
        if ser.inWaiting() > 0:  # if incoming bytes are waiting to be read from the serial input buffer
            data_str = ser.read(ser.inWaiting()).decode(
                'ascii')  # read the bytes and convert from binary array to ASCII
            print(data_str, end='')




if __name__ == '__main__':
    main()