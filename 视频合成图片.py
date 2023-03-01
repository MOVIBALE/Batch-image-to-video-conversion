import os
import cv2
import tkinter as tk
from tkinter import filedialog

class VideoConverter:
    def __init__(self, master):
        self.master = master
        master.title("Video Converter")

        # 添加选择文件夹按钮
        self.select_folder_button = tk.Button(master, text="选择文件夹", command=self.select_folder)
        self.select_folder_button.pack()

        # 添加帧率输入框
        self.fps_label = tk.Label(master, text="帧率:")
        self.fps_label.pack()
        self.fps_entry = tk.Entry(master)
        self.fps_entry.insert(0, "30")
        self.fps_entry.pack()

        # 添加分辨率输入框
        self.frame_size_label = tk.Label(master, text="分辨率(宽x高):")
        self.frame_size_label.pack()
        self.frame_size_entry = tk.Entry(master)
        self.frame_size_entry.insert(0, "696x1200")
        self.frame_size_entry.pack()

        # 添加转换按钮
        self.convert_button = tk.Button(master, text="转换", command=self.convert)
        self.convert_button.pack()

    def select_folder(self):
        self.image_folder = filedialog.askdirectory()
        print("选择文件夹: ", self.image_folder)

    def convert(self):
        # 获取帧率和分辨率
        fps = int(self.fps_entry.get())
        frame_size = tuple(map(int, self.frame_size_entry.get().split('x')))
        print("帧率: ", fps)
        print("分辨率: ", frame_size)

        # 创建视频写入器
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        video_writer = cv2.VideoWriter("output.mp4", fourcc, fps, frame_size)

        # 遍历图片文件夹并读取图片
        images = [img for img in os.listdir(self.image_folder) if img.endswith(".jpg")]
        images.sort()
        for image in images:
            image_path = os.path.join(self.image_folder, image)
            img = cv2.imread(image_path)

            # 如果图片读取失败，则跳过该图片
            if img is None:
                continue

            # 调整图片尺寸并写入视频
            img = cv2.resize(img, frame_size)
            video_writer.write(img)

        # 释放视频写入器并关闭输出文件
        video_writer.release()
        print("生成视频完成")

root = tk.Tk()
video_converter = VideoConverter(root)
root.mainloop()
