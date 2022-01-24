import os
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

import pyfiglet
ascii_banner = pyfiglet.figlet_format("          Azure Py          \n Create    Secrets")
print(ascii_banner)

print("This CLI script was created by Tish Hutchinson ....... \n\n")

#set keyvault variable
keyVaultVar = "KEY_VAULT_NAME"
#ask for key vault name
keyVaultName = input("Please enter the name of the key vault that you wish to create secrets for: \n> ")
#run script on the command line
os.system(f"export {keyVaultVar}={keyVaultName}")
#print envrionment variable
print(f"\n \n'{keyVaultVar}={keyVaultName}' environment variable has been set.\n\n")
#set keyvault URI
KVUri = f"https://{keyVaultName}.vault.azure.net"
#get credentials from already signed in user
credential = DefaultAzureCredential()
#store user credentials & keyvault URI
secret_client = SecretClient(vault_url=KVUri, credential=credential)

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
