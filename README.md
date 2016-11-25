# lanbrowse
Have an app that runs on a phone that can browse directory hierarchies on a LAN.

Remove the need for samba/SMB, nfs, whatever support requirements from AOSP.

This should be simple to use with a back-end that supports RESTful APIs and
a client that can request the following things:
- browse/list
- get info a dir/file
- open a dir/file
- download a file
- play a file locally (e.g. on a ref board w/HDMI output and mplayer)
- stream a file (e.g. from something like VLC using udp on a specified address and port)

