import pycuda.autoinit
import pycuda.driver as cuda
from pycuda.compiler import SourceModule
import numpy as np

# CUDA kernel code
cuda_kernel_code = """
__global__ void add_vectors(float *a, float *b, float *result, int size) {
    int idx = threadIdx.x + blockIdx.x * blockDim.x;
    if (idx < size) {
        result[idx] = a[idx] + b[idx];
    }
}
"""

# Compile the CUDA kernel
mod = SourceModule(cuda_kernel_code)

# Get the compiled function
cuda_add_vectors = mod.get_function("add_vectors")

def add_vectors_on_gpu(a, b):
    size = len(a)

    # Allocate GPU memory
    a_gpu = cuda.mem_alloc(a.nbytes)
    b_gpu = cuda.mem_alloc(b.nbytes)
    result_gpu = cuda.mem_alloc(b.nbytes)

    # Transfer data from CPU to GPU
    cuda.memcpy_htod(a_gpu, a)
    cuda.memcpy_htod(b_gpu, b)

    # Define grid and block dimensions
    block_size = 256
    grid_size = (size + block_size - 1) // block_size

    # Launch the CUDA kernel
    cuda_add_vectors(a_gpu, b_gpu, result_gpu, np.int32(size), block=(block_size, 1, 1), grid=(grid_size, 1))

    # Allocate space for the result on the CPU
    result = np.empty_like(a)

    # Transfer the result from GPU to CPU
    cuda.memcpy_dtoh(result, result_gpu)

    # Free GPU memory
    a_gpu.free()
    b_gpu.free()
    result_gpu.free()

    return result

# Example usage
a = np.array([1.0, 2.0, 3.0], dtype=np.float32)
b = np.array([4.0, 5.0, 6.0], dtype=np.float32)

result = add_vectors_on_gpu(a, b)
print("Result:", result)
