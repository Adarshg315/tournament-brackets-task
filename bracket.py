from flask import Flask

app = Flask(__name__)


@app.route('/')
def BracketGen():
    teamSize = range(120)
    bracketSize = 25
    topTeams = 5
    outputBracket = []
    avg = len(teamSize) / float(len(teamSize) / bracketSize)

    last = 0.0

    while last < len(teamSize):
        outputBracket.append(list(teamSize[int(last):int(last + avg)]))
        last += avg

    if len(outputBracket[0]) == topTeams:
        print(str(outputBracket))
    else:
        b = []
        for x in outputBracket:
            b.append(x[-topTeams:])
        return str(b)


app.run(host='0.0.0.0', port=3000)
