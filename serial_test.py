import binascii
import serial
import time

tty_Port = "/dev/ttymxc2"
tty_baudrate = 9600

s_obj = serial.Serial(tty_Port, tty_baudrate, bytesize=8, parity='N', stopbits=1, timeout=2)

cmd = "00 64 04 AA BB CC"

def send_lora_test(cmd):
    """
    串口发送测试函数
    :param cmd: 定点目标的位置信息和数据
    前两对是位置信息
    第三队是信道
    后面是数据
    """
    time.sleep(3)
    s_obj.write(bytes.fromhex(cmd))

def receive_lora_test():
    """
    串口接受测试函数
    """
    time.sleep(1)
    num = s_obj.inWaiting()

    if num:
        try:
            data = str(binascii.b2a_hex(s_obj.read(num)))[2:-1]
            print(data)
    #        send_lora_test(cmd)
        except:
            lora_str = s_obj.read(num)

while True:
    send_lora_test(cmd)

