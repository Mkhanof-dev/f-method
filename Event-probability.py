good_event = int(input('Enter a good probability for event: '))  # check good event
event = int(input('Enter the number of all event\'s: '))  # check all event

event_probability = good_event/event
print(f'Your event probability (p) = n_g/n_all = {good_event}/{event} = {event_probability:.2f}')

status = str(input('Does finite probability have additional situations?(y/n): '))  # continue the calc probability
while status == 'y':
    event = good_event  # check good event
    good_event = int(input('Enter a good probability for event: '))  # check all event

    event_probability = good_event / event
    print(f'Your event probability (p) = n_g/n_all = {good_event}/{event} = {event_probability:.2f}')

    status = str(input('Does finite probability have additional situations?(y/n): '))  # continue the calc probability

    # check status user:
    if status == 'y':
        continue
    elif status == 'n':
        break
