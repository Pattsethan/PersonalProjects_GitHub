from googletrans import Translator
import json
# Open our JSON file and load it into python
class bcolors:
    Blue = '\033[94m'
    Green = '\033[92m'
    White = '\033[0m'
    Yellow = '\033[93m'
    Bold = '\033[1m'
    Underline = '\033[4m'

        
with open ('twitter_data.json', 'r') as json_file:
    translator = Translator()
    data = json.load(json_file)
    for p in data["tweets"]:
        print (bcolors.Underline + p.get("user").get("screen_name"), "from,", p.get("user").get("location"), "says:", bcolors.White + p["text"],"\n")
        try:
            x = translator.translate(p["text"])
            t = (str(x)[33:].split(", pronunciation="))
            print (bcolors.White + "English Translaion:", (t[0]), "\n")
        except:
            continue
        
        #data = json.loads(line['text'])
        #for p in data ["text"]:
        #    try:
        #        print(p)
        #   except:
        #        continue
        