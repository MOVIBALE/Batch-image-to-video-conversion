import os
import cv2

# 图片文件夹路径
image_folder = "images"
# 输出视频文件
video_file = "output.mp4"
# 视频帧率
fps = 30
# 视频分辨率
frame_size = (696, 1200)

# 创建视频写入器
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
video_writer = cv2.VideoWriter(video_file, fourcc, fps, frame_size)

# 遍历图片文件夹并读取图片
images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
images.sort()
for image in images:
    image_path = os.path.join(image_folder, image)
    img = cv2.imread(image_path)

    # 如果图片读取失败，则跳过该图片
    if img is None:
        continue

    # 调整图片尺寸并写入视频
    img = cv2.resize(img, frame_size)
    video_writer.write(img)

# 释放视频写入器并关闭输出文件
video_writer.release()
