# anyseed
Generating seed from any mnemonic phrase

## Using
```html
  from anyseed import get_seed
  words = "online shift magic dog obtain clog bus hello farm island style onion suffer ensure bean"
  password = ""
  seed = get_seed(words, password)
  print(seed.hex())
  # f03c00c137fb4b4f5682806701f4ff705d302f07c4b3b5506ff75666d3b7258eca86494a37be9e347c58accdc9e8522edcc4215da938a1dddb5e67f8c8e24270
```
Works with electrum and bip39 mnemonics. 
:exclamation: Does not determine the validity of the phrase, will generate a seed from any words