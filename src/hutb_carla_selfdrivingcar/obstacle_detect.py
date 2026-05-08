import math

def check_front_obstacle(vehicle, world):
    for actor in world.get_actors().filter("vehicle.*"):
        if actor.id == vehicle.id:
            continue
        dx = actor.get_location().x - vehicle.get_location().x
        dy = actor.get_location().y - vehicle.get_location().y
        dist = math.sqrt(dx**2 + dy**2)
        if dist < 10:
            return True
    return False