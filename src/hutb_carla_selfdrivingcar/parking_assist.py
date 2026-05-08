def parking_assist_tip(vehicle, carla_map):
    wp = carla_map.get_waypoint(vehicle.get_location())
    if wp.is_junction:
        print("🅿️  泊车辅助提示：已进入路口区域，请减速慢行注意观察")
    else:
        print("✅ 泊车辅助提示：正常道路直行行驶")