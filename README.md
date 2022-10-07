## kEeprom

This little program is a GUI for using the CH341A USB dongle programmer and the *ch341eeprom* and *flashrom* (ch341a_spi) programs. The program allows reading, saving, writing and checking binary data in 24c and 25q series eeprom memories through the I2C and SPI interfaces of the ch341a chip.

### Requirements

For the program to work properly, it is required to install the ch341eeprom program (all credits to [asbokid](http://sourceforge.net/projects/ch341eepromtool/)). The source code is included here and we must have the llvm, libusb and make libraries. For 25q series memories, we need the command in line program [flashrom](https://www.flashrom.org/Flashrom). The programs ch341eeprom and flashrom are used as subprocess on python. We also require PyQt: `pip install pyqt5 pyqt5-tools`. This is believed to work fine on a Linux environment.


