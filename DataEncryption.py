import oci
from oci.config import from_file
import base64
import DataKeyManagement
config = from_file(file_location="C:\\Users\\...config", profile_name='DEFAULT')
# Manages encryption of actual data.


def encryptdata(masterkeyocid, artifact, plain_text):
    # This function is called when actual Data needs to be encrypted.
    # Note:- Artifact is the Encrypted Data Key passed to the function just for this example.
    # The Artifact should stored securely and only this code should have access to it.
    masterkey = masterkeyocid
    key_management_client = oci.key_management.KmsCryptoClient(config, "https://your_crypto_head.oraclecloud.com")
    encrypt_data_details = oci.key_management.models.EncryptDataDetails(
        key_id=DataKeyManagement.decryptdatakey(masterkey, artifact),
        plaintext=plain_text)
    encrypt_response = key_management_client.encrypt(encrypt_data_details)
    return encrypt_response


def decryptdata(masterkey, artifact, cipher_text):
    # This function is called when actual Data needs to be decrypted.
    # The Data Key OCID is passed inline calling methods from DataKeyManagement.py file.
    key_management_client = oci.key_management.KmsCryptoClient(config, "https://your_crypto_head.oraclecloud.com")
    decrypt_data_details = oci.key_management.models.DecryptDataDetails(
            key_id=DataKeyManagement.decryptdatakey(masterkey, artifact),
            ciphertext=artifact)
    decrypt_response = key_management_client.encrypt(decrypt_data_details)
    return decrypt_response

