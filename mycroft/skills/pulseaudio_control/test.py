from pulsectl import Pulse

pulse = Pulse('mycroft-pulse-client')

for sink in pulse.sink_list():
    print sink.proplist['alsa.card']

#print pulse.sink_list()[0].proplist['alsa.card']