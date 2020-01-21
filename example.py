from pyxantech import get_xantech

xantech = get_xantech('/dev/ttyUSB0')

# Valid zones are 11-16 for main xantech amplifier
zone_status = xantech.zone_status(11)

# Print zone status
print('Zone Number = {}'.format(zone_status.zone))
print('Power is {}'.format('On' if zone_status.power else 'Off'))
print('Mute is {}'.format('On' if zone_status.mute else 'Off'))
print('Public Anouncement Mode is {}'.format('On' if zone_status.pa else 'Off'))
print('Do Not Disturb Mode is {}'.format('On' if zone_status.do_not_disturb else 'Off'))
print('Volume = {}'.format(zone_status.volume))
print('Treble = {}'.format(zone_status.treble))
print('Bass = {}'.format(zone_status.bass))
print('Balance = {}'.format(zone_status.balance))
print('Source = {}'.format(zone_status.source))
print('Keypad is {}'.format('connected' if zone_status.keypad else 'disconnected'))

# Turn off zone #11
xantech.set_power(11, False)

# Mute zone #12
xantech.set_mute(12, True)

# Set volume for zone #13
xantech.set_volume(13, 15)

# Set source 1 for zone #14 
xantech.set_source(14, 1)

# Set treble for zone #15
xantech.set_treble(15, 10)

# Set bass for zone #16
xantech.set_bass(16, 7)

# Set balance for zone #11
xantech.set_balance(11, 3)

# Restore zone #11 to it's original state
xantech.restore_zone(zone_status)