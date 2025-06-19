"""
29/03/2020 03:48:17 PM Sunday: INFO: Text Entered in edit box
29/03/2020 03:48:17 PM Sunday: ERROR: Unable to click on search button

"""
import logging

#i -12 hours format, h-24 hours format
#filemode="a"--append mode
#filemode="w"--overwritten
#logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%d/%m/%y %I:%M:%S %p %A' , level=logging.DEBUG ,filename="test2.log",filemode="w")
logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%d/%m/%y %H:%M:%S %p %A' , level=logging.DEBUG ,filename="test2.log",filemode="w")
logging.critical("This is critical msg")
logging.error("This is a error msg")
logging.warning("this is warning msg")
logging.info("This is a Info msg")
logging.debug("This is a Debug msg")