def auto_turn_light_tip(steer_angle):
    if steer_angle > 0.05:
        print("💡 车辆左转，左转向灯开启")
    elif steer_angle < -0.05:
        print("💡 车辆右转，右转向灯开启")
    else:
        print("💡 车辆直行，转向灯关闭")