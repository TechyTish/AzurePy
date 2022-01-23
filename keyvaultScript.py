import os
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential
#from azure.keyvault.keys import KeyClient

#keyvault env name
keyVaultName = os.environ["KEY_VAULT_NAME"]
#keyvault URI
KVUri = f"https://{keyVaultName}.vault.azure.net"
#get credentials from already signed in user
credential = DefaultAzureCredential()
#store user credentials and keyvault URI
secret_client = SecretClient(vault_url=KVUri, credential=credential)

import pyfiglet
ascii_banner = pyfiglet.figlet_format("          Azure Py          \n Create    Secrets")
print(ascii_banner)

print("This CLI script was created by Tish Hutchinson ....... \n\n")

#check if inputs
while True:
    try:
        numberOfSecrets = int(input("How many secrets do you want to create?: \n> "))
    except ValueError:
        print("Invalid Response! - You must enter an integer! \n")
        continue
    answer = input("Are you sure you want to create {} number of secrets? (y/n) \n> ".format(numberOfSecrets))
    if  answer.lower() in ('yes', 'y'):
        break
    elif answer.lower() in ('no', 'n'):
       continue
    else:
        print("Invalid Response! - Please enter 'y', 'yes' or 'n', 'no' next time! \n")
        continue

print (f'You entered: {numberOfSecrets} \n \n')

#store secrets inputted in a dictionary
myDict = {}

#iterate through number of input
for i in range(numberOfSecrets):
    secretName = input(f"Please enter no. {i+1} secret name: \n> ")
    secretValue = input(f"Please enter no. {i+1} secret value: \n> ")

    #store secret names & values as 
    myDict[secretName] = secretValue

print(f"\n \nCreating the following secrets in the {keyVaultName} keyvault called; \n '{myDict}' \n ... \n ... \n ... \n")

#set keyvault secret names and values
for key, value in myDict.items():
    secret_client.set_secret(key, value)

print("Your secrets have been uploaded to Azure, thanks for using my script!")

#print(f"Retrieving your secret from {keyVaultName}.")

#retrieved_secret = secret_client.get_secret(myDict)

#print(f"Your secret is '{retrieved_secret.value}'.")