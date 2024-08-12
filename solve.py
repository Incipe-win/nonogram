import pytesseract
from PIL import Image
import numpy as np


def extract_clues_from_image(image_path):
    """
    从图片中提取数织游戏的行和列线索
    :param image_path: 包含线索的图片路径
    :return: 一个包含行线索和列线索的元组
    """
    # 加载图片并进行预处理（比如调整对比度、阈值等）
    img = Image.open(image_path).convert("L")  # 转换为灰度
    img = img.point(lambda x: 0 if x < 128 else 255, "1")  # 二值化处理

    # 使用Tesseract进行OCR识别
    text = pytesseract.image_to_string(img, config="--psm 6")

    # 这里简化处理，假设线索之间以特定字符分隔（例如逗号或空格），实际情况可能需要更复杂的解析逻辑
    clues_text = text.replace("\n", ",")  # 假设每行线索后换行，这里先统一用逗号分隔
    clues_list = list(
        map(int, filter(None, clues_text.split(",")))
    )  # 分割并转换为整数列表

    # 假设我们知道线索的总数（或可以通过某种方式推断），这里简化处理，未实现动态确定行列
    total_clues = len(clues_list)
    side = int(np.sqrt(total_clues))  # 假设线索均匀分布于行和列，简化处理
    if side * side != total_clues:
        raise ValueError("线索数量不能构成完美的正方形，请检查图片或处理逻辑")

    # 分割线索为行线索和列线索
    row_clues = clues_list[:side]
    col_clues = clues_list[side:]

    print(row_clues)
    print(col_clues)
    return row_clues, col_clues


extract_clues_from_image("./nonogram.jpg")
