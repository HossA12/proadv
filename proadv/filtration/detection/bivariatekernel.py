import numpy as np

def _cutoff(density_profile, velocity_profile, c1_threshold, c2_threshold, force_profile, peak_index, grid):
    grid):
    """
    Find the lower and upper cutoff velocities based on specified criteria.

    Parameters
    ------
        density_profile (array_like): Density profile of the system.
        velocity_profile (array_like): Velocity profile of the system.
        c1_threshold (float): Threshold ratio for force compared to peak force.
        c2_threshold (float): Threshold for absolute change in force.
        force_profile (array_like): Force profile of the system.
        peak_index (int): Index of the peak force in the force profile.
        grid (int): Grid spacing or resolution.

    Returns
    ------
        lower_cutoff_velocity, upper_cutoff_velocity: A tuple containing the lower and upper cutoff velocities.

    Note
    ------
        This function assumes that the input arrays (density_profile, velocity_profile, and force_profile) 
            are of the same length.

    """
    
    profile_length = force_profile.size
    delta_force = np.append([0], np.diff(force_profile)) * grid / density_profile
    
    # Find lower cutoff index
    for i in range(peak_index - 1, 0, -1):
        if force_profile[i] / force_profile[peak_index] <= c1_threshold and abs(delta_force[i]) <= c2_threshold:
            lower_cutoff_index = i
            break
    else:
        lower_cutoff_index = 1

    # Find upper cutoff index
    for i in range(peak_index + 1, profile_length - 1):
        if force_profile[i] / force_profile[peak_index] <= c1_threshold and abs(delta_force[i]) <= c2_threshold:
            upper_cutoff_index = i
            break
    else:
        upper_cutoff_index = profile_length - 1

    lower_cutoff_velocity = velocity_profile[lower_cutoff_index]
    upper_cutoff_velocity = velocity_profile[upper_cutoff_index]
    
    return lower_cutoff_velocity, upper_cutoff_velocity