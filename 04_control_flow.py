# 1. 条件判断实战：模拟毕设中的智能体初始化与速度检查 (对应毕设 if 逻辑)
# =====================================================================
print("--- 🚦 1. 条件分支 (if/else) 模拟机器人决策 ---")

# 模拟变量
navdp_navigator = None  # 设为 None 代表智能体还没诞生
current_speed = 0.8    # 当前小车速度 (m/s)

# 模拟毕设第 26 行：判断智能体状态
if navdp_navigator is None:
    print("[系统提示]检测到智能体未初始化，正在为你加载 LoGoPlanner 模型...")
    navdp_navigator = "智能体已就为"
else:
    print("[系统提示] 智能体已经处于运行状态，无需重复加载。")

# 模拟毕设第 85 行：速度限幅判断
if current_speed > 0.8:
    print("⚠️ 警告：当前线速度超过安全阈值！正在触发自动刹车减速...")
    current_speed = 0.8
elif current_speed < 0.1:
    print("ℹ️ 提示：速度过慢，底盘可能处于静止或微动状态。")
else:
    print(f"✅ 状态正常：当前巡航速度为 {current_speed} m/s，安全。")

print("\n" + "="*40 + "\n")

# 2. 循环结构实战：模拟毕设 MPC 控制器的迭代求解 (对应毕设 for 循环)
# =====================================================================
print("--- 🔄 2. 循环结构 (for loop) 模拟 MPC 迭代优化 ---")

max_steps = 5 # 为了演示，我们将最大迭代次数设为 5 次 (毕设里是20次)
current_pos = 0.0
end_pos = 0.22 # 假设目标终点在这个位置

# range(max_steps) 会自动生成一个从 0 到 4 的数字序列
for i in range(max_steps):
    print(f"🌀 [第 {i+1} 次迭代] 正在使用 MPC 算法求解最优控制量...")

    # 模拟小车向前挪动一步
    current_pos += 0.05
    print(f"   -> 当前小车坐标移动到了: {current_pos:.2f}")

    # 模拟毕设第 107 行：提前收敛退出条件
    # 如果当前位置与终点的距离小于 0.05 米，就提前结束循环！
    if abs(current_pos - end_pos) < 0.05: #abs(...) （绝对值函数，清除正负号）
        print(f"🎯 [提前达标] 距离终点仅剩 {abs(current_pos - end_pos):.3f}m，小于阈值，跳出循环！")
        break  # break 的作用是强行终止整个循环