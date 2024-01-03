from ultralytics import YOLO
import torch
def main():
    # Inicializar el modelo YOLO pre-entrenado
    model = YOLO('yolov8n')  # Puedes especificar 'yolov5s', 'yolov5m', 'yolov5l', o 'yolov5x'

    print(torch.cuda.is_available())
    # Cargar datos y comenzar el entrenamiento
    # pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
    results = model.train(data='data.yaml', epochs=200, imgsz=800, device='0')
if __name__ == "__main__":
    main()