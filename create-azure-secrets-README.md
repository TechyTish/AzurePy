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

# Latest releases

| Version No. |                                                            Details                                                      |
| :---------: | :--------------------------------------------------------------------------------------------------------------------:  |
|     1.0     | users can create multiple secrets with error handling for invalid inputs                                                |
|     1.1     | environment variable stored via user input - no longer need to run ```export KEY_VAULT_NAME=mykeyvaultname``` command prior to running script.|
|     1.2     | ...                                                                                                                     |
|     1.3     | ...                                                                                                                     |
|     1.4     | ...                                                                                                                     |
|     1.5     | ...                                                                                                                     |
|     1.6     | ...                                                                                                                     |

# API references
- azure.identity
- azure.keyvault.secrets

# Build and Test
- Download the ``` "create-azure-secrets.py" ``` file from this repo.
- Open your command line of choice
- Navigate to the folder where the ``` "create-azure-secrets.py" ``` file is located on your device.
- Enter ``` pyhton3 create-azure-secrets.py ``` in the command line and the script will start.
- Press CTRL + C at anytime to exit the script

# Contribute
- [Github](https://github.com/TechyTish/AzurePy)


# Screenshot of App
<img width="918" alt="Screenshot 2022-01-23 at 11 02 42" src="https://user-images.githubusercontent.com/27959256/150686559-1fdf88d9-4e05-4c45-b264-9278c78d1fe4.png">
