from PIL import Image, ImageFilter

def image_enhancement(path):
    imageObject = Image.open(path)

    sharpened = imageObject.filter(ImageFilter.SHARPEN)
    sharpened_more = sharpened.filter(ImageFilter.SHARPEN)
    sharpened_more.save(path, 'JPEG')

    enhanced_image = imageObject.filter(ImageFilter.EDGE_ENHANCE)
    enhanced_image.save(path, 'JPEG')
    return print("The image has been enhanced")