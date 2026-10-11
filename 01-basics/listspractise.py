languages =["java", "python", "javascript", "php", "C++"]
print(languages)

print(languages[0])
print(languages[-1])

languages.append("C#")
print(languages)
languages.remove("php")
print(languages)


count = 1

for language in languages:
    print(f"{count}.{language}")
    count += 1

#enumerate()
for count, language in enumerate(languages, start=1):
    print(f"{count}. {language}")

