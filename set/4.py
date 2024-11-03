a = "salom yoz. olam juda ham g'ozal. imtimxon bolyapdi."
soz = [".", ","]
b = ""
for c in a:
    if c not in soz:
        b += c

d = b.split()
s = a.split(". ")
s = [text.strip() for text in s if text]

print(d)
print(s)