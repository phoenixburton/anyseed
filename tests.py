from anyseed import get_seed

electrum_phrase = "unveil twin menu flight maple across canoe debris diagram expand chapter tooth"
electrum_phrase_seed = "3524ea97bf5cf49749ee511867b9b1af0a18c4a8b171e4dcd0f6104281fc5a94c9ec4c8b75bd1a8bfbf73c4b4553f0d5a35fbb225f667667b17621754e729718"
tmp_seed = get_seed(electrum_phrase)
print("====================================================\n")
print("Electrum phrase: {}\nSeed: {}\nType: {}\nTest: {}\n".format(electrum_phrase, tmp_seed["seed"].hex(), tmp_seed["type"], electrum_phrase_seed == tmp_seed["seed"].hex()))

bip39_phrase = "pelican orphan cherry mouse lucky never ketchup cross million cross blue bring parade shadow steak"
bip39_phrase_seed = "96d48cc015cecbf01b5d06da2ec59fd2849e768147a06e29053b45d800517f4374107d846175ac760535f176d1b7f771461c871c7bb3247f0c63c92727a98829"
tmp_seed = get_seed(bip39_phrase)
print("====================================================\n")
print("Bip39 phrase: {}\nSeed: {}\nType: {}\nTest: {}\n".format(bip39_phrase, tmp_seed["seed"].hex(), tmp_seed["type"], bip39_phrase_seed == tmp_seed["seed"].hex()))
print("====================================================\n")

unknown_phrase = "my random mnemonic phrase"
unknown_phrase_seed = "780def3da6558d1d31dbcff89788875f791757e2d998b124f40fccd634f8c444959258a64aff5c02db90fc1981de9241b2f27e00f32517d54418f34731a69cdc"
tmp_seed = get_seed(unknown_phrase)
print("====================================================\n")
print("Unknown phrase: {}\nSeed: {}\nType: {}\nTest: {}\n".format(unknown_phrase, tmp_seed["seed"].hex(), tmp_seed["type"], unknown_phrase_seed == tmp_seed["seed"].hex()))
print("====================================================\n")
