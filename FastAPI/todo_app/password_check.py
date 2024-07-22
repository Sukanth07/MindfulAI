from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def hash_password(password):
    return pwd_context.hash(password)

def verify_pwd(password, hashed_pwd):
    return pwd_context.verify(password, hashed_pwd)

password = input("Enter Password: ")
hashed_pwd =  hash_password(password)

print("\n\nPassword: ", password)
print("Hashed Password: ", hashed_pwd)

new_password = "sukanth@123"

print("Verification Status: ", verify_pwd(password, hashed_pwd))
print("New Verification Status: ", verify_pwd(new_password, hashed_pwd))