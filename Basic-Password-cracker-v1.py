import hashlib

pass_filename = "Dumb-pass.txt" #Change to wordlist name, be sure to also put word list in same file
password = "004s" #Put a password that was in wordlist here

enc_password = password.encode("utf-8")
password_hash = hashlib.sha256(enc_password.strip()).hexdigest()
          #Change hash here ^
pass_file = open(pass_filename, "r")

for word in pass_file:
    enc_word = word.encode("utf-8")
    enc_hash = hashlib.sha256(enc_word.strip()).hexdigest()
       #Change hash here ^
    if password_hash == enc_hash:
        print("SUCCESS! The password was " + word)
        quit()

print("FAILED")