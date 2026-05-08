import carla
import time
from spawn_car import create_vehicle
from cruise_control import get_vehicle_speed, speed_cruise_control
from obstacle_detect import check_front_obstacle
from lane_keep import calc_lane_steer
from speed_limit import get_road_speed_limit
from emergency_brake import emergency_brake_logic
from turn_light import auto_turn_light_tip
from safe_distance import monitor_safe_distance
from parking_assist import parking_assist_tip

def main():
    client = carla.Client('localhost', 2000)
    client.set_timeout(10.0)
    world = client.get_world()
    carla_map = world.get_map()

    vehicle = None
    try:
        vehicle = create_vehicle(world, carla_map)
        print("✅ 作业9：泊车辅助场景提示功能启动")
        base_speed = 30

        for _ in range(1300):
            world.tick()
            speed = get_vehicle_speed(vehicle)
            has_obstacle = check_front_obstacle(vehicle, world)
            steer_angle = calc_lane_steer(vehicle, carla_map)
            road_limit = get_road_speed_limit()
            target_speed = min(base_speed, road_limit)

            monitor_safe_distance(vehicle, world)
            auto_turn_light_tip(steer_angle)
            parking_assist_tip(vehicle, carla_map)

            ctrl = carla.VehicleControl()
            brake_cmd = emergency_brake_logic(has_obstacle)
            if brake_cmd:
                ctrl.throttle, ctrl.brake = brake_cmd
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