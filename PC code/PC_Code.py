import serial
import time

ser = serial.Serial('COM7', 2400)

text = """Finance Minister Arun Jaitley Tuesday hit out at former RBI governor Raghuram Rajan for predicting that the next banking crisis would be triggered by MSME lending, saying postmortem is easier than taking action when it was required. Rajan, who had as the chief economist at IMF warned of impending financial crisis of 2008, in a note to a parliamentary committee warned against ambitious credit targets and loan waivers, saying that they could be the sources of next banking crisis. Government should focus on sources of the next crisis, not just the last one. In particular, government should refrain from setting ambitious credit targets or waiving loans. Credit targets are sometimes achieved by abandoning appropriate due diligence, creating the environment for future NPAs, Rajan said in the note. Both MUDRA loans as well as the Kisan Credit Card, while popular, have to be examined more closely for potential credit risk. Rajan, who was RBI governor for three years till September 2016, is currently."""

start_time = time.time()
total_bits_transmitted = 0
update_interval = 0.3 

for char in text:
    ser.write(char.encode())
    total_bits_transmitted += 8 
    time.sleep(0.3)

    if ser.in_waiting > 0:
        received_char = ser.read(1) 
        print("Received Data: ", received_char)

    if time.time() - start_time >= update_interval:
        elapsed_time = time.time() - start_time
        transmission_speed_bps = total_bits_transmitted / elapsed_time
        print("Transmission Speed: {:.2f} bps".format(transmission_speed_bps))
        start_time = time.time()
        total_bits_transmitted = 0 

ser.close()







