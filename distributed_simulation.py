import os
import time
from multiprocessing import Process, Manager
from PIL import Image, ImageDraw, ImageFont

input_folder = "images_dataset"
output_folder = "output_distributed"


def process_node(images, node_id, return_dict):
    start = time.perf_counter()

    for src_path, dst_path in images:
        try:
            img = Image.open(src_path)
            img = img.resize((128, 128))

            draw = ImageDraw.Draw(img)
            font = ImageFont.load_default()
            draw.text((5, 5), "Watermark", fill=(255, 255, 255), font=font)

            img.save(dst_path)

        except:
            pass

    end = time.perf_counter()
    node_time = round(end - start, 2)
    return_dict[node_id] = (len(images), node_time)


def get_all_image_paths():
    pairs = []
    for class_name in os.listdir(input_folder):
        class_path = os.path.join(input_folder, class_name)

        if os.path.isdir(class_path):
            out_class_path = os.path.join(output_folder, class_name)
            os.makedirs(out_class_path, exist_ok=True)

            for img_name in os.listdir(class_path):
                pairs.append(
                    (os.path.join(class_path, img_name),
                     os.path.join(out_class_path, img_name))
                )
    return pairs


if __name__ == "__main__":

    os.makedirs(output_folder, exist_ok=True)

    print(f"System CPU Cores Detected: {os.cpu_count()}\n")

    all_images = get_all_image_paths()

    mid = len(all_images) // 2
    node1_data = all_images[:mid]
    node2_data = all_images[mid:]

    manager = Manager()
    result_dict = manager.dict()

    print("Starting Distributed Simulation...\n")

    total_start = time.perf_counter()

    p1 = Process(target=process_node, args=(node1_data, "Node 1", result_dict))
    p2 = Process(target=process_node, args=(node2_data, "Node 2", result_dict))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    total_end = time.perf_counter()
    total_time = round(total_end - total_start, 2)

    images1, time1 = result_dict["Node 1"]
    images2, time2 = result_dict["Node 2"]

    print(f"Node 1 processed {images1} images in {time1}s")
    print(f"Node 2 processed {images2} images in {time2}s")
    print(f"\nTotal Distributed Time: {total_time}s")

    sequential_time = 0.31 
    efficiency = round(sequential_time / total_time, 2)
    print(f"Efficiency: {efficiency}x over sequential")
