import oci
from oci.config import from_file
import base64

config = from_file(file_location="C:\\Users\\..\\..\\..\\config", profile_name='DEFAULT')
SecretsClient = oci.secrets.SecretsClient(config)
print("I am in Secrets")
secret_base64 = SecretsClient.get_secret_bundle("<ocid1...>").data.secret_bundle_content
secret = secret_base64.__getattribute__("content")
print(base64.b64decode(secret))


