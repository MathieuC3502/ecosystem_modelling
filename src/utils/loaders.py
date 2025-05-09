import pygame

def load_png(name):
    """Loads a PNG image as a pygame Sprite and returns the image and its bounding box

    Args:
        name (string): Filepath of the image to load

    Raises:
        SystemExit: Raised when the Image can't be loaded

    Returns:
        image: Sprite of the image
        bounding_box: PyGame bounding box of the image (image.get_rect)
    """
    try:
        image = pygame.image.load(name)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error as message:
        print(f'Cannot load image: {name}')
        raise SystemExit(message)
    return image, image.get_rect()
