oyuncular = {"fb":{"kaleci":"Ahmet",
                   "defans":["Ali","Can","Recep"],
                   "forvet":{"sag_on":"Muhammed","ileri":"Eren","sol_on":"Recep Can"}
                   },
             "gs": {"kaleci": "Muslera",
                    "defans": ["Ahmet","Mete","Kerim"],
                    "forvet": {"sag_on": "Burak", "ileri": "Sabri", "sol_on": "Neymar"}
                    },
             }

print(oyuncular["fb"]["kaleci"])
print(oyuncular["fb"]["forvet"])
print(oyuncular["fb"]["forvet"]["ileri"])
print("oyuncu değişikliği")
oyuncular["fb"]["forvet"]["ileri"]= input("Yeni oyuncu ekle")
print(oyuncular["fb"]["forvet"]["ileri"])
print(oyuncular["fb"])
print(oyuncular["gs"])

print("bjk" in oyuncular)
