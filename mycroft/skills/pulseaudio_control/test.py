from pulsectl import Pulse

pulse = Pulse('mycroft-pulse-client')

# for sink in pulse.sink_list():
#     print sink.proplist['device.description'] + ' ' + sink.proplist['alsa.card']
#
for source in pulse.source_list():
   print source.proplist['device.description'] + ' ' + source.proplist['alsa.card']

print pulse.source_list()

#print pulse.sink_list()[0].proplist['alsa.card']