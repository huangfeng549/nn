import carla
import time
from spawn_car import create_vehicle
from cruise_control import get_vehicle_speed, speed_cruise_control
from obstacle_detect import check_front_obstacle
from lane_keep import calc_lane_steer
from speed_limit import get_road_speed_limit

def main():
    client = carla.Client('localhost', 2000)
    client.set_timeout(10.0)
    world = client.get_world()
    carla_map = world.get_map()

    vehicle = None
    try:
        vehicle = create_vehicle(world, carla_map)
        print("✅ 作业5：道路限速控制功能启动")
        base_speed = 30

        for _ in range(900):
            world.tick()
            speed = get_vehicle_speed(vehicle)
            has_obstacle = check_front_obstacle(vehicle, world)
            steer_angle = calc_lane_steer(vehicle, carla_map)
            road_limit = get_road_speed_limit()
            target_speed = min(base_speed, road_limit)

            ctrl = carla.VehicleControl()
            if has_obstacle:
                ctrl.throttle = 0.0
                ctrl.brake = 1.0
            else:
                ctrl.throttle, ctrl.brake = speed_cruise_control(speed, target_speed)

            ctrl.steer = steer_angle
            vehicle.apply_control(ctrl)
            time.sleep(0.05)
    finally:
        if vehicle:
            vehicle.destroy()

if __name__ == "__main__":
    main()