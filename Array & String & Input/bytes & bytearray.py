w=b"\x74\x61\x69\x70\x65\x69"
print(w)
a=bytes.fromhex("746169706569")
print(a)
print(type(a))
bytearr = bytearray(a)
print(bytearr)
print(type(bytearr))
bytearr.pop()
print(bytearr)
bytearr.pop()
print(bytearr)
bytearr.pop()
print(bytearr)
bytearr.append(110)
print(bytearr)
bytearr.append(97)
print(bytearr)
bytearr.append(ord("n"))
print(bytearr)

w=b"abc"
print(w[0])
print(type(w[0]))
print(w[:1])
print(type(w[:1]))