import serial
import logging
import segment
from time import sleep

class Sender:

	def __init__ (self, path_to_tty, baudrate):

		self.serial = serial.Serial(path_to_tty, baudrate)

	def calculate_crc(self, message):
		CRC = 0xFFFF
		for byte in message:
			CRC ^= byte
			for i in range(8):
				if (CRC & 0x0001) > 0:
					CRC >>= 1
					CRC ^=0xA001
				else:
					CRC >>= 1
		return CRC

	def send_trigger(self):
		message = [0x00, 0x04]
		crc = self.calculate_crc(message)
		message += [crc & 0xff, crc >> 8]
		self.serial.write(message)
		self.serial.flush()
		sleep(0.0001)

	def send_direct_common_value(self, addr, value):
		message = [addr, 0x05, value]
		crc = self.calculate_crc(message)
		message += [crc & 0xff, crc >> 8]
		self.serial.write(message)
		self.serial.flush()
		sleep(0.0001)

	def send_direct_values(self, segment_to_send):
		message = [segment_to_send.addr, 0x09]
		for byte in segment_to_send.content:
			print byte
			message += [byte]
		crc = self.calculate_crc(message)
		message += [crc & 0xff, crc >> 8]
		self.serial.write(message)
		self.serial.flush()
		sleep(0.01)

#sender = Sender("/dev/ttyUSB0", 115200)
#my_segment = segment.Segment(0x01)
#sender.send_trigger()
#sender.send_direct_common_value(0x01, 0xFF)
#sender.send_direct_values(my_segment)
#sender.send_trigger()

#logging.basicConfig(level=logging.DEBUG)
#logging.info("Server started...")