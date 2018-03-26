import csv
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

with open('sampleInput.csv', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        name = row[0]
        company = row[1]
        date = row[2]
        splitName = name.split(',')
        fullName = splitName[1] + " " + splitName[0]
        print(fullName.upper())

        nameFont = ImageFont.truetype("arial.ttf", 46)
        detFont = ImageFont.truetype("arial.ttf", 30)
        sampleCert = "sampleCertificate.jpg"
        img = Image.open(sampleCert)

        draw = ImageDraw.Draw(img)
        draw.text((224, 234), fullName.upper(), (40, 40, 40), font=nameFont)
        draw.text((555, 328), company, (40, 40, 40), font=detFont)
        draw.text((476, 380), date, (40, 40, 40), font=detFont)
        draw = ImageDraw.Draw(img)

        path = "generated/"
        img.save(path + fullName.upper() + ".png")

