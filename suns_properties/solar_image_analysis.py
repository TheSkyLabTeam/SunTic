from image_services import calculate_probabilities
import numpy as np

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