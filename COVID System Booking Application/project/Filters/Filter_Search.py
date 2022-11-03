
from Filters.FilterInterface import Filter

class FilterSearchByAttribute(Filter):
    def __init__(self, attribute, string, searchLayers) -> None:
        self.attribute = attribute
        self.searchStr = string
        self.searchLayers : list = searchLayers
        self.searchLayers.append(attribute)

    def filter(self, json):
        matches = []
        if not isinstance(json, list): json = [json]
        for value in json:
            topLayer = value
            for layer in self.searchLayers:
                if self.searchLayers[-1] == layer: continue
                value = value[layer]
            if value[self.attribute].startswith(self.searchStr):
                matches.append(topLayer)
        return matches

