import os

def validate_path(target_path, working_dir):
    """Ensure the target path is within the working directory."""
    real_target = os.path.realpath(target_path)
    real_working = os.path.realpath(working_dir)
    return real_target.startswith(real_working)

def get_absolute_path(current_dir, relative_path):
    """Convert a relative path to an absolute path based on current directory."""
    return os.path.normpath(os.path.join(current_dir, relative_path))