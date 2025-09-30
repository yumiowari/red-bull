import cv2
import os

def process_video(path, width, height):
    video = cv2.VideoCapture(path)

    # cria a pasta de saída com o nome do vídeo (sem extensão)
    #file = os.path.basename(path)
    #out = os.path.splitext(file)[0]
    out = os.path.splitext(path)[0]
    os.makedirs(out, exist_ok=True)

    count, success = 0, True
    while success:
        # lê o frame
        success, image = video.read()
        if success:
            # redimensiona a imagem para a resolução desejada
            resized = cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)
        
            # salva o frame
            cv2.imwrite(f'{out}/frame{count}.jpg', image, [cv2.IMWRITE_JPEG_QUALITY, 70]) # <--- 70% de compressão JPEG
            count += 1

    video.release()

    print(f"Frames salvos em '{out}'")

if __name__ == '__main__':
    while(True):
        path = input("Digite o nome do arquivo (ou 'quit' para encerrar o programa):\n")

        if path == 'quit':
            break;
        else:
            process_video(f'./src/{path}', 360, 640) # proporção 9:16 (youtube shorts)