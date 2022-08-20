import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import numpy as np
import time

#1st ADC Converter Config
CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

def PPM_Reading(reading):
    return(3.125*reading - 1.25)

#Convert Analog Data to Digital Data and store it in an np array
print('Reading MCP3008 values, press Ctrl-C to quit...')
# Print nice channel column headers.
arr_HCHO = np.zeros(1)
i = 0
while(i < 20):
    # Read all the ADC channel values in an np array.
    print(i)
    arr_HCHO = np.append(arr_HCHO, PPM_Reading(mcp.read_adc(0)))
    # Print the latest ADC value
    print(arr_HCHO[(np.size(arr_HCHO) - 1)])
    # Pause for half a second.
    time.sleep(0.5)
    i = i + 1
arr_HCHO = np.delete(arr_HCHO, 0)
print(arr_HCHO)
  

