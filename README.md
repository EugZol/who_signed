# Who signed?

A script which shows who signed particular inputs of multisig witness transaction.

## Usage

```
python -m pip install pipenv
pipenv install

pipenv run python main.py <txid> # mainnet
pipenv run python main.py -t <txid> # testnet
```

or via Docker:

```
docker run --rm -it ghcr.io/eugzol/who_signed python main.py <txid>
```

*Example*:

```
% docker run --rm -it ghcr.io/eugzol/who_signed python main.py 63790adc5fd90dc307ca926f77b355984d7b0ff512df6d8a262a090558168783
Getting https://blockstream.info/api//tx/63790adc5fd90dc307ca926f77b355984d7b0ff512df6d8a262a090558168783/hex
Getting https://blockstream.info/api//tx/63790adc5fd90dc307ca926f77b355984d7b0ff512df6d8a262a090558168783
Input #0 from bc1qwqdg6squsna38e46795at95yu9atm8azzmyvckulcc7kytlcckxswvvzej (48714061 satoshis) (witness)
Public keys:
  1. 0375e00eb72e29da82b89367947f29ef34afb75e8654f6ea368e0acdfd92976b7c -> signature #1
  2. 03a1b26313f430c4b15bb1fdce663207659d8cac749a0e53d70eff01874496feff -> signature #2
  3. 03c96d495bfdd5ba4145e3e046fee45e84a8a48ad05bd8dbb395c011a32cf9f880
```
