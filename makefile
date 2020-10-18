help:
	@echo to encode the plaintext: make run ARGS='encode plaintext key'
	@echo to decode the ciphertext: make run ARGS='decode plaintext key'

run:
	python Vigenere.py $(ARGS)
