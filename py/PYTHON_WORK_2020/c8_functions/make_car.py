def make_car(manufacturer, model, **properties):
    """Returns a dictionary of information about a car."""
    properties['manufacturer'] = manufacturer
    properties['model'] = model
    return properties