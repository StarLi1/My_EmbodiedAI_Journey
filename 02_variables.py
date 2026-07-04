# 02_variables.py
robot_id = 101                 # 整数 (int)
linear_velocity = 0.25         # 浮点数 (float)
model_name = "LoGoPlanner"     # 字符串 (str)
is_motor_on = True            # 布尔值 (bool)

print("--- 🔍 正在检查机器人运行参数的数据类型 ---")
print(f"机器编号类型: {type(robot_id)}")
print(f"线速度类型: {type(linear_velocity)}")
print(f"模型名称类型: {type(model_name)}")
print(f"电机开关类型: {type(is_motor_on)}")