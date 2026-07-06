# 06_classes_and_objects.py

# =====================================================================
# 1. 声明一个“类” (等同于设计一款机器人底盘的蓝图)
# =====================================================================
class RobotController:
    # 构造函数：每当有一台真正的机器人出厂时，这个函数会自动运行，用来给它“配置初始硬件参数”
    def __init__(self, name, max_vx):
        self.robot_name = name    # 属性 (Attribute)：绑定在实体小车自己身上的名字
        self.vx_limit = max_vx    # 属性 (Attribute)：绑定在实体小车自己身上的限速值
        self.current_vx = 0.0     # 属性 (Attribute)：初始速度默认是 0
        print(f"🎉 成功根据蓝图造出了一台实体小车，名字叫：[{self.robot_name}]")

    # 方法 (Method)：绑定在小车身上的加工函数，负责控制小车加速
    def accelerate(self, increment):
        # 这里的 self.current_vx 代表改变“小车自己”的当前速度
        self.current_vx += increment
        
        # 结合前面学的条件判断，进行速度限幅 (模拟你的毕设 MPC 限速逻辑)
        if self.current_vx > self.vx_limit:
            self.current_vx = self.vx_limit
            print(f"⚠️ [{self.robot_name}] 已经达到限幅最大速度：{self.current_vx} m/s")
        else:
            print(f"🚀 [{self.robot_name}] 正在加速，当前速度：{self.current_vx} m/s")


# =====================================================================
# 2. 实例化“对象” (真正根据蓝图在生产线上造出两台不同属性的实体小车)
# =====================================================================
print("--- 🏭 机器人面向对象 (OOP) 实战演练 ---\n")

# 造第一台小车：叫 LogoBot，安全限速 0.5 m/s (对应毕设初始化)
robot_1 = RobotController(name="LogoBot", max_vx=0.5)

# 造第二台小车：叫 OmniBot，性能更好，安全限速 1.2 m/s
robot_2 = RobotController(name="OmniBot", max_vx=1.2)

print("\n" + "="*20 + " 🎮 开始下发控制指令 " + "="*20 + "\n")

# 场景：两台小车互相独立，各自执行自己的加速动作
print("-> 指令：命令两台小车同时加速 0.4 m/s")
robot_1.accelerate(0.4)  # 运行结果应该是 0.4
robot_2.accelerate(0.4)  # 运行结果应该是 0.4
print("-" * 40)

print("-> 指令：命令两台小车再次加速 0.4 m/s")
robot_1.accelerate(0.4)  # 触发限幅，被压制回 0.5
robot_2.accelerate(0.4)  # 正常加速到 0.8