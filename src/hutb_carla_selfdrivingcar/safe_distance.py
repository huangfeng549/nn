import math

def monitor_safe_distance(vehicle, world):
    min_dist = 999.0
    for actor in world.get_actors().filter("vehicle.*"):
        if actor.id == vehicle.id:
            continue
        dist = math.hypot(actor.get_location().x - vehicle.get_location().x,
                          actor.get_location().y - vehicle.get_location().y)
        if dist < min_dist:
            min_dist = dist
    if min_dist < 15:
        print(f"⚠️  跟车距离过近，当前距离：{min_dist:.1f}m，请保持安全车距")
    return min_dist