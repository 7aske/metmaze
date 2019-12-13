
# velicina ekrana u pikselima
WINDOW_SIZE = (1024, 768)
# velicina sprite-a u gridu u fajlu
SPR_SIZE = (16, 16)
# velicina sprite-a koju zelimo da prikazemo na ekranu
BLOCK_SIZE = (32, 32)
# lokacija fajla u odnosu na lokaciju gde nam je
# main.py
SPRITE_IMAGE = "assets/sprites.png"
# visina i sirina level-a u blokivima
LEVEL_W = WINDOW_SIZE[0] // BLOCK_SIZE[0]
LEVEL_H = WINDOW_SIZE[1] // BLOCK_SIZE[1]