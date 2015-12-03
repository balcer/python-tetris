import logging
import sender
import time

class SkylightPanel:

    PANEL_X_SIZE = 5
    PANEL_Y_SIZE = 5

    def __init__(self, addr):

        logging.info('%s: running constructor', __name__)
        self.addr = addr
        self.content = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def set(self, valueList):

        if len(valueList) == (self.PANEL_X_SIZE * self.PANEL_Y_SIZE):
            self.content = list(valueList)
        else:
            logging.warning('%s: wrong input size', __name__)

    def set_px(self, x, y, value):

        if x < self.PANEL_X_SIZE and y < self.PANEL_Y_SIZE:
            self.content[y * self.PANEL_X_SIZE + x] = value
        else:
            logging.warning('%s: index out of panel size', __name__)

    def set_px_liner(self, px, value):
        if px < 25:
            self.content[px] = value
        else:
            logging.warning('%s: index out of panel size', __name__)

    def show(self):

        print "Panel address: %d" %self.addr
        show_string = ''
        for y in xrange(self.PANEL_Y_SIZE):
            for x in xrange(self.PANEL_X_SIZE):
                value = self.content[y * self.PANEL_X_SIZE + x]
                if value < 10:
                    show_string += '  '
                    show_string += str(value)
                    show_string += ' '
                elif value < 100:
                    show_string += ' '
                    show_string += str(value)
                    show_string += ' '
                else:
                    show_string += str(value)
                    show_string += ' '
            show_string += "\n"
        print (show_string)


##my_test_panel = SkylightPanel(255)
##my_test_sender = sender.Sender("/dev/ttyUSB0", 115200)

##while True:
##
##    for i in range(25):
##        my_test_panel.set_px_liner(i, 255)
##        my_test_sender.send_direct_values(my_test_panel)
##        time.sleep(0.5)
##        my_test_panel.set_px_liner(i, 0)
##        time.sleep(0.5)


