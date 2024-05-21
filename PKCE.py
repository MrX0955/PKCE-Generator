import random,string,hashlib,base64

rand = random.SystemRandom()
code_verifier = ''.join(rand.choice(string.ascii_letters + string.digits)for _ in range(128))
code_sha_256 = hashlib.sha256(code_verifier.encode('utf-8')).digest()
b64 = base64.urlsafe_b64encode(code_sha_256)
code_challenge = b64.decode('utf-8').replace('=', '')

print(code_challenge, code_verifier)
