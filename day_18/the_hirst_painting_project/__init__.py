import colorgram

colors = colorgram.extract('hirst_painting.jpg', 240)
colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]

print(colors)