from PIL import Image
import os

def resize_images(input_folder, output_folder, target_width, target_height):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all files in the input folder
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp'))]

    for image_file in image_files:
        try:
            # Open the image file
            img = Image.open(os.path.join(input_folder, image_file))

            # Calculate the new dimensions while maintaining aspect ratio
            width, height = img.size
            if width / target_width > height / target_height:
                new_width = target_width
                new_height = int(height * (target_width / width))
            else:
                new_width = int(width * (target_height / height))
                new_height = target_height

            # Resize the image
            img = img.resize((new_width, new_height), Image.LANCZOS)

            # Save the resized image to the output folder
            output_path = os.path.join(output_folder, image_file)
            img.save(output_path)

            print(f"Resized {image_file} to {new_width}x{new_height}")
        except Exception as e:
            print(f"Error processing {image_file}: {e}")

if __name__ == "__main__":
    input_folder = "C:\\Users\\91773\\Downloads\\image_resize_input"
    output_folder = "C:\\Users\\91773\\Documents\\image_resize_output"
    target_width = int(input("enter the new width"))
    target_height = int(input("enter the new height"))

    resize_images(input_folder, output_folder, target_width, target_height)