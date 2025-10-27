import os
import time
from PIL import Image, ImageDraw, ImageFont
from multiprocessing import Pool

input_folder = "images_dataset"
output_folder = "output_parallel"


def process_one_image(args):
    img_path, output_img_path = args

    try:
        img = Image.open(img_path)

        # Resize
        img = img.resize((128, 128))

        # Watermark
        draw = ImageDraw.Draw(img)
        font = ImageFont.load_default()
        draw.text((5, 5), "Watermark", fill=(255, 255, 255), font=font)

        img.save(output_img_path)
        return True
    except:
        return False


def get_all_image_paths():
    image_pairs = []

    for class_name in os.listdir(input_folder):
        class_path = os.path.join(input_folder, class_name)

        if os.path.isdir(class_path):
            output_class_path = os.path.join(output_folder, class_name)
            os.makedirs(output_class_path, exist_ok=True)

            for img_name in os.listdir(class_path):
                src = os.path.join(class_path, img_name)
                dst = os.path.join(output_class_path, img_name)
                image_pairs.append((src, dst))

    return image_pairs


def run_parallel(workers):
    image_pairs = get_all_image_paths()

    start = time.perf_counter()

    with Pool(processes=workers) as pool:
        pool.map(process_one_image, image_pairs)

    end = time.perf_counter()
    return round(end - start, 2)


if __name__ == "__main__":
    os.makedirs(output_folder, exist_ok=True)

    worker_list = [1, 2, 4, 8]
    times = {}

    print("\nRunning Parallel Processing...\n")

    for w in worker_list:
        t = run_parallel(w)
        times[w] = t
        print(f"Workers: {w} → Time: {t} seconds")

    print("\nWorkers | Time (s) | Speedup")
    print("-----------------------------")

    base_time = times[1]
    for w in worker_list:
        speedup = round(base_time / times[w], 2)
        print(f"{w:<7} | {times[w]:<7} | {speedup}x")
