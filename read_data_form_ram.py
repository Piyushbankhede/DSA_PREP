import ctypes

x = 5
address = id(x)

# Proper way to get the integer value from the Python object
value = ctypes.pythonapi.PyLong_AsLong(ctypes.py_object(x))

print(f"Memory Address of x: {hex(address)}")
print(f"Correct Value at address {hex(address)}: {value}")
