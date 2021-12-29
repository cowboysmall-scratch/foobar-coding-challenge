
import base64

mes = "HBMBElcNEQZHQBRIRxMJBhBVExNeRxMNGxlYAlUVElFJVE8UQFEBE1ELGRBQQBhSQFEIEhpGE0dV Rw5OUxxaBEYXA10MGBATSxRVBlcGHRBCAlkXCUBJVE8UQEEcC1sNHxBQQBhSQEYPFhddE0dVRw5O UwZVAVFVSxRJEhpbQBRIRxMZHRsVQEk="
key = "g4rg4ntu4"
res = []

for i, c in enumerate(base64.b64decode(mes)):
    # res.append(chr(ord(key[i % len(key)]) ^ ord(c)))
    res.append(chr(ord(key[i % len(key)]) ^ c))

print(''.join(res))
