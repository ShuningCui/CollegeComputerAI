import numpy as np
import matplotlib.pyplot as plt

# 设置中文字体，确保标签正常显示
plt.rcParams["font.family"] = ["SimHei", "WenQuanYi Micro Hei", "Heiti TC"]

# 1. 定义5x5灰度图像矩阵（之前例子中的渐变灰度图）
gray_matrix = np.array([
    [0,   51,  102, 153, 204],
    [51,  102, 153, 204, 255],
    [102, 153, 204, 255, 204],
    [153, 204, 255, 204, 153],
    [204, 255, 204, 153, 102]
], dtype=np.uint8)  # 使用uint8类型表示0-255的像素值

# 2. 定义5x5RGB彩色图像的三个通道矩阵（之前例子中的彩色图）
# 红色通道
r_matrix = np.array([
    [255, 255, 255, 128, 0],
    [255, 255, 128, 0,   0],
    [255, 128, 255, 0,   0],
    [128, 0,   0,   0,   0],
    [0,   0,   0,   0,   0]
], dtype=np.uint8)

# 绿色通道
g_matrix = np.array([
    [0,   0,   0,   128, 255],
    [0,   0,   128, 255, 255],
    [0,   128, 255, 255, 255],
    [128, 255, 255, 255, 255],
    [255, 255, 255, 255, 255]
], dtype=np.uint8)

# 蓝色通道
b_matrix = np.array([
    [0,   0,   0,   0,   255],
    [0,   0,   0,   255, 255],
    [0,   0,   0,   255, 255],
    [0,   0,   0,   255, 255],
    [0,   0,   0,   255, 255]
], dtype=np.uint8)

# 将三个通道合并为RGB图像（需要调整为(行, 列, 3)的形状）
rgb_image = np.stack([r_matrix, g_matrix, b_matrix], axis=-1)

# 创建画布显示两个图像
plt.figure(figsize=(10, 4))

# 显示灰度图像
plt.subplot(1, 2, 1)
plt.imshow(gray_matrix, cmap='gray', vmin=0, vmax=255)
plt.title('5x5灰度图像')
plt.xticks(range(5))  # 显示x轴刻度（0-4）
plt.yticks(range(5))  # 显示y轴刻度（0-4）
plt.grid(color='white', linewidth=1)  # 显示网格线，更清晰地看到每个像素

# 显示RGB彩色图像
plt.subplot(1, 2, 2)
plt.imshow(rgb_image)
plt.title('5x5RGB彩色图像')
plt.xticks(range(5))
plt.yticks(range(5))
plt.grid(color='white', linewidth=1)

plt.tight_layout()
plt.show()
