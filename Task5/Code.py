text = input("Enter a string: ")
encoded = ""
i = 0
while i < len(text):
    count = 1
    while i + 1 < len(text) and text[i] == text[i + 1]:
        count += 1
        i += 1
    encoded += text[i] + str(count)
    i += 1
print("Original String:", text)
print("Original Length:", len(text))
print("Encoded String:", encoded)
print("Encoded Length:", len(encoded))
if len(encoded) < len(text):
    print("Compression is beneficial.")
else:
    print("Compression is not beneficial.")
    print("Final String:", text)

