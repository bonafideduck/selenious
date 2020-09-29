def validate_time_settings(implicit_wait, timeout, poll_frequency):
    """Verifies that implicit_wait isn't larger than timeout or poll_frequency."""
    if poll_frequency < implicit_wait:
        raise TypeError(
            f"Driver implicit_wait {implicit_wait} is longer than poll_frequency {poll_frequency}"
        )

    if timeout < implicit_wait:
        raise TypeError(
            f"Driver implicit_wait {implicit_wait} is longer than timeout {timeout}"
        )
