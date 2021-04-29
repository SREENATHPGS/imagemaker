from PIL import Image, ImageDraw, ImageFilter, ImageFont
import os, sys, argparse, json

def generateImageFromText(text, save_dir_path = "./generatedImages"):

    if not os.path.isdir(save_dir_path):
        os.mkdir(save_dir_path)

    font_roboto_40 = ImageFont.truetype('./fonts/Roboto/Roboto-Bold.ttf',40)
    font_roboto_30 = ImageFont.truetype('./fonts/Roboto/Roboto-Bold.ttf',30)
    font_roboto_regular_40 = ImageFont.truetype('./fonts/Roboto/Roboto-Regular.ttf',40)
    
    img = Image.new('RGB', (1024,1024), color="white")
    img_width, img_height = img.size
    
    logo_image = Image.open('./jatalks_logo.jpg')
    logo_image_width, logo_image_height = logo_image.size
    
    img.paste(logo_image, (128, 348))#int(img_height/2 - logo_image_height/2)))
    
    d = ImageDraw.Draw(img)
    d.text((302,387 - 20), "Ja Talks", font = font_roboto_40, fill=(0,0,0))
    d.text((302,440 - 15), "@ja.talks", font = font_roboto_30, fill=(0,0,0))

    words = text.split(" ")
    lines = []
    line = []
    no_of_chars_in_line = 0
    for index, word in enumerate(words):
        no_of_chars_in_line = no_of_chars_in_line + len(word) + 1

        if no_of_chars_in_line >= 45:
            lines.append(" ".join(line))
            line = []
            no_of_chars_in_line = 0
            
        if index == (len(words) - 1):
            line.append(word)
            lines.append(" ".join(line))
            line = []
            no_of_chars_in_line = 0


        line.append(word)

    print(lines)

    
    textY = 530

    for line in lines:
        d.text((128, textY), line, font = font_roboto_regular_40, fill=(0,0,0))
        textY = textY + 55
    #d.text((128,585), "answer.", font = font_roboto_regular_40, fill=(0,0,0))

    img.save(f"{save_dir_path}/{text}.jpg")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--quotes_file", default="quotes_file.json", help="Quotes file in json format.")
    args = parser.parse_args()
    quotes = None

    quotes_file = args.quotes_file

    if not os.path.isfile(quotes_file):
        print("No such input file exists.")
        sys.exit()

    with open(quotes_file, "r") as fp:
        try:
            quotes = json.loads(fp.read()).get("quotes", [])
        except Exception as e:
            print(e)
            print("ERROR, possibly file format is invalid JSON.")

    if not quotes:
        print("No quotes given.")
    
    for quote in quotes:
        generateImageFromText(quote)
            



