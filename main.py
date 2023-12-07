import json

from json2ofx import json2ofx

inputfile = 'input.json'
outputfile = 'output.ofx'
with open(inputfile, 'r') as f:
    input = json.load(f)

oxf_string = json2ofx(input)

with open(outputfile, 'w') as f:
    f.write(oxf_string)

print("converted '{0}' to '{1}'".format(inputfile, outputfile))
