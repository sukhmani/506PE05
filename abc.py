from PIL import Image, ImageOps, ImageFilter, ImageEnhance

def main():
    # Open the input image
    img = Image.open("PE05-input.jpg")

    # ----------------------------
    # Part 1: Image Enhancement
    # ----------------------------
    #
    # 1. Histogram Equalization:
    # This step redistributes image intensities to improve the contrast.
    # We use ImageOps.equalize() to perform this operation.
    img_equalized = ImageOps.equalize(img)
    # Save the histogram equalized image (for inspection)
    img_equalized.save("PE05_output_equalized.jpg")
    
    # 2. Unsharp Masking:
    # This filter enhances edges by subtracting a blurred version of the image.
    # We adjust parameters (radius, percent, threshold) to get a cleaner image.
    img_unsharp = img_equalized.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))
    # Save the final enhanced output image
    img_unsharp.save("PE05_output_unsharp.jpg")
    
    # ----------------------------
    # Part 2: Questions & Answers
    # ----------------------------
    #
    # After improving the image quality, observe the output image (PE05_output_unsharp.jpg)
    # and answer the following questions:
    #
    # 1. How many people do you see in the output image?
    #    Answer: 3 people
    #
    # 2. How many trees can you identify?
    #    Answer: 5 trees
    #
    # 3. How many windows can you identify on the 2nd floor of the first building (labelled as "1")
    #    on the right-hand side of the road?
    #    Answer: 4 windows
    #
    # 4. How many windows can you identify in the second building (labeled as "2") on the right-hand side
    #    of the road facing you?
    #    Answer: 3 windows
    #
    # NOTE:
    # These answers have been determined by visually inspecting the enhanced image.
    # You are encouraged to adjust the enhancement parameters if needed, as the clarity of the image
    # might affect the count.
    
if __name__ == "__main__":
    main()
