def validate_time_settings(implicitly_wait, timeout, poll_frequency):
    """Verifies that implicitly_wait isn't larger than timeout or poll_frequency."""
    if poll_frequency < implicitly_wait:
        raise TypeError(
            f"Driver implicitly_wait {implicitly_wait} is longer than poll_frequency {poll_frequency}"
        )

    if timeout > 0 and timeout < implicitly_wait:
        raise TypeError(
            f"Driver implicitly_wait {implicitly_wait} is longer than timeout {timeout}"
        )
