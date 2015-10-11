

class USBXboxInterfaceOne(USBInterface)
	
	name = "USB Xbox 360 Interface One"
	
	def __init__(self,verbose=10):
		
		descriptors = {
	 		0x21 : '\x00\x01\x01\x25\x81\x14\x00\x00\x00\x00\x13\x01\x08\x00\x00'
		}

       self.endpointOne = USBEndpoint(
            1,          # endpoint number
            USBEndpoint.direction_in,
            USBEndpoint.transfer_type_interrupt,
            USBEndpoint.sync_type_none,
            USBEndpoint.usage_type_data,
            32,      # max packet size
            4,         # polling interval, see USB 2.0 spec Table 9-13
            self.handle_buffer_available    # handler function
        )

       self.endpointTwo = USBEndpoint(
            1,          # endpoint number
            USBEndpoint.direction_in,
            USBEndpoint.transfer_type_interrupt,
            USBEndpoint.sync_type_none,
            USBEndpoint.usage_type_data,
            32,      # max packet size
            8,         # polling interval, see USB 2.0 spec Table 9-13
            self.handle_buffer_available    # handler function
        )


      	USBInterface.__init__(
            self,
            0,          # interface number
            0,          # alternate setting
            0xFF,          # interface class
            0x5D,          # subclass
            0x01,          # protocol
            0,          # string index
            verbose,
            [ self.endpointOne, self.endpointTwo ],
            descriptors
        )


	def handle_buffer_available(self):
		pass

class USBXboxInterfaceTwo(USBInterface)
	
	name = "USB Xbox 360 Interface Two"
	
	def __init__(self,verbose=10):
		
		descriptors = {
			0x21 : 	'\x00\x01\x01\x01\x82\x40\x01\x02\x20\x16\x83\x00\x00\x00\x00\x00\x00\x16\x03\x00\x00\x00\x00\x00\x00'
		}

       self.endpointOne = USBEndpoint(
            2,          # endpoint number
            USBEndpoint.direction_in,
            USBEndpoint.transfer_type_interrupt,
            USBEndpoint.sync_type_none,
            USBEndpoint.usage_type_data,
            32,      # max packet size
            2,         # polling interval, see USB 2.0 spec Table 9-13
            self.handle_buffer_available    # handler function
        )

       self.endpointTwo = USBEndpoint(
            2,          # endpoint number
            USBEndpoint.direction_in,
            USBEndpoint.transfer_type_interrupt,
            USBEndpoint.sync_type_none,
            USBEndpoint.usage_type_data,
            32,      # max packet size
            4,         # polling interval, see USB 2.0 spec Table 9-13
            self.handle_buffer_available    # handler function
        )
       self.endpointThree = USBEndpoint(
            3,          # endpoint number
            USBEndpoint.direction_in,
            USBEndpoint.transfer_type_interrupt,
            USBEndpoint.sync_type_none,
            USBEndpoint.usage_type_data,
            32,      # max packet size
            64,         # polling interval, see USB 2.0 spec Table 9-13
            self.handle_buffer_available    # handler function
        )

       self.endpointFour = USBEndpoint(
            3,          # endpoint number
            USBEndpoint.direction_in,
            USBEndpoint.transfer_type_interrupt,
            USBEndpoint.sync_type_none,
            USBEndpoint.usage_type_data,
            32,      # max packet size
            16,         # polling interval, see USB 2.0 spec Table 9-13
            self.handle_buffer_available    # handler function
        )



      	USBInterface.__init__(
            self,
            1,          # interface number
            0,          # alternate setting
            0xFF,          # interface class
            0x5D,          # subclass
            0x03,          # protocol
            0,          # string index
            verbose,
            [ self.endpointOne,self.endpointTwo,self.endpointThree,self.endpointFour ],
            descriptors
        )


	def handle_buffer_available(self):
		pass


class USBXboxInterfaceThree(USBInterface)
	
	name = "USB Xbox 360 Interface Three"
	
	def __init__(self,verbose=10):
		
		descriptors = {
			0x21 : '\x00\x01\x01\x22\x84\x07\x00'
		}

       self.endpointOne = USBEndpoint(
            4,          # endpoint number
            USBEndpoint.direction_in,
            USBEndpoint.transfer_type_interrupt,
            USBEndpoint.sync_type_none,
            USBEndpoint.usage_type_data,
            32,      # max packet size
            16,         # polling interval, see USB 2.0 spec Table 9-13
            self.handle_buffer_available    # handler function
        )

      	USBInterface.__init__(
            self,
            2,          # interface number
            0,          # alternate setting
            0xFF,          # interface class
            0x5D,          # subclass
            0x02,          # protocol
            0,          # string index
            verbose,
            [ self.endpointOne ],
            descriptors
        )


	def handle_buffer_available(self):
		pass

class USBXboxInterfaceFour(USBInterface)
	
	name = "USB Xbox 360 Interface Four"
	
	def __init__(self,verbose=10):
		
		descriptors = {
			0x21 : '\x00\x01\0x01\0x03'
		}

      	USBInterface.__init__(
            self,
            3,          # interface number
            0,          # alternate setting
            0xFF,          # interface class
            0x5D,          # subclass
            0x13,          # protocol
            0,          # string index
            verbose,
            [ self.endpointOne ],
            descriptors
        )


	def handle_buffer_available(self):
		pass


 class USBXboxControllerDevice(USBDevice):
    name = "USB Xbox 360 Controller"

    def __init__(self, maxusb_app, verbose=0, text=None):
        config = USBConfiguration(
                1,                                          # index
                "Xbox 360 Controller",    # string desc
                [  USBXboxInterfaceOne(),USBXboxInterfaceTwo(),USBXboxInterfaceThree(),USBXboxInterfaceFor() ]         # interfaces
        )

        USBDevice.__init__(
                self,
                maxusb_app,
                0,                      # device class
                0,                      # device subclass
                0,                      # protocol release number
                64,                     # max packet size for endpoint 0
                0x610b,                 # vendor id
                0x4653,                 # product id
                0x3412,                 # device revision
                "Microsoft",                # manufacturer string
                "Xbox 360 Controller",   # product string
                "00001",             # serial number string
                [ config ],
                verbose=verbose
        )

