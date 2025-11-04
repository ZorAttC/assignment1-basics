Problem (unicode1): Understanding Unicode (1 point)
(a) What Unicode character does chr(0) return?
'\x00'
(b) How does this character’s string representation (__repr__()) differ from its printed representa-
tion?
>>> 'my_ass is hurt'.__repr__()
"'my_ass is hurt'"


(c) What happens when this character occurs in text? It may be helpful to play around with the
following in your Python interpreter and see if it matches your expectations:
>>> print("this is a test" + chr(0) + "string")
this is a teststring
chr(0)在print字面上似乎等价于空格



Problem (unicode2): Unicode Encodings (3 points)
(a) What are some reasons to prefer training our tokenizer on UTF-8 encoded bytes, rather than
UTF-16 or UTF-32? It may be helpful to compare the output of these encodings for various
input strings.
因为UTF-8编码英文字符最省字节，UTF-8编码一个字符会用1~4个bytes,UTF-16编码一个字符会用2或4个bytes。UTF-8适合编码纯英文字符串，
UTF-16适合编码中英文混合字符串

(b) Consider the following (incorrect) function, which is intended to decode a UTF-8 byte string into
a Unicode string. Why is this function incorrect? Provide an example of an input byte string
that yields incorrect results.
def decode_utf8_bytes_to_str_wrong(bytestring: bytes):
return "".join([bytes([b]).decode("utf-8") for b in bytestring])
>>> decode_utf8_bytes_to_str_wrong("hello".encode("utf-8"))
'hello'
给中文字符就不行了，因为UTF-8只有在简单的字母符号编码时才用一个字节，中文的话编码不止一个字节，就会解码失败

(c) Give a two byte sequence that does not decode to any Unicode character(s).
print(bytes([000,245]).decode("utf-8"))


byte-pair编码解决的是子词编码问题，我们可以对每个字符编码也可以对每个字词编码，字词编码介于两者之间，提供效率和精度的tradeoff