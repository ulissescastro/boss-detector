#!/usr/bin/env python
import pyshark

#capture = pyshark.LiveCapture(interface='wlan0mon', display_filter='wlan.addr == c0:65:99:2a:d1:90 && radiotap.dbm_antsignal <= -30')
capture = pyshark.LiveCapture(interface='wlan0mon', display_filter='wlan.addr == c0:65:99:2a:d1:90 && radiotap.dbm_antsignal <= -30')
#capture.sniff(timeout=50)
#capture

for packet in capture.sniff_continuously(packet_count=1):
    print packet.pretty_print()
#    for field in packet.radiotap.field_names:
#        print "FIELD [%s] :  %s" % (field, packet.radiotap.get_field_value(field))


