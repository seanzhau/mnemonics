import os
import hashlib
import multiprocessing
from mnemonic import Mnemonic
from hdwallet.utils import is_mnemonic
from hdwallet import HDWallet
from hdwallet.symbols import BTC, ETH
from eth_hash.auto import keccak
from bitcoinutils.setup import setup
from bitcoinutils.script import Script
from bitcoinutils.keys import P2wshAddress, P2shAddress, PrivateKey, PublicKey

def generate_custom_mnemonic():
    custom_keywords = "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon"
  
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

    # if is_mnemonic(mnemonic=english_mnemonic):
    return english_mnemonic, mnemonic_indices

# 生成地址
def generate_taproot_address(mnemonic):
    hdw_btc = HDWallet(symbol = BTC)
    hdw_btc.from_mnemonic(mnemonic = mnemonic)
    hdw_btc.from_path(path="m/86'/0'/0'/0/0")
    private_key = PrivateKey(secret_exponent=int(hdw_btc.private_key(), 16))
    public_Key = private_key.get_public_key()
    taproot_address = public_Key.get_taproot_address()
    return taproot_address.to_string()

def generate_legacy_address(mnemonic):
    hdw_btc = HDWallet(symbol = BTC)
    hdw_btc.from_mnemonic(mnemonic = mnemonic)
    hdw_btc.from_path(path="m/44'/0'/0'/0/0")
    private_key = PrivateKey(secret_exponent=int(hdw_btc.private_key(), 16))
    public_Key = private_key.get_public_key()
    legacy_address = public_Key.get_address(compressed=True)
    return legacy_address.to_string()

def generate_nested_address(mnemonic):
    hdw_btc = HDWallet(symbol = BTC)
    hdw_btc.from_mnemonic(mnemonic = mnemonic)
    hdw_btc.from_path(path="m/49'/0'/0'/0/0")
    private_key = PrivateKey(secret_exponent=int(hdw_btc.private_key(), 16))
    public_Key = private_key.get_public_key()
    segwit_key = (
        public_Key
        .get_segwit_address()
    )
    nested_address = P2shAddress.from_script(segwit_key.to_script_pub_key())
    return nested_address.to_string()

def generate_native_address(mnemonic):
    hdw_btc = HDWallet(symbol = BTC)
    hdw_btc.from_mnemonic(mnemonic = mnemonic)
    hdw_btc.from_path(path="m/84'/0'/0'/0/0")
    private_key = PrivateKey(secret_exponent=int(hdw_btc.private_key(), 16))
    public_Key = private_key.get_public_key()
    native_address = public_Key.get_segwit_address()
    return native_address.to_string()

def generate_eth_address(mnemonic):
    hdw_eth = HDWallet(symbol = ETH)
    hdw_eth.from_mnemonic(mnemonic = mnemonic)
    hdw_eth.from_path(path="m/44'/60'/0'/0/0")
    private_key = PrivateKey(secret_exponent=int(hdw_eth.private_key(), 16))
    public_Key = private_key.get_public_key()
    uncompressed_pubkey = bytes.fromhex(public_Key.to_hex(compressed=True))
    keccak_hash = keccak(uncompressed_pubkey[1:])
    return '0x' + keccak_hash.hex()[-40:]
  
def generate_address():
    setup("mainnet")
    en_phrase, indices = generate_custom_mnemonic()

    taproot_address = generate_taproot_address(en_phrase)
    legacy_address = generate_legacy_address(en_phrase)
    native_address = generate_native_address(en_phrase)
    nested_address = generate_nested_address(en_phrase)
    eth_address = generate_eth_address(en_phrase)

    print('-' * 100)
    print('en_phrase:', en_phrase)
    print('indices:', indices)
    print('Taproot:', taproot_address.to_string())
    print('Legacy:', legacy_address.to_string())
    print('Native:', native_address.to_string())
    print('Nested:', nested_address.to_string())
    print('ETH:', eth_address)

if __name__ == '__main__':
    generate_address()


