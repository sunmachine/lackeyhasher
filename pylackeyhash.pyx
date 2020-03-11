cdef extern from "src/lackeyhash.h":
    cdef int c_get_file_hash(char *filepath)

def get_file_hash(filepath: str) -> int:
    by: bytes = filepath.encode()
    return c_get_file_hash(by)