# 06_classes_and_objects.py
import numpy as np

# =====================================================================
# 1. 声明“智能体大脑类” (完美高仿 policy_agent.py 里的图纸)
# =====================================================================
class ToyLoGoPlannerAgent:
    # 构造函数：开机配置向导
    # image_intrinsic 后面没有等号，代表必须由主程序手动传入
    # 其他三个参数有等号，代表有默认值
    def __init__(self, image_intrinsic, image_size=224, memory_size=8, device='cuda:0'):
        # 核心动作：用 self. 把参数死死刻在这个刚诞生的实体骨头上
        self.image_intrinsic = image_intrinsic
        self.image_size = image_size
        self.memory_size = memory_size
        self.device = device
        
        print(f"🧠 [大脑实体已诞生] 成功绑定计算芯片: {self.device}")
        print(f"   -> 视觉裁剪分辨率设为: {self.image_size}x{self.image_size}")
        print(f"   -> 历史时间序列记忆步长锁死为: {self.memory_size} 帧")
        print(f"   -> 相机内参成功刷入，当前内参矩阵为:\n{self.image_intrinsic}")

    # 方法：绑定在大脑实体身上的数据加工厂
    def step_pointgoal(self, image, depth):
        print("\n⚡ [大脑正在高速思考推理中...]")
        # 模拟大脑在后台默默翻阅自己身体里存着的硬件内参
        print(f"   [读取状态] 正在调用 {self.device} 显卡资源...")
        print(f"   [数学转换] 正在利用体内的小车相机内参，将 2D 像素画面反投影为 3D 物理空间...")
        
        # 假装经过了复杂的 Transformer 矩阵乘法，最终加工出一条推荐的行驶轨迹
        simulated_trajectory = [[0.0, 0.0], [0.1, 0.05], [0.2, 0.10]]
        
        # 把加工完的最终数据成果“吐出去”给主程序
        return simulated_trajectory


# =====================================================================
# 2. 主程序运行：模拟服务器接收网络数据、实例化并调用 (高仿 server 端)
# =====================================================================
print("--- 🌐 欢迎来到具身智能大脑「面向对象」全景演练 ---\n")

# 场景模拟：此时实体小车开机了，通过局域网给服务器发来了一串它相机自带的内参矩阵数字
# 这是一个经典的 3x3 相机内参矩阵数字（代表焦距和中心点）
camera_hardware_matrix = np.array([
    [525.0,   0.0, 319.5],
    [  0.0, 525.0, 239.5],
    [  0.0,   0.0,   1.0]
])

print("📬 [网络接收] 服务器成功收到小车发来的物理相机内参数据。")
print("🏭 [开始生产] 准备根据图纸创造专属的大脑实体对象...")

# 实例化对象：把上面刚收到的相机内参传进去
# 我们故意不传 image_size 和 memory_size，让它自动去使用图纸里的默认值 224 和 8
navdp_navigator = ToyLoGoPlannerAgent(image_intrinsic=camera_hardware_matrix)

print("\n" + "="*50)

# 模拟机器人运行循环：摄像头拍到了画面，扔给对象去加工
print("\n📸 [流式数据输入] 摄像头抓拍到一帧新的图像和深度图...")
current_image = "Fake_RGB_Image_Data"
current_depth = "Fake_Depth_Image_Data"

# 呼叫对象身上的加工厂方法，灌入图像，等待它吐出轨迹
execute_trajectory = navdp_navigator.step_pointgoal(image=current_image, depth=current_depth)

print(f"\n🎯 [加工完成] 服务器成功拿到大脑对象返回的规划轨迹: {execute_trajectory}")
print("🏎️  MPC控制器可以根据这条轨迹去控轮子转速了！")