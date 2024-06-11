import os
import hashlib
from mnemonic import Mnemonic
from hdwallet.utils import is_mnemonic
from hdwallet import HDWallet
from hdwallet.symbols import BTC
from eth_keys import keys
from bitcoinutils.setup import setup
from bitcoinutils.script import Script
from bitcoinutils.keys import P2wshAddress, P2shAddress, PrivateKey, PublicKey

def generate_custom_english_mnemonic():
    custom_keywords = "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon"
  
    english_mnemonic = Mnemonic('english')
    english_wordlist = english_mnemonic.wordlist

    keyword =  custom_keywords.split()
    num_random_words = 24 - len(keyword)
  
    random_phrase = english_mnemonic.generate(strength=256)
    random_words = random_phrase.split(' ')[:num_random_words]
    custom_words = keyword + random_words
  
    custom_binarys = ''.join([bin(english_wordlist.index(word))[2:].zfill(11) for word in custom_words])
    custom_binary = custom_binarys[:-8]
    byte_sequence = bytes(int(custom_binary[i:i+8], 2) for i in range(0, len(custom_binary), 8))
  
    checksum = hashlib.sha256(byte_sequence).digest()
    checksum_binary = ''.join(format(byte, '08b') for byte in checksum)
    mnemonic_binary = ''.join(custom_binary) + checksum_binary[:8]

    mnemonic_segments = [mnemonic_binary[i:i+11] for i in range(0, len(mnemonic_binary), 11)]

    mnemonic_indices = [int(segment, 2) for segment in mnemonic_segments]

    english_words = [english_wordlist[index] for index in mnemonic_indices]
    english_mnemonic = ' '.join(english_words)

    if is_mnemonic(mnemonic=english_mnemonic):
        return english_mnemonic, mnemonic_indices
  
def generate_address():
    setup("mainnet")
    while True:
        en_phrase, indices = generate_custom_english_mnemonic()

        hdw_btc = HDWallet(symbol = BTC)
        hdw_btc.from_mnemonic(mnemonic = en_phrase)
        hdw_btc.from_index(44, hardened=True)
        hdw_btc.from_index(0, hardened=True)
        hdw_btc.from_index(0, hardened=True)
        hdw_btc.from_index(0)
        hdw_btc.from_index(0)

        wif = hdw_btc.wif()
        private_key = PrivateKey(secret_exponent=int(hdw_btc.private_key(), 16))
        public_Key = private_key.get_public_key()

        taproot_address = public_Key.get_taproot_address()
        legacy_address = public_Key.get_address()
        native_address = public_Key.get_segwit_address()
        segwit_key = (
            public_Key
            .get_segwit_address()
        )
        nested_address = P2shAddress.from_script(segwit_key.to_script_pub_key())

        private_key = keys.PrivateKey(bytes.fromhex(hdw_btc.private_key()))
        public_key = private_key.public_key
        eth_address = public_key.to_checksum_address().lower()
      
        print('-' * 100)
        print('en_phrase:', en_phrase)
        print('indices:', indices)
        print('hex:', private_key)
        print('wif:', wif)
        print('Taproot:', taproot_address.to_string())
        print('Legacy:', legacy_address.to_string())
        print('Native:', native_address.to_string())
        print('Nested:', nested_address.to_string())
        print('ETH:', eth_address)

if __name__ == '__main__':
    generate_address()
  
