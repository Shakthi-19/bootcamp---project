import hashlib
result = hashlib.md5(b'Shakthi')
print("the equaivalent byte is: ", end="")
print(result.digest())
