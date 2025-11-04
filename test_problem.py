def decode_utf8_bytes_to_str_wrong(bytestring: bytes):
    print("bytest")
    return "".join([bytes(bytestring).decode("utf-8")])

res=decode_utf8_bytes_to_str_wrong("hell o".encode("utf-8"))
print(res)
res2=decode_utf8_bytes_to_str_wrong("你好".encode("utf-8"))
print(res2) 

print(bytes([000,245]).decode("utf-8"))