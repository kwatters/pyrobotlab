webgui = Runtime.create("webgui","WebGui")

# if you don't want the browser to 
# autostart to homepage
#
# webgui.autoStartBrowser(false)

# set a different port number to listen to
# default is 8888
# webgui.setPort(7777)

# on startup the webgui will look for a "resources"
# directory (may change in the future)
# static html files can be placed here and accessed through
# the webgui service

# starts the websocket server
# and attempts to autostart browser
webgui.startService();

