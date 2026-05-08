def emergency_brake_logic(has_obstacle):
    if has_obstacle:
        return 0.0, 1.0
    return None