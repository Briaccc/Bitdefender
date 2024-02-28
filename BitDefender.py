import base64
import requests
import json

apiKey = "XXX"
loginString = apiKey + ":"
encodedBytes = base64.b64encode(loginString.encode())
encodedUserPassSequence = str(encodedBytes, 'utf-8')
authorizationHeader = "Basic " + encodedUserPassSequence

apiEndpoint_Url = "https://cloud.gravityzone.bitdefender.com/api/v1.0/jsonrpc/network"

while True:
    print("Menu:")
    print("1. Détail des modules")
    print("2. Reconfigurer l'agent")
    print("0. Quitter")
    choix = input("Votre choix : ")

    if choix == "1":
        computer_name = input("Entrez l'ID du PC : ")

        request = {
            "params": {
                "endpointId" : computer_name,
            },
            "jsonrpc": "2.0",
            "method": "getManagedEndpointDetails",
            "id": "301f7b05-ec02-481b-9ed6-c07b97de2b7b"
        }

        result = requests.post(apiEndpoint_Url, json=request, verify=False,
                               headers={"Content-Type": "application/json", "Authorization": authorizationHeader})

        # Vérifiez que la requête a réussi avant d'écrire dans le fichier
        if result.status_code == 200:
            # Écrivez le résultat dans un fichier JSON
            with open('resultat.json', 'w') as f:
                json.dump(result.json(), f, indent=4)
        else:
            print("La requête a échoué. Statut de la réponse :", result.status_code)


    elif choix == "2":
            computer_name_agent = input("Entrez l'ID du PC : ")

            request = {
                "params": {
                    "targetIds": [
                        computer_name_agent
                    ],
                    "scheduler": {
                        "type": 1
                    },
                    "modules": {
                        "advancedThreatControl": 1,
                        "firewall": 1,
                        "contentControl": 1,
                        "deviceControl": 1,
                        "powerUser": 1,
                        "encryption": 1,
                        "advancedAntiExploit": 1,
                        "patchManagement": 1,
                        "networkAttackDefense": 1,
                    },
                    "scanMode": {
                        "type": 1
                    },
                    "roles": {
                        "relay": 0,
                        "exchange": 0
                    },
                    "productType": 0
                },
                "jsonrpc": "2.0",
                "method": "createReconfigureClientTask",
                "id": "787b5e36-89a8-4353-88b9-6b7a32e9c87f"
            }

            result = requests.post(apiEndpoint_Url, json=request, verify=False,
                                headers={"Content-Type": "application/json", "Authorization": authorizationHeader})

            # Vérifiez que la requête a réussi avant d'écrire dans le fichier
            if result.status_code == 200:
                # Écrivez le résultat dans un fichier JSON
                with open('reconfiguration_result.json', 'w') as f:
                    json.dump(result.json(), f, indent=4)
            else:
                print("La requête a échoué. Statut de la réponse :", result.status_code)



    elif choix == "0":
        break


    else:
        print("Choix invalide. Veuillez choisir à nouveau.") 
