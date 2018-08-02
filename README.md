# tuw_rqt
Custom rqt Plugins

## tuw_emergency_stop
Simple emergency stop button which publishes a `std_msgs::Bool` message on the provided topic in the GUI to stop a robot. 

### Usage
The plugin can be used in `rqt_gui` or as standalone with the following command:
```
rqt --standalone rqt_emergency_stop
```
When launched as a standalone one can remap the published topic as an alternative to entering the topic name in the text field of the plugin.
```
rqt --standalone rqt_emergency_stop emergency_stop:=$TOPIC_NAME
```
