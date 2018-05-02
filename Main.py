import Scanner
import Image
import time
import matplotlib.pyplot as plt

if __name__ == '__main__':  # Esto en el futuro va a estar en un Main.py
    tic = time.time()
    s = Scanner()
    s.frame_scan()
    s.__delete__()
    toc = time.time()
    # s.x_line_scan()
    # s.y_line_scan()
    # print("Se movio con amplitud {} V".format(s.amplitude))
    print("Duracion total en segundos:", toc - tic)
    image = plt.imshow(I)
    plt.imshow(I, interpolation='nearest')
    grid(True)
    img = Image.fromarray(I, 'RGB')
    img.save('my.png')
    img.show()
# Esperar unos segundos a que cierre el device para volver a correr
# Por ahora el frame time mas chico que alcanza es 0.3 seg (aprox 18 us por pixel)

