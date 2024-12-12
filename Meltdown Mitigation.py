def is_criticality_balanced(temperature, neutrons_emitted):
    return temperature < 800 and neutrons_emitted > 500 and (temperature * neutrons_emitted) < 500000


def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    efficiency = (generated_power / theoretical_max_power) * 100

    if efficiency >= 80:
        return 'green'
    elif efficiency >= 60:
        return 'orange'
    elif efficiency >= 30:
        return 'red'
    else:
        return 'black'


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    product = temperature * neutrons_produced_per_second

    if product < 0.9 * threshold:
        return 'LOW'
    elif 0.9 * threshold <= product <= 1.1 * threshold:
        return 'NORMAL'
    else:
        return 'DANGER'
