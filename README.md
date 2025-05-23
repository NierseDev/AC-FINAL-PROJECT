# CryptoGadget | Applied Cryptography | April 26, 2025

**Group Members:**
1. ***Hamzah Ibarreta Cuadra***
2. ***Harold Salvador***
3. ***Jude Fajardo***

## Introduction
Crypto Gadget is an online cryptographic tool designed as our final project for the Applied Cryptography course. The application serves to provide an environment where people can check out and apply basic cryptographic actions. The goal of the project is to close the divide between understanding and using cryptography by presenting a simple and practical platform.

Cryptography helps keep today’s digital life safe by securing all kinds of communications online. When you understand cryptographic processes, you realize the value of keeping your data private, unchanged and authenticated. With Crypto Gadget, users can watch how their data is changed by different cryptographic approaches. By means of demonstrations and simulations, the tool teaches us how cryptography helps people and organizations trust each other online.


## Project Objectives
The specific objectives of this project are the following:

1. To produce an interactive platform to show the main cryptographic operations of hashing, symmetric encryption/decryption and asymmetric encryption/decryption.
2. To give users the chance to learn personally about different ways cryptographic algorithms protect digital data.
3. To connect our learning with practice by seeing and comparing the results of using various cryptographic techniques on input information handled by users.

## Discussions
The Crypto Gadget tool has been developed using Streamlit and demonstrates everyday uses of key cryptography methods. Thanks to the clear and straightforward strategy, people can move between symmetric encryption/decryption, generating keys and hashing functions by using the sidebar menu. The initial view of the application is Home.py which greets users, provides information on project credits and instructions for using the app and allows users to quickly check out the available cryptographic modes. Thanks to Streamlit, you can experiment with cryptographic ideas right away and in an interactive way.

There’s a specific educational purpose for each cryptographic algorithm we apply. The hashing section uses MD5, SHA-1 and SHA-256 algorithms for the purpose of checking data integrity. In symmetric encryption, Fernet, AES (CBC mode) and ChaCha20 methods are covered, allowing you to see how passwords are used to generate a secret key and how random salt/IV are added. The module’s asymmetric part provides the ability to make key pairs using RSA, DSA and ECDSA. Knowing these algorithms is important because public-key cryptography is key to digital signatures and strong information security on the internet. The applications are made possible by Python’s cryptography and hashlib libraries and the results are shown in real time for easy understanding.

## Sample Runs and Outputs
## Asymmetric Encryption/Decryption:

Generate Keys

