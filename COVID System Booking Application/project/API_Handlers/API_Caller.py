import requests
from abc import ABC, abstractmethod
from typing import List
import datetime

class APICaller(ABC):
    @classmethod
    def __init__(self, url, attributes) -> None:
        self.urlBase = f'https://fit3077.com/api/v1/{url}'
        self.apiKey = ""
        with open("API_KEY.txt") as f:
            self.apiKey = f.readline()
        self.attributes = attributes
        self.status = None


    @classmethod 
    def get(self,urlEnd = ""):
        response = requests.get(url=f"{self.urlBase}{urlEnd}", headers={'Authorization': self.apiKey})
        self.status = response.status_code
        return response.json()

    @classmethod
    def post(self, jsonData, urlEnd = "") :
        response = requests.post(url=f"{self.urlBase}{urlEnd}", headers={'Authorization': self.apiKey}, json= jsonData)
        if self.status == 400: print(response.message)
        self.status = response.status_code
        return response

    @classmethod
    def delete(self, id):
        response = requests.delete(url=f"{self.urlBase}/{id}", headers={'Authorization': self.apiKey})
        self.status = response.status_code

    @classmethod
    def patch(self, json, id):
        response = requests.patch(url=f"{self.urlBase}/{id}", headers={'Authorization': self.apiKey}, json=json)
        self.status = response.status_code
        return response

    @classmethod
    def getByID(self, id):
        return self.get(f"/{id}")

    @abstractmethod
    def select(self, filter = None):
        pass

    @classmethod
    def add(self, ignore = None, urlEnd = ""):
        if ignore is None:
            ignore = []
        if isinstance(ignore, str): ignore = [ignore]
        ignore.insert(0, "updatedAt") 
        ignore.insert(0,"createdAt")
        self.post(self.__inputValues(self.attributes, ignore), urlEnd)
    
    @classmethod
    def update(self, attributes : list, id):
        if isinstance(attributes, str): attributes = [attributes]
        updateVals = {}
        for attribute in attributes:
            if attribute in self.attributes:
                updateVals[attribute] = self.attributes[attribute] 
        self.patch(self.__inputValues(updateVals),id)

    @classmethod
    def __inputValues(self, attributes : dict, ignore = []):
        newJsonValue = {}
        for attribute, attributeType in attributes.items():
            if attribute in ignore: continue
            if isinstance(attributeType, str): newJsonValue[attribute] = input(f"{attribute}: ")
            elif isinstance(attributeType, bool): newJsonValue[attribute] = eval(input(f"{attribute}: "))
            elif isinstance(attributeType, int): newJsonValue[attribute] = int(input(f"{attribute}: "))
            elif isinstance(attributeType, dict): 
                print(attribute)
                if len(ignore) > 0:
                    if isinstance(ignore[-1], list): 
                        ignore = ignore[-1]
                    else: ignore = []
                    newJsonValue[attribute]  = self.__inputValues(attributeType, ignore[-1])
                else:
                    newJsonValue[attribute]  = self.__inputValues(attributeType, ignore)
        return newJsonValue

    @classmethod
    def storeChanges(self, id, change):
        currentObject = self.getByID(id)
        currentChanges : dict = currentObject["additionalInfo"]
        if "changes" not in currentChanges:
            currentChanges.update({'changes' : []})
        currentChanges = currentChanges['changes']
        if len(currentChanges) >= 3:
            currentChanges = currentChanges[1:]
        change.append(str(datetime.datetime.now()))
        currentChanges.append(change)
        currentObject["additionalInfo"]['changes'] = currentChanges
        self.patch(currentObject, id)
        pass
            
    @classmethod
    def reverseChange(self, id, change):
        patchFile = {}
        for individualChange in change[:-1]:
            path = individualChange[0]
            value = individualChange[1]
            patchFile.update({path : value})
            self.patch(patchFile, id)
            pass