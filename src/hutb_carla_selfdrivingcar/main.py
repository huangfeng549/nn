import carla
from spawn_car import create_vehicle

def main():
    client = carla.Client('localhost', 2000)
    client.set_timeout(10.0)
    world = client.get_world()
    carla_map = world.get_map()

    vehicle = None
    try:
        vehicle = create_vehicle(world, carla_map)
        print("✅ 作业1：车辆生成成功")
        for _ in range(100):
            world.tick()
    finally:
        if vehicle:
            vehicle.destroy()

if __name__ == "__main__":
    main()