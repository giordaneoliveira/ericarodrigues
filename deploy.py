from flask import Flask
app = Flask(__name__)


@app.route("/")
def index():

    db = [
        {
            "grupo": "#01 Grupo V.I.P P. Pallazo",
            "link": "https://chat.whatsapp.com/K1CGgxShp3q8vAAd7eHRSv"
        },
        {
            "grupo": "#02 Grupo V.I.P P. Pallazo",
            "link": "https://chat.whatsapp.com/IsOJv2LuRz5Agtj1RPYPdh"
        },
        {
            "grupo": "#03 Grupo V.I.P P. Pallazo",
            "link": "https://chat.whatsapp.com/LUPoENajOxJ2mzKEZPEuoe"
        },
        {
            "grupo": "#04 Grupo V.I.P P. Pallazo",
            "link": "https://chat.whatsapp.com/HppaIC9yni15hA8wcgcO8L"
        },
        {
            "grupo": "#05 Grupo V.I.P P. Pallazo",
            "link": "https://chat.whatsapp.com/BgQgSRkWQZvLRtEY1NdTPe"
        },
        {
            "grupo": "#06 Grupo V.I.P P. Pallazo",
            "link": "https://chat.whatsapp.com/G2OguzUrFvQLRRHS4EPSv2"
        },
        {
            "grupo": "#07 Grupo V.I.P P. Pallazo",
            "link": "https://chat.whatsapp.com/IOwOLLJJ8bQ5LqWPC8a1fE"
        },
        {
            "grupo": "#08 Grupo V.I.P P. Pallazo",
            "link": "https://chat.whatsapp.com/KcSMKeyxE2v6tIHdhmbKxf"
        },
        {
            "grupo": "#09 Grupo V.I.P P. Pallazo",
            "link": "https://chat.whatsapp.com/Hsa6zidUZ5U0b3CHZlRN1E"
        },
        {
            "grupo": "#10 Grupo V.I.P P. Pallazo",
            "link": "https://chat.whatsapp.com/Idq96MSkYiP5AqdXEiqHza"
        }
    ]

    count = 0

    with open('count.txt') as f:
        count = int(f.readline())
        f.close()

    link = 'link'

    if count in range(0, 200):
        link = db[0]['link']
        nome = db[0]['grupo']
    if count in range(200, 400):
        link = db[1]['link']
        nome = db[1]['grupo']
    if count in range(400, 600):
        link = db[2]['link']
        nome = db[2]['grupo']
    if count in range(600, 800):
        link = db[3]['link']
        nome = db[3]['grupo']
    if count in range(800, 1000):
        link = db[4]['link']
        nome = db[4]['grupo']
    if count in range(1000, 1200):
        link = db[5]['link']
        nome = db[5]['grupo']
    if count in range(1200, 1400):
        link = db[6]['link']
        nome = db[6]['grupo']
    if count in range(1400, 1600):
        link = db[7]['link']
        nome = db[7]['grupo']
    if count in range(1600, 1800):
        link = db[8]['link']
        nome = db[8]['grupo']
    if count in range(1800, 2000):
        link = db[9]['link']
        nome = db[9]['grupo']

    count += 1

    with open('count.txt', 'w') as f:
        f.write(str(count))
        f.close()

    return """<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"><link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"
        crossorigin="anonymous"><title>Grupo vip P. Palazzo</title></head><body><div class="py-1"><div class="container"><div class="row"><div class="col-md-12"><img class="img-fluid d-block mx-auto" src="https://ericarodrigues.netlify.com/Logo-Fundo-Vazado-1-1024x738.png"></div></div></div></div><div class="pt-2"><div class="container"><div class="row"><div class="col-md-12"><p class="lead text-center">Clique no botão abaixo <br> para acessar o grupo</p><p class="text-center">⬇</p></div></div></div></div><div class="py-5"><div class="container"><div class="row"><div class="col-md-12"><a class="btn btn-block btn-success" href="{}">
                {}
                </a></div></div></div></div><script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
        crossorigin="anonymous"></script><script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
        crossorigin="anonymous"></script><script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
        crossorigin="anonymous"></script></body>""".format(link, nome)


@app.route("/acessos")
def acessos():
    acesso = 0
    with open('count.txt') as f:
        acesso = int(f.readline())
        f.close()
    return "Acessos {}".format(acesso)

# app.run(ssl_context='adhoc', port="80")