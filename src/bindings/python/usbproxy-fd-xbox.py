from USBProxyApp import USBProxyApp
from USBXbox import USBXboxControllerDevice
import sys

 u = USBProxyApp(verbose=1)
XboxController = USBXboxControllerDevice(u,verbose=10)
XboxController.connect()
try:
	XboxController.run()
except KeyboardInterrupt:
	XboxController.disconnect()
