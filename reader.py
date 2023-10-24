import serial

def read_card_information():
    try:
        # Replace 'COM3' with the appropriate serial port for your card reader.
        ser = serial.Serial('COM3', 9600, timeout=1)
        while True:
            card_data = ser.readline().strip().decode('utf-8')
            if card_data:
                print(f"Card Data: {card_data}")
                # You can process and display the card information as needed.
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        ser.close()

if __name__ == "__main__":
    read_card_information()
