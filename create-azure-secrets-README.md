# Introduction 
This python script will enable you to create multiple secrets at once via the command line.

# Prerequisites
- [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli)
- [Python 3.6+](https://www.python.org/downloads/)

# Installation
- Open your command line of choice
- Sign into Azure using the ``` az login ``` command.
- Install the identity package using the ``` pip3 install azure-identity ``` command.
- Install the secrets package using the ``` pip3 install azure-keyvault-secrets ``` command.
- Define your enrionment variable that supplies the name of the Keyvault using the ``` export KEY_VAULT_NAME=mykeyvaultname ``` command.

# Latest releases
- v1.0: Sunday 23rd January 2022

# API references
- azure.identity
- azure.keyvault.secrets

# Build and Test
- Open your command line of choice
- Navigate to the folder where the "create-azure-secrets.py" file is located
- Enter pyhton3 create-azure-secrets.py in ther command line and the script will Started
- Press CTRL + C at anytime to exit the script

# Contribute
- [Github](https://github.com/TechyTish/AzurePy)