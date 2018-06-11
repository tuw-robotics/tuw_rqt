import os
import rospy
import rospkg

from qt_gui.plugin import Plugin
from python_qt_binding import loadUi
from python_qt_binding.QtWidgets import QWidget
from std_msgs.msg import Bool

class EmergencyStopPlugin(Plugin):

    def __init__(self, context):
        super(EmergencyStopPlugin, self).__init__(context)
        # Give QObjects reasonable names
        self.setObjectName('rqt_emergency_stop_plugin')

        # Process standalone plugin command-line arguments
        from argparse import ArgumentParser
        parser = ArgumentParser()
        # Add argument(s) to the parser.
        parser.add_argument("-q", "--quiet", action="store_true",
                      dest="quiet",
                      help="Put plugin in silent mode")
        args, unknowns = parser.parse_known_args(context.argv())
        if not args.quiet:
            print 'arguments: ', args
            print 'unknowns: ', unknowns

        # Create QWidget
        self._widget = QWidget()
        # Get path to UI file which should be in the "resource" folder of this package
        ui_file = os.path.join(rospkg.RosPack().get_path('rqt_emergency_stop'), 'resource', 'EmergencyStop.ui')
        # Extend the widget with all attributes and children from UI file
        loadUi(ui_file, self._widget)
        # Give QObjects reasonable names
        self._widget.setObjectName('EmergencyStopUi')
        # Show _widget.windowTitle on left-top of each plugin (when
        # it's set in _widget). This is useful when you open multiple
        # plugins at once. Also if you open multiple instances of your
        # plugin at once, these lines add number to make it easy to
        # tell from pane to pane.
        if context.serial_number() > 1:
            self._widget.setWindowTitle(self._widget.windowTitle() + (' (%d)' % context.serial_number()))
        # Add widget to the user interface
        context.add_widget(self._widget)
        
        self.stop_pub = rospy.Publisher('emergency_stop', Bool, queue_size=1)
        
        self._widget.stop_button.setCheckable(True)
        self._widget.lineEdit.textChanged.connect(self.line_edit_callback)
        self._widget.stop_button.toggled.connect(self.stop_button_callback)

    def shutdown_plugin(self):
        # TODO unregister all publishers here
        self.stop_pub.unregister()

    def save_settings(self, plugin_settings, instance_settings):
        # TODO save intrinsic configuration, usually using:
        # instance_settings.set_value(k, v)
        pass

    def restore_settings(self, plugin_settings, instance_settings):
        # TODO restore intrinsic configuration, usually using:
        # v = instance_settings.value(k)
        pass

    #def trigger_configuration(self):
        # Comment in to signal that the plugin has a way to configure
        # This will enable a setting button (gear icon) in each dock widget title bar
        # Usually used to open a modal configuration dialog

    def stop_button_callback(self, checked):
        
        msg = Bool()
        
        if checked:
            print("emergency stop pressed")
            msg.data = True
        else:
            print("emergency stop released")
            msg.data = False
            
        self.stop_pub.publish(msg)
        
    def line_edit_callback(self, text):
        self.stop_pub.unregister()
        self.stop_pub = rospy.Publisher(text, Bool, queue_size=1)
