import re
txt = """The rain in Spain The rain in Spain
        The rain in Spain The rain in Spain
        The rain in Spain The rain in Spain"""
x = re.findall("ai", txt)
print("counting word:\n",txt)
print(x.count("ai"),"ai Found")
