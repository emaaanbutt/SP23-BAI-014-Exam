import os
import time
from PIL import Image, ImageDraw, ImageFont

def process_images(input_folder, output_folder):
    start_time = time.time()

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for class_name in os.listdir(input_folder):
        class_path = os.path.join(input_folder, class_name)

        if os.path.isdir(class_path):
            output_class_path = os.path.join(output_folder, class_name)
            if not os.path.exists(output_class_path):
                os.makedirs(output_class_path)

            for img_name in os.listdir(class_path):
                img_path = os.path.join(class_path, img_name)

                try:
                    img = Image.open(img_path)

                    img = img.resize((128, 128))

                    draw = ImageDraw.Draw(img)
                    font = ImageFont.load_default()
                    watermark_text = "Watermark"
                    draw.text((5, 5), watermark_text, fill=(255, 255, 255), font=font)

                    output_img_path = os.path.join(output_class_path, img_name)
                    img.save(output_img_path)

                except Exception as e:
                    print(f"Error processing {img_path}: {e}")

    end_time = time.time()
    print(f"Sequential Processing Time: {round(end_time - start_time, 2)} seconds")


if __name__ == "__main__":
    input_dir = "images_dataset"
    output_dir = "output_seq"
    process_images(input_dir, output_dir)
