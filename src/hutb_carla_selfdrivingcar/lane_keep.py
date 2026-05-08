import math

def calc_lane_steer(vehicle, carla_map):
    wp = carla_map.get_waypoint(vehicle.get_location(), project_to_road=True)
    if not wp:
        return 0.0
    dx = vehicle.get_location().x - wp.transform.location.x
    dy = vehicle.get_location().y - wp.transform.location.y
    yaw = math.radians(vehicle.get_transform().rotation.yaw)
    cross_error = dx * math.sin(yaw) - dy * math.cos(yaw)
    steer = -cross_error * 0.3
    return max(-0.12, min(0.12, steer))