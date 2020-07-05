#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from pyIndego import IndegoClient

def country_operator(mcc, mnc):
    if mcc == 262:
        country =  "Germany"
        if mnc == 1:
            operator = "Telekom Deutschland"
        elif mnc == 2:
            operator = "Vodafone"
        elif mnc == 3:
            operator = "Telefónica"
        else:
            operator = None
    elif mcc == 232:
        if mnc == 1:
            operator = "A1 Telekom Austria"
        elif mnc == 2:
            operator = "Magenta Telekom"
        elif mnc == 5:
            operator = "Hutchison Drei Austria"
        else:
            operator = None
    else:
        country = None
        operator = None
    return (country, operator)


def main(config):
    with IndegoClient(**config) as indego:
        indego.update_network()
        
        (country, operator) = country_operator(indego.network.mcc, indego.network.mnc)
        if country is not None:
            print("Country is:", country)
            if operator is not None:
                print("Operator is:", operator)
            else:
                print("Operator is unknown")
        else:
            print("Country and operator are unknown")
        
        print("Signal strength (rssi):", indego.network.rssi)
        
        print("Available Networks:")
        for i in range(indego.network.networkCount):
            (country, operator) = country_operator(int(str(indego.network.networks[i])[:3]), int(str(indego.network.networks[i])[3:5]))
            if (country is not None) and (operator is not None):
                print("\t", country, ":", operator)
            else:
                print("\t", str(indego.network.networks[i])[:3], ":", str(indego.network.networks[i])[3:5])
        
if __name__ == "__main__":
    with open("config.json", "r") as config_file:
        config = json.load(config_file)
    main(config)
