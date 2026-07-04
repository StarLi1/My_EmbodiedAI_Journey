# 1. 列表实战：模拟 MPC 控制器的轨迹记录 (对应毕设 x_history)
# =====================================================================
print("--- 🛣️ 1. 列表 (List) 模拟机器人轨迹历史 ---")

# 创建一个初始列表，里面放着初始坐标 [X, Y]
x_history = [[0.0,0.0]]
print(f"机器人出发点：{x_history}")

# 模拟机器人向前移动，使用 .append() 动态追加新的位置快照\
x_history.append([0.2,0.1])
x_history.append([0.4,0.2])
x_history.append([0.6,0.3])

print(f"完整行驶轨迹：{x_history}")
print(f"机器人当前走到了第{len(x_history)}个位置点")
print(f"单独取出第1步的坐标（注意索引从0开始）：{x_history[1]}")
print("\n"+"="*40+"\n")

# 2. 字典实战：模拟接收到的网络目标点数据 (对应毕设 goal_data)
# =====================================================================
print("--- 🎯 2. 字典 (Dict) 结构化管理目标点数据 ---")
goal_data = {
    "goal_x": 1.5,
    "goal_y": 2.8,
    "frame_id": "map",
    "is_reached": False
}
print(f"收到的完整目标信息字典: {goal_data}")

# 通过 键(Key) 精准提取我们想要的内容
current_goal_x = goal_data["goal_x"]
current_goal_y = goal_data["goal_y"]
print(f"解析成功 -> 机器人应该向地图上的 X: {current_goal_x}, Y: {current_goal_y} 导航前进！")

# 甚至可以动态修改字典里的状态
goal_data["is_reached"] = True
print(f"更新后的目标状态：{goal_data['is_reached']}")