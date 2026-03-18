import os, sys

__all__=['get_exe', 'get_dir']

def get_dir(path: str):
    """:param path: просто напишите __file__"""
    return os.path.dirname(os.path.abspath(path))

def get_exe(path: str):
    """:param path: просто напишите __file__"""
    if getattr(sys, 'frozen', False): return os.path.dirname(sys.executable)
    return get_dir(path)