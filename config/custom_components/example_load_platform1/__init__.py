"""Example Load Platform integration."""
PLATFORM = "example_load_platform1"


def setup(hass, config):
    """Your controller/hub specific code."""
    # Data that you want to share with your platforms
    hass.data[PLATFORM] = {"temperature": 23}

    hass.helpers.discovery.load_platform("sensor", PLATFORM, {}, config)

    return True
