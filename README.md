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

The project is supported and made consistent by using GitHub Codespaces with devcontainer.json configuration files. This method pulls in the mcr.microsoft.com/devcontainers/python:1-3.11-bullseye container, adds the needed packages (streamlit and requirements from requirements.txt) and opens the app with streamlit run streamlit_app.py. You can start using a browser to check your Streamlit app right away because port forwarding is set up for 8501. Having the project in a containerized environment guarantees it can be shared, duplicated and executed instantly, lowering the effort required for setup and helping everyone collaborate better. Both automation and its design structure make Crypto Gadget practical for cryptography as well as a structured way to study applied cryptography.

## Sample Runs and Outputs
Include screen snippets (screenshots) or text-based output examples for each algorithm's functionality (encryption, decryption, hashing for both text and files where applicable).

Embed images directly in the README.md or link to them within the repository. Use Markdown code blocks for text output.

Example:

Python Code:
```Python
print("hello")
```

```
This is just text in a code block
```

More can be found here: ![Markdown Guide: Basic Syntax](https://www.markdownguide.org/basic-syntax/)
