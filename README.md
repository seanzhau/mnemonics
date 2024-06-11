# Breadcrumbsgenerate_mnemonic_by_custom_words

This program allowed you use custom words to create mnemonics, Custom keywords must be in [Bip39](https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt).

## mnemonics

![Principle of mnemonic words](./mnemonicone.png)

## Notice

- Only support 24 keywords.
- Max custom keywords: 23 custom words (Not recommended).
- Safe to use, Save your mnemonics offline.

## Example
```bash
% python3.11 generate_mnemonic.py
----------------------------------------------------------------------------------------------------
en_phrase: abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon organ
indices: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1251]
hex: 0x8d85ffefd65591492e6fbd3ccd396a07ff5927158c225bee504b73a55f23ece4
wif: L1xpANm9pHz58F4SJYKCJx5YYBHANBF9s4Yk8HGgGExuNKEUifJG
Taproot: bc1pdwu7cwtx4kked9vgks52dkjqn0735n6r5qg8xgxphu03awht2s9sjx6dff
Legacy: 1BuU1sNx5a6bMcbJ3uet44g1wJH5PeTXWD
Native: bc1qw7whq4jwgxhu3s47yk2chyn65an5mr2utwx6w5
Nested: 37MwH5Uo8NBwW2mZXzbuJK7JGaxrt64M1o
ETH: 0x5648a8543558dd45312880cfada13a4892347444
% python3.11 generate_mnemonic.py
----------------------------------------------------------------------------------------------------
en_phrase: abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon surface
indices: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1745]
hex: 0xb86542ac1a5cb7b0f5855db33e7101c1062595a28d52b5644bf941eaa3edb5e1
wif: L3Q9kgPHnSFGWGxaotb9t5DRtHpd6wKS9Ptx64VFiy9UKxXdhQpN
Taproot: bc1ptrehjc87g0vaaka6h8hdm6v2kfpk7mzcwy2zkdw9adedq560rwxqfl0nf5
Legacy: 18sL2uZkJY1PXsFkmPuJFdDMg7L6CQeY8j
Native: bc1q2exezqr59na6jvfhx84qwh0p2uv6ktct84n02x
Nested: 3PALmm8YJKdH3ZGSVJLwVxAuXJd3d6Lesu
ETH: 0xa76b603098ec1f2088f4c225debfcf6c10c60f0b
% python3.11 generate_mnemonic.py
----------------------------------------------------------------------------------------------------
en_phrase: abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon trouble
indices: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1864]
hex: 0x9e8bb5176569dac2980d2f238ae90277df78754b5188c54ef6d78a248749f330
wif: L2XuLAkNNk25w3nS8LbhpxEE6Ee1b6sBzjJkUoK4ACCumJrzPpa1
Taproot: bc1p539q2qwwx2tyyl39ssgzsd3tuqx9grxuyn3xpl9l4xhtkq9d6quqfgjw8h
Legacy: 1BtQcgGiCzB5uLg8eLbxkNQQZV4aBPaoft
Native: bc1qwa4z7nc3cmnyzhh37eay5hesjn37mnenrmjxyp
Nested: 3Mh2N94oNokwKqdLR45igMM18o4NiosHhZ
ETH: 0x9d07e66e6d8fcb289de292038aadaede50411184
% python3.11 generate_mnemonic.py
----------------------------------------------------------------------------------------------------
en_phrase: abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon trouble
indices: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1864]
hex: 0x9e8bb5176569dac2980d2f238ae90277df78754b5188c54ef6d78a248749f330
wif: L2XuLAkNNk25w3nS8LbhpxEE6Ee1b6sBzjJkUoK4ACCumJrzPpa1
Taproot: bc1p539q2qwwx2tyyl39ssgzsd3tuqx9grxuyn3xpl9l4xhtkq9d6quqfgjw8h
Legacy: 1BtQcgGiCzB5uLg8eLbxkNQQZV4aBPaoft
Native: bc1qwa4z7nc3cmnyzhh37eay5hesjn37mnenrmjxyp
Nested: 3Mh2N94oNokwKqdLR45igMM18o4NiosHhZ
ETH: 0x9d07e66e6d8fcb289de292038aadaede50411184
% python3.11 generate_mnemonic.py
----------------------------------------------------------------------------------------------------
en_phrase: abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon organ
indices: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1251]
hex: 0x8d85ffefd65591492e6fbd3ccd396a07ff5927158c225bee504b73a55f23ece4
wif: L1xpANm9pHz58F4SJYKCJx5YYBHANBF9s4Yk8HGgGExuNKEUifJG
Taproot: bc1pdwu7cwtx4kked9vgks52dkjqn0735n6r5qg8xgxphu03awht2s9sjx6dff
Legacy: 1BuU1sNx5a6bMcbJ3uet44g1wJH5PeTXWD
Native: bc1qw7whq4jwgxhu3s47yk2chyn65an5mr2utwx6w5
Nested: 37MwH5Uo8NBwW2mZXzbuJK7JGaxrt64M1o
ETH: 0x5648a8543558dd45312880cfada13a4892347444
% python3.11 generate_mnemonic.py
----------------------------------------------------------------------------------------------------
en_phrase: abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon art
indices: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 102]
hex: 0xcb4793fa23e98437e2d37655eaaa59cf03a0637ea890f85a85d91946e9214c64
wif: L42rpqMcjt1LtyvZCSTLkaif5mjFyTXTHSVuckRZEM7GaD2KLCkc
Taproot: bc1pchg9zwycj7gv6cmcv42ewztvwyddqzx4erfjf3t3ecae8j6m6leqa559z0
Legacy: 1KBdbBJRVYffWHWWZ1moECfdVBSEnDpLHi
Native: bc1qca600p6lwp84dzvrwxmyyjmwda3j34l6dk2t4z
Nested: 3EeAWLnFaWxTupS1ePVbCgwmYkR6yZTCr8
ETH: 0x1cde9225ffe472d7426a0e18a3407635f9fa8fdb
```

## Donations:

- BTC: 1SeanZhmmKe48Je6MSeTzZgdzTDVu4F9j
- ETH: 0x7ec531fe3ef3343763427bec35d56fec083bd38a
