import cv2
import os

def process_video(path):
    video = cv2.VideoCapture(path)

    # Cria pasta de saída com o nome do vídeo (sem extensão)
    out = os.path.splitext(path)[0]
    os.makedirs(out, exist_ok=True)

    count, success = 0, True
    while success:
        success, image = video.read() # Lê o frame
        if success: 
            cv2.imwrite(f'{out}/frame{count}.jpg', image) # Salva o frame
            count += 1

    video.release()

    print(f"Frames salvos em '{out}'")

if __name__ == '__main__':
    while(True):
        path = input("Digite o nome do arquivo (ou 'quit' para encerrar o programa):\n")

        if path == 'quit':
            break;
        else:
            process_video(f'./src/{path}')