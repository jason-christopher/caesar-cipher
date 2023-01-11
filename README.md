# LAB - Class 18

## Project: Caesar Cipher

### Author: Jason Christopher

### Description

This app will encrypt a message that can then be decrypted when supplied with the corresponding key. It can also crack and decrypt an encrypted Caesar Cipher message, even when key a key is not given. 

* `encrypt` function - takes in a plain text phrase and a numeric shift value and shifts the phrase that many letters. Shifts that push a letter out or range should wrap around. Upper and lower case letter keep their case during encryption. 
* `decrypt` function - takes in encrypted text and numeric shift which will restore the encrypted text back to its original form when correct key is supplied. 
* `crack` function - decodes the cipher so that an encrypted message can be transformed into its original state WITHOUT access to the key. If the app has a match rate of greater than 90%, it will return it's proposed answer.

### Links and Resources

* NLTK Library: Words & Names

### Setup

Install required packages:

* `pip install nltk`

To run:

* From the `caesar-cipher` directory run `python caesar_cipher/cipher.py`.
* The first prompt will ask you for the URL of the Wikipedia page you'd like to scrape. Either:
  * Paste the desired URL (including `https://` header)
  * Hit the Return key to scrape the default Wikipedia page.

### Tests

Tests were provided and more tests were added.

* Check for simple words for encrypt & decrypt.
* Check shift inputs greater than 26.
* Check upper and lower cases during encryption/decryption.
* Check that characters that are not letters are maintained.
* Check that encrypt messages matches decrypt for the same shift value.
* Check the app can crack a valid string using English words.
* Check the app cannot crack a string using random letters (no false positive).
* Check the app can crack a string that uses names.

To run tests, from the `caesar-cipher` directory run `pytest tests/test_caesar.py`.

