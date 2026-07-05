# 1. 定义函数 (打造一个“全自动速度裁剪限幅器”)
# =====================================================================
# 用 def 声明函数，括号里的是“输入参数” (raw_speed)
def clip_robot_speed(raw_speed):
    """
    这是一个功能模块：负责检查传入的速度，如果超速就强行裁剪到安全范围。
    """
    max_safe_speed = 0.8 # 对应毕设里 mpc_controller 的 vx_max=0.8

    # 结合第四课的条件判断
    if raw_speed > max_safe_speed:
        safe_speed = max_safe_speed
    elif raw_speed < -max_safe_speed:
        safe_speed = -max_safe_speed
    else:
        safe_speed = raw_speed
    
    # 用 return 把加工好的安全速度“吐出去”
    return safe_speed


# =====================================================================
# 2. 调用函数 (真正把这个硬件插到主程序里运行)
# =====================================================================
print("--- 🤖 2. 函数 (def) 模块化复用实战 ---")

# 场景 A：网络或模型吐出了一个非常危险的超速指令 1.2 m/s
input_speed_A = 1.2
# 就像调用底盘硬件驱动一样，直接把速度扔进函数盒子里
final_speed_A = clip_robot_speed(input_speed_A)

print(f"场景A -> 原始指令速度：{input_speed_A} m/s")
print(f"场景A -> 经过安全函数过滤后的实际下发速度：{final_speed_A} m/s（成功限幅）")
print("-"*40)

# 场景 B：模型吐出了一个安全的巡航速度 0.35 m/s
input_speed_B = 0.35
final_speed_B = clip_robot_speed(input_speed_B)

print(f"场景 B -> 原始指令速度: {input_speed_B} m/s")
print(f"场景 B -> 经过安全函数过滤后的实际下发速度: {final_speed_B} m/s (安全放行)")