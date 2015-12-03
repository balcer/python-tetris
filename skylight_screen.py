import skylight_panel
import logging
import sender

class SkylightScreen:

    def __init__(self):

        logging.info('%s: running constructor', __name__)
        self.x_size_px = 0
        self.y_size_px = 0
        self.x_size_panel = 0
        self.y_size_panel = 0
        self.x_margin = 0
        self.y_margin = 0
        self.panel_count = 0
        self.panels_list = []
        self.screen_array = []
        self.tetris_sender = sender.Sender("/dev/ttyUSB0", 115200)

    
    def update(self, screen_array):

        self.screen_array = list(screen_array)
        if((self.x_size_px != len(self.screen_array)) or (self.y_size_px != len(self.screen_array))):
            logging.info('%s: resizing screen', __name__)
            self.x_size_px = len(screen_array)
            self.y_size_px = len(screen_array[0])
            self.x_size_panel = self.x_size_px / skylight_panel.SkylightPanel.PANEL_X_SIZE
            self.y_size_panel = self.y_size_px / skylight_panel.SkylightPanel.PANEL_Y_SIZE
            self.x_margin = self.x_size_px % skylight_panel.SkylightPanel.PANEL_X_SIZE
            self.y_margin = self.y_size_px % skylight_panel.SkylightPanel.PANEL_Y_SIZE
            if self.x_margin != 0:
                self.x_size_panel += 1
            if self.y_margin != 0:
                self.y_size_panel += 1
            self.panel_count = self.x_size_panel * self.y_size_panel
            self.panels_list = [skylight_panel.SkylightPanel(count + 1) for count in xrange(self.panel_count)]
            #logging.info('size: %dx%d, panels: %dx%d, margins: %dx%d, panel_count: %d',
            #                                                            self.x_size_px,
            #                                                            self.y_size_px,
            #                                                            self.x_size_panel,
            #                                                            self.y_size_panel,
            #                                                            self.x_margin,
            #                                                            self.y_margin,
            #                                                            self.panel_count)
        for y_panel in range(self.y_size_panel):
            for x_panel in range(self.x_size_panel):
                temp_panel_tab = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                for y_pixel in range(5):
                    for x_pixel in range(5):
                        temp_panel_tab[(y_pixel * 5) + x_pixel] = self.screen_array[x_pixel + (x_panel * 5)][y_pixel + (y_panel * 5)]
                self.panels_list[(y_panel * 2) + x_panel].set(temp_panel_tab)
        for panel in self.panels_list:
            if panel.addr == 7 or panel.addr == 8:
                self.tetris_sender.send_direct_values(panel)
        self.panels_list[0].show()
        self.show()

    def show(self):

        print "Screen size: %dx%d" %(self.x_size_px, self.y_size_px)
        show_string = ''
        for y in xrange(self.y_size_px):
            for x in xrange(self.x_size_px):
                value = self.screen_array[x][y]
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


#logging.basicConfig(level=logging.DEBUG)
#sampel_table = [[0 for x in range(20)] for x in range(10)]
#sampel_table[2][2] = 3
#sampel_table[3][5] = 255
#
#my_test_screen = SkylightScreen()
#my_test_screen.update(sampel_table)
#my_test_screen.show()