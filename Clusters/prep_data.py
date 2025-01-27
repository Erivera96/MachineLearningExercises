from imports import *
CWD = os.getcwd()

def PrepData(data, number_of_labels, number_of_images_per_label):

    print("Prepping the data...")

    #convert the data to an array
    data_array = np.array(data)

    # get the labels from the data (assuming first col are labels)
    labels = np.array(data)[:,0]

    # to make sure we get the number of labels we want
    labels_included = []
     
    # we include 10 of each label we want
    for i in range(number_of_labels):
        labels_included.extend([j for j in range(len(labels)) if labels[j] == i][:number_of_images_per_label])

    # shuffle the aquired labels, seed it to get same results
    r.seed(7)
    r.shuffle(labels_included)

    labels_included = np.array(labels_included)
     
    # don't want to give the algo the labels so extract them
    return data_array[labels_included,0], data_array[labels_included, 1:]

def CreateImages(data_array):
    
    print("Creating images...")

    number_of_images = data_array.shape[0]

    # convert 2d array into 3d array and cast values to uint8
    data_matrix = np.array([data_array[i,:].reshape(28,28) for i in range(number_of_images)], dtype=np.uint8)
    
    print("Saving images....")
    
    # convert all the 2d arrays from data_matrix and save them as .png
    # MAKE SURE TO HAVE mnist_images DIRECTORY CREATED FIRST
    for i in range(number_of_images):
        png.from_array(data_matrix[i,:,:], mode="L").save('{}/mnist_images/img{}.png'.format(CWD,i))
    
    return

def BinaryThresholding(data_array):

    print("Turning to binary...")

    number_of_images = data_array.shape[0]
    
    # get all the location and names for the images
    image_titles = ['{}/mnist_images/img{}.png'.format(CWD,i) for i in range(number_of_images)]
    binary_data_array = []
    
    # read in each image and preform binary image thresholding on it 
    # (black and dark grays turn black, white and light gray turn white)
    for i in range(number_of_images):
        image = np.array(Image.open(image_titles[i]).convert('L'))
        binary_data_array.append(Threshold(image))
    
    binary_data_array = np.array(binary_data_array)

    # reshape to original data size
    binary_data_array = np.array([binary_data_array[i,:,:].reshape(28*28) for i in range(number_of_images)])

    return binary_data_array

def Threshold(image, threshold=128, max_val=255):
    
    bool_vals = (image > threshold)
    binary_image = bool_vals * max_val

    return binary_image

def ReduceImage(): # (work in progress)
    
    return
