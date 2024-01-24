from flask import Flask
import os
from azure.keyvault.secrets import SecretClient
from azure.identity import ClientSecretCredential

app = Flask(__name__)

@app.route('/')
def get_secret_from_keyvault():
    try:
        keyVaultName = os.environ.get("AZURE_KEYVAULT_NAME")
        KVUri = f"https://{keyVaultName}.vault.azure.net"

        tenant_id = os.environ.get("AZURE_TENANT_ID")
        client_id = os.environ.get("AZURE_CLIENT_ID")
        client_secret = os.environ.get("AZURE_CLIENT_SECRET")

        credential = ClientSecretCredential(tenant_id, client_id, client_secret)
        client = SecretClient(vault_url=KVUri, credential=credential)

        secretName = os.environ.get("SECRET_NAME", "TEST")

        retrieved_secret = client.get_secret(secretName)

        return f"Secret from Key Vault: {retrieved_secret.value}"

    except Exception as e:
        return f"Error retrieving secret: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
