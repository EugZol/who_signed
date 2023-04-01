import argparse
import bitcoinlib
import hashlib
import sys
import requests
import urllib.parse

MAINNET_BASE_URL = "https://blockstream.info/api/"
TESTNET_BASE_URL = "https://blockstream.info/testnet/api/"

def sha256(byte_string):
  return hashlib.sha256(byte_string).digest()

def request(url):
  print(f'\033[2mGetting {url}\033[0m', file=sys.stderr)
  result = requests.get(url)
  text = result.text
  if result.status_code != 200:
    print(f'\033[2mReturned status {result.status_code} - {text}\033[0m', file=sys.stderr)
    exit(1)
  return result

parser = argparse.ArgumentParser(
  description="Show who signed multisig transaction",
  formatter_class=argparse.ArgumentDefaultsHelpFormatter
)
parser.add_argument("-t", "--testnet", action="store_true", help="use testnet")
parser.add_argument("txid", help="transaction ID (a.k.a. transaction hash)")
args = parser.parse_args()

base_url = TESTNET_BASE_URL if args.testnet else MAINNET_BASE_URL

txid = urllib.parse.quote(args.txid)
tx_hex = request(f"{base_url}/tx/{txid}/hex").text
tx_json = request(f"{base_url}/tx/{txid}").json()

tx = bitcoinlib.transactions.Transaction.parse(bytes.fromhex(tx_hex))

for i, [tx_input, json_input] in enumerate(zip(tx.inputs, tx_json['vin'])):
  tx_input.value = json_input['prevout']['value']
  if 'witness' in json_input and len(json_input['witness']) > 0:
    tx_hash = sha256(sha256(tx.signature_segwit(i, tx_input.hash_type)))
    witness_msg = ' (witness)'
  else:
    tx_hash = tx.signature_hash(i, tx_input.hash_type)
    witness_msg = ''
  print(f"Input #{i} from {json_input['prevout']['scriptpubkey_address']} ({json_input['prevout']['value']} satoshis){witness_msg}")
  print(f'Public keys:')
  for j, public_key in enumerate(tx_input.keys):
    match_msg = ''
    for s, signature in enumerate(tx_input.signatures):
      if signature.verify(tx_hash, public_key):
        match_msg = f' -> signature #{s+1}'
    print(f'  {j+1}. {public_key}{match_msg}')
