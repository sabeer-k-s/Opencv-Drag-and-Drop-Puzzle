import cv2
def divide_image_into_9_squares(image_path):
    # Load the image
    image = cv2.imread(image_path)
    
    # Get the dimensions of the image
    height, width, _ = image.shape
    
    # Ensure the image dimensions are divisible by 3
    if height % 3 != 0 or width % 3 != 0:
        raise ValueError("Image dimensions must be divisible by 3 for equal squares.")
    
    # Calculate the size of each square piece
    piece_height = height // 3
    piece_width = width // 3
    
    # List to hold the 9 pieces
    pieces = []
    
    # Loop through the image and extract the 9 pieces
    for i in range(3):
        for j in range(3):
            # Calculate the coordinates of the current piece
            y0, y1 = i * piece_height, (i + 1) * piece_height
            x0, x1 = j * piece_width, (j + 1) * piece_width
            
            # Extract the piece
            piece = image[y0:y1, x0:x1]
            pieces.append(piece)
            
            # Save the piece as an image file
            piece_filename = f"piece_{i}_{j}.png"
            cv2.imwrite(piece_filename, piece)
    
    return pieces

pieces = divide_image_into_9_squares('puzzle.jpg')
