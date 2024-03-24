import cv2
import json


# openCV处理图片
def openCV_image(image_path, resp_text):
    # 读取图片
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Unable to load image.")
        return []  # 如果图片加载失败，返回空列表

    # 解析JSON数据
    data = json.loads(resp_text)
    detection_classes = data["detection_classes"]
    detection_boxes = data["detection_boxes"]
    detection_scores = data["detection_scores"]

    # 初始化目标列表来存储信息
    targets = []

    # 遍历检测框，绘制矩形并提取信息
    for i, (box, cls, score) in enumerate(zip(detection_boxes, detection_classes, detection_scores)):
        # 置信度大于50%的条件检查
        if score > 0.5:
            # 绘制矩形框
            x, y, w, h = int(box[0]), int(box[1]), int(box[2] - box[0]), int(box[3] - box[1])
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # 提取并存储目标信息
            targets.append({
                'class': cls,
                'score': score,
                'box': (x, y, x + w, y + h)
            })

    # 如果需要，保存带有边界框的图片
    cv2.imwrite('chuli.jpg', image)

    # 返回目标列表
    return targets
