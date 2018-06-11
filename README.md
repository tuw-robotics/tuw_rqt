# tuw_rqt
Custom rqt Plugins

## tuw_emergency_stop
Simple emergency stop button which publishes a `std_msgs::Bool` message on the provided topic in the GUI to stop a robot. 

### Usage
The plugin can be used in `rqt_gui` or as standalone with the following command:
```
rqt --standalone rqt_emergency_stop
```
