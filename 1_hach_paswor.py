import hashlib

password = "password"
hashed_password = hashlib.md5(password.encode()).hexdigest()
print("MD5:", hashed_password)
