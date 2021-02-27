import oci
from oci.config import from_file
import base64
config = from_file(file_location="C:\\Users...config", profile_name='DEFAULT')
# Manages encryption/decryption of the data key.


def encryptdatakey(masterkeyocid):
    # This function is called only when the Data Key needs to be encrypted by the Master Key.
    # This function is rarely used only during master key rotation
    datakeyocid = "<OCID of the data key>"
    datakey = datakeyocid   # Convert into Base64/Bytes if required.
    masterkey = masterkeyocid
    key_management_client = oci.key_management.KmsCryptoClient(config, "https://your_crypto_head.oraclecloud.com")
    encrypt_data_details = oci.key_management.models.EncryptDataDetails(
        key_id=masterkey,
        plaintext=datakey)
    encrypt_response = key_management_client.encrypt(encrypt_data_details)
    return encrypt_response


def decryptdatakey(masterkey, artifact):
    # This function is called only the Data Key is needs.
    # Note:- Only the Data Key OCID is returned, the actual Data Key is safe in the Vault.
    key_management_client = oci.key_management.KmsCryptoClient(config, "https://your_crypto_head.oraclecloud.com")
    decrypt_data_details = oci.key_management.models.DecryptDataDetails(
            key_id=masterkey,
            ciphertext=artifact)
    decrypt_response = key_management_client.encrypt(decrypt_data_details)
    return decrypt_response

