import cv2
from pyzbar.pyzbar import decode

# Inicializar la cámara
cap = cv2.VideoCapture(0)  # 0 para la cámara predeterminada, puedes ajustar el índice según tu configuración

while True:
    # Capturar un fotograma desde la cámara
    ret, frame = cap.read()

    # Decodificar los códigos de barras en el fotograma
    barcodes = decode(frame)

    # Dibujar un rectángulo alrededor de los códigos de barras y mostrar el valor decodificado
    for barcode in barcodes:
        (x, y, w, h) = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        barcode_data = barcode.data.decode("utf-8")
        cv2.putText(frame, barcode_data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        print("Código de barras: " + barcode_data)

    # Mostrar el fotograma con los códigos de barras
    cv2.imshow("Lector de Código de Barras", frame)

    # Salir si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar la ventana
cap.release()
cv2.destroyAllWindows()
