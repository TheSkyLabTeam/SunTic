from image_services import calculate_probabilities
import numpy as np
import cv2


def compute_entropy(image: np.ndarray) -> float:
    """
    Compute the entropy of an image.
    
    The entropy is a statistical measure of randomness that 
    can be used to characterize the texture of an input image.

    Parameters
    ----------
    image : np.ndarray
        Input image data. Will be converted to float.

    Returns
    -------
    entropy : float
        Calculated entropy.
        
    """
    # Calculate the probabilities
    probabilities = calculate_probabilities(image)
    
    # Exclude zero probabilities
    probabilities = probabilities[probabilities != 0]
    
    # Compute entropy
    entropy = -np.sum(probabilities * np.log2(probabilities))
    
    return entropy

def compute_mean_intensity(image: np.ndarray) -> float:
    """
    Compute the mean intensity of an image.
    
    The mean intensity is a measure that 
    represents the average level of brightness of the image.

    Parameters
    ----------
    image : np.ndarray
        Input image data. Will be converted to float.

    Returns
    -------
    mean_intensity : float
        Calculated mean intensity.
        
    """
    # Calculate the probabilities
    probabilities = calculate_probabilities(image)
    
    # Compute the pixel intensities
    intensities = np.arange(256)
    
    # Compute mean intensity
    mean_intensity = np.sum(intensities * probabilities)
    
    return mean_intensity

def compute_standard_deviation(image: np.ndarray) -> float:
    """
    Compute the standard deviation of the pixel intensity of an image.
    
    The standard deviation is a measure that 
    represents the dispersion of the pixel intensities in the image.

    Parameters
    ----------
    image : np.ndarray
        Input image data. Will be converted to float.

    Returns
    -------
    standard_deviation : float
        Calculated standard deviation of pixel intensity.
        
    """
    # Calculate the probabilities
    probabilities = calculate_probabilities(image)
    
    # Compute the pixel intensities
    intensities = np.arange(256)
    
    # Compute mean intensity
    mean_intensity = compute_mean_intensity(image)
    
    # Compute standard deviation
    standard_deviation = np.sqrt(np.sum(probabilities * (intensities - mean_intensity)**2))
    
    return standard_deviation

def compute_fractal_dimension(image: np.ndarray, threshold: float=0.5) -> float:
    """
    Computes the fractal dimension of a 2D grayscale image using the box-counting method.
    
    Parameters
    ----------
    image : np.ndarray
        2D input image data. Will be converted to grayscale if not already.
    threshold : float, optional
        Threshold to convert the grayscale image to binary, by default 0.5.

    Returns
    -------
    fractal_dimension : float
        Calculated fractal dimension of the image.
    """
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    assert(len(image.shape) == 2)# "image must be 2D"
    

    # Binarize the image using the given threshold
    image = image < threshold
    
    # Define the boxcount function
    def boxcount(Z, k):
        S = np.add.reduceat(np.add.reduceat(Z, np.arange(0, Z.shape[0], k), axis=0), np.arange(0, Z.shape[1], k), axis=1)
        return np.count_nonzero((0 < S) & (S < k*k))

    # Define the box sizes
    p = min(image.shape)
    n = int(np.floor(np.log2(p)))
    sizes = 2**np.arange(n, 1, -1)

    # Count the number of boxes for each size
    counts = [boxcount(image, size) for size in sizes]

    # Perform a linear fit (y = ax + b) to the sizes and counts
    coeffs = np.polyfit(np.log(sizes), np.log(counts), 1)

    # Return the fractal dimension (-a)
    return -coeffs[0]

def compute_skewness(image: np.ndarray) -> float:
    """
    Compute the skewness of an image.

    The skewness is a measure of the asymmetry of the probability distribution
    of a real-valued random variable about its mean. Skewness can be positive or negative,
    or undefined, and it quantifies the extent and direction of skew (departure from horizontal symmetry).
    
    Parameters
    ----------
    image : np.ndarray
        Input image data. Will be converted to float.

    Returns
    -------
    skewness : float
        Calculated skewness of the image pixel intensity distribution.
        
    """
    # Calculate the probabilities
    probabilities = calculate_probabilities(image)
    
    # Compute the pixel intensities
    intensities = np.arange(256)

    # Compute mean intensity
    mean_intensity = compute_mean_intensity(image)

    # Compute standard deviation
    standard_deviation = compute_standard_deviation(image)

    # Compute skewness
    skewness = (1/standard_deviation**3)*(np.sum(probabilities * (intensities - mean_intensity)**3))

    return skewness

def compute_kurtosis(image: np.ndarray) -> float:
    """
    Compute the kurtosis of an image.

    The kurtosis is a measure of the "tailedness" of the probability distribution
    of a real-valued random variable. In particular, kurtosis quantifies the extent
    to which a distribution shows a peaked or flat shape.

    Parameters
    ----------
    image : np.ndarray
        Input image data. Will be converted to float.

    Returns
    -------
    kurtosis : float
        Calculated kurtosis of the image pixel intensity distribution.
        
    """
    # Calculate the probabilities
    probabilities = calculate_probabilities(image)
    
    # Compute the pixel intensities
    intensities = np.arange(256)

    # Compute mean intensity
    mean_intensity = compute_mean_intensity(image)

    # Compute standard deviation
    standard_deviation = compute_standard_deviation(image)

    # Compute kurtosis
    kurtosis = (1/standard_deviation**4)*(np.sum(probabilities * (intensities - mean_intensity)**4)) - 3

    return kurtosis

def compute_uniformity(image: np.ndarray) -> float:
    """
    Compute the uniformity of an image.

    The uniformity is a measure of the texture of an image. It measures the sum of 
    the squares of the pixel intensities, normalized to be in the range [0, 1]. 
    A value close to 1 indicates an image with low variation in pixel intensities 
    (like a completely black or white image), while a value close to 0 indicates 
    high variation in pixel intensities.

    Parameters
    ----------
    image : np.ndarray
        Input image data. Will be converted to float.

    Returns
    -------
    uniformity : float
        Calculated uniformity of the image pixel intensity distribution.
        
    """
    # Calculate the probabilities
    probabilities = calculate_probabilities(image)

    # Compute uniformity
    uniformity =  np.sum(probabilities**2)

    return uniformity

def compute_relative_smoothness(image: np.ndarray) -> float:
    """
    Compute the relative smoothness of an image.
    
    The relative smoothness is a measure of variation in the pixel intensity levels.

    Parameters
    ----------
    image : np.ndarray
        Input image data. Will be converted to float.

    Returns
    -------
    relative_smoothness : float
        Calculated relative smoothness.
        
    """
    # Compute standard deviation
    sigma = compute_standard_deviation(image)

    # Compute relative smoothness
    relative_smoothness = 1 - (1 / (1 + sigma**2))

    return relative_smoothness







