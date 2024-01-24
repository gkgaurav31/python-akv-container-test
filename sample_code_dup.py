from azure.keyvault import KeyVaultClient, KeyVaultAuthentication
from azure.keyvault.certificates import CertificateClient
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
import os
from azure.common.credentials import ServicePrincipalCredentials
import sys
import requests
#from azure.identity import AzureCliCredential
#cred = AzureCliCredential()
#e#cred.get_token("https://kv-ccoe-infra-secure.vault.azure.net/.default")
'''exclude_credentials = {
"exclude_environment_credential": True,
"exclude_shared_token_cache_credential": True,
"exclude_visual_studio_code_credential": True,
"exclude_interactive_browser_credential": True,
"exclude_powershell_credential": True,
"exclude_managed_identity_credential": True
}'''

exclude_credentials = {
"exclude_managed_identity_credential": True
}
credential = DefaultAzureCredential(**exclude_credentials, managed_identity_client_id="something")

def get_secreats():
    print ("Get Secret call....")
    vault_client=SecretClient(vault_url="https://kv-ccoe-infra-secure.vault.azure.net/", credential=credential)
    print ("Secreat Client created succesfully")
    value=vault_client.get_secret("okta-client-secret")
    print ("Received secret = ")
    print(value.value)

get_secreats()