Private Key:
```
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEArRTD0fSjOoyK/SPgPXS/3ERoecliJyb929z80TbgaXqEakJE
NVH0HD3sPS7eSUrfMXcJW9047O9zhsZLFcTgAfrhnvnyQ0drgN2dSLm/p9DdVoU9
oAN18F9XV4Xx4Ckeh6sgk0hjRvyrrgcK74f+gwoKEeSF43xojp2nlCnRxqEXWfvH
aSOSSOZpTDLqv4iCc3G0q5441G91SCJtYh7Mr+aLJmeizKCNdrpApw+9fww5/hUm
4BHlolY7reugdoFvEPsyVXYcbNOBDUEzerZFK8C2sR+efC4Uo5QhYEt39lUG8dOh
lH9y2YDL2o5CVX8xbb1iWqobLX1gT+aEwcqqQQIDAQABAoIBAAPLwgPIxEVjoVih
LAXPbOkVqn8ErmJUFqrDyo5dMES78kUnoCbIhF/HF2QcBkKQMbvJEK0n0xVpZuZN
X8aLbD7Hq+5WxljycZ5qFEA5shHjnaqyiCOwsIpCd9aXo+w1KdvGAk3cn1aTMmg1
QRVrbTOeRlK2lhDWlzvzSijQlhUi0fHxe63UzrrPKdhPTGtacgucKusS/sVP9xgl
FRT0DF28wcQHsIZyIFvmBiP/Xv+hSTEi3L7+L3gVSeP3qmskeAW+JR88WueoreG8
5TUudLRHbLuQevstijbzLzZh9pIbXIFADX3DkTV3/slre+k4X7N7RQ1/4Xa/RBfc
bq9JIbkCgYEA8h13XiVtSu29Q15IZ9swO/RsZ0xvC9JZsManYIWkOyIch3cnKDlD
s1FWZffUrNMoxRX5h0jKVfheR+o9vRlQuq6UWsihoXCSf0s8lCjakVyurCqT5LTo
5/TppXKBeJgil9Hjwc6utozC5Pu20JpIu6wIB596EaKtCtYGkzUtJZkCgYEAtwHM
dywWm1lhgEDF+wDwAaEmAcC21CX9YiJ0eAS2bWsNx5xhXHbrIQCL/1Xd+Q75HX70
zadCWXCdv9Op1GtUcsjvjjjFcNgS8NNbRwWm6dzy6iAGLj3+YdPHjb27FJBTDXYW
OPCZmjd72o0zp44S5HD7PhsP4JugW4t1XTVSQukCgYEA1s2Nudk6vd9uqvZbBslQ
YeDYzEzjuHlHWa7lkJ0At/XrmcP82ZL0nYLsREs8RJiS80grufq6iMtx2hvX6o0r
MnTw6hpWTASz9Huro0cboxu3XMfprl9Sw3hmUoLkmzled5OfnbLhDtSTlNQ9vZUk
MlzOQvUaN8s7+wEnlDL5ewECgYEAjzwLKiMJtqEoXNdVnXVIZB4avzh0YGszfIF3
IxCdL9qgOGE/Gr3Anl3tNPWh/HMpq1pYhDWrCpHIBgHGZIl02TpHtMreTcnwWSkz
wcy8rUHPpktWSw8ecLbu8xNSv2+OcXTBQ+OcdUWD3LSzfysFwmJjYmKP9L4Zrkzi
mQdI0TECgYBT7ynKIxhItnT6/eMDJ6efyps3f5Tg+Z7JkKcjmuaIS2NGt6r9m1hv
OPgSxnR0DFznjIEFRH/Z/JtVA5nJdy3A+xjwKd/140K5++ePFGf5D6+ufCjL7Zh5
g6rh7Fse5UcHmoQUs1JRLnHNDK4gshAkKQgl4WeUojEtFxZMngJM/w==
-----END RSA PRIVATE KEY-----
```
Public Key:
```
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEArRTD0fSjOoyK/SPgPXS/
3ERoecliJyb929z80TbgaXqEakJENVH0HD3sPS7eSUrfMXcJW9047O9zhsZLFcTg
AfrhnvnyQ0drgN2dSLm/p9DdVoU9oAN18F9XV4Xx4Ckeh6sgk0hjRvyrrgcK74f+
gwoKEeSF43xojp2nlCnRxqEXWfvHaSOSSOZpTDLqv4iCc3G0q5441G91SCJtYh7M
r+aLJmeizKCNdrpApw+9fww5/hUm4BHlolY7reugdoFvEPsyVXYcbNOBDUEzerZF
K8C2sR+efC4Uo5QhYEt39lUG8dOhlH9y2YDL2o5CVX8xbb1iWqobLX1gT+aEwcqq
QQIDAQAB
-----END PUBLIC KEY-----
```
## Symmetric Encrpytion/Decryption:
Fernet (Encrypt)
Text:
```
CSPC
```
Encrypted Token:
```
gAAAAABoME45otmLHEs5WhvfCVkKpO_jm9uoZ4lLRFeawBuUoNfAhtFx_1FMBgTEGlCkmwoMCVYKc4ul12fZ3h8U3joeRlUHEQ==
```

Fernet (Decrypt)
Text:
```
gAAAAABoME3DomFr3O-rVEVn1VyU0BpkF7zCXEqPvusCaDQXW91sKsFNUW5KuhDdsp8YnKIJKqe2l5s5GKoUlPSydwSa5QYmiQ==
```
Decrypted Message:
```
CSPC
```