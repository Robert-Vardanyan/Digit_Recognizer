import pygame
from datetime import datetime
import cv2
import pickle
import numpy as np

# Установка размеров окна и области рисования
WIDTH, HEIGHT = 700, 400
DRAWING_AREA_SIZE = 280

# Параметры кисти
brush_size = 15

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (169, 169, 169)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Переменные для отслеживания состояния
last_saved_image_path = None

# Отслеживает состояние (Очистка/Перезапуск)
is_restarted = False  

# Параметры кнопок
BUTTON_WIDTH = 150
BUTTON_HEIGHT = 50
BUTTON_COLOR = (0, 128, 0)
BUTTON_TEXT_COLOR = (255, 255, 255)
BUTTON_TEXT_HOVER_COLOR = (255, 255, 0)
BUTTON_HOVER_COLOR = (34, 139, 34)
PREDICTION_BUTTON_POS = (WIDTH - BUTTON_WIDTH - 100, HEIGHT - BUTTON_HEIGHT - 120)
CLEAR_BUTTON_POS = (WIDTH - BUTTON_WIDTH - 100, HEIGHT - BUTTON_HEIGHT - 60)

# Инициализация Pygame
pygame.init()

icon = pygame.image.load('neural-network.png')
pygame.display.set_icon(icon)

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Digit Recognizer by ROVA")

# Создание поверхности для рисования
drawing_surface = pygame.Surface((DRAWING_AREA_SIZE, DRAWING_AREA_SIZE))
drawing_surface.fill(BLACK)

# Переменная для ответа
answer = None

def clear_drawing():
    """
    Очищает поверхность для рисования и сбрасывает путь к последнему сохраненному изображению.
    """
    global last_saved_image_path, is_restarted
    drawing_surface.fill(BLACK)
    last_saved_image_path = None
    is_restarted = False

def draw_button_prediction(mouse_pos, mouse_down):
    """
    Рисует кнопку "Prediction" на экране и изменяет ее внешний вид в зависимости от состояния мыши.
    """
    if PREDICTION_BUTTON_POS[0] <= mouse_pos[0] <= PREDICTION_BUTTON_POS[0] + BUTTON_WIDTH and \
       PREDICTION_BUTTON_POS[1] <= mouse_pos[1] <= PREDICTION_BUTTON_POS[1] + BUTTON_HEIGHT:
        pygame.draw.rect(screen, BUTTON_HOVER_COLOR, (*PREDICTION_BUTTON_POS, BUTTON_WIDTH, BUTTON_HEIGHT))
        text_color = BUTTON_TEXT_HOVER_COLOR if mouse_down else BUTTON_TEXT_COLOR
    else:
        pygame.draw.rect(screen, BUTTON_COLOR, (*PREDICTION_BUTTON_POS, BUTTON_WIDTH, BUTTON_HEIGHT))
        text_color = BUTTON_TEXT_COLOR

    font = pygame.font.Font(None, 36)
    text = font.render("Prediction", True, text_color)
    text_rect = text.get_rect(center=(PREDICTION_BUTTON_POS[0] + BUTTON_WIDTH // 2, 
                                      PREDICTION_BUTTON_POS[1] + BUTTON_HEIGHT // 2))
    screen.blit(text, text_rect)

def draw_button_clear_or_restart(mouse_pos, mouse_down):
    """
    Рисует кнопку "Clear" или "Restart" в зависимости от состояния программы.
    """
    button_text = "Restart" if last_saved_image_path else "Clear"
    if CLEAR_BUTTON_POS[0] <= mouse_pos[0] <= CLEAR_BUTTON_POS[0] + BUTTON_WIDTH and \
       CLEAR_BUTTON_POS[1] <= mouse_pos[1] <= CLEAR_BUTTON_POS[1] + BUTTON_HEIGHT:
        pygame.draw.rect(screen, BUTTON_HOVER_COLOR, (*CLEAR_BUTTON_POS, BUTTON_WIDTH, BUTTON_HEIGHT))
        text_color = BUTTON_TEXT_HOVER_COLOR if mouse_down else BUTTON_TEXT_COLOR
    else:
        pygame.draw.rect(screen, BUTTON_COLOR, (*CLEAR_BUTTON_POS, BUTTON_WIDTH, BUTTON_HEIGHT))
        text_color = BUTTON_TEXT_COLOR

    font = pygame.font.Font(None, 36)
    text = font.render(button_text, True, text_color)
    text_rect = text.get_rect(center=(CLEAR_BUTTON_POS[0] + BUTTON_WIDTH // 2, 
                                      CLEAR_BUTTON_POS[1] + BUTTON_HEIGHT // 2))
    screen.blit(text, text_rect)

def draw_answer():
    """
    Рисует ответ на экране в зависимости от результата предсказания.
    """
    font = pygame.font.Font(None, 70)
    answer_text = font.render('-', True, WHITE) if answer is None else font.render(str(answer), True, GREEN)
    screen.blit(font.render("Answer", True, WHITE), (PREDICTION_BUTTON_POS[0] - 15, 60))
    screen.blit(answer_text, (PREDICTION_BUTTON_POS[0] + BUTTON_WIDTH // 2 - 10, PREDICTION_BUTTON_POS[1] - 100))

def predicting(image_tensor):
    """
    Делает предсказание на основе входного изображения.
    """
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
    predict = model.predict(image_tensor)
    print(predict)
    number = np.argmax(predict)
    print(number)
    return number

# Основной цикл программы
running = True
drawing = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if PREDICTION_BUTTON_POS[0] <= mouse_x <= PREDICTION_BUTTON_POS[0] + BUTTON_WIDTH and \
               PREDICTION_BUTTON_POS[1] <= mouse_y <= PREDICTION_BUTTON_POS[1] + BUTTON_HEIGHT:
                is_restarted = True
                timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S_%f')
                file_path = f"./Draws/drawing_{timestamp}.png"
                pygame.image.save(drawing_surface, file_path)

                # Преобразование и сохранение изображения
                image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
                image_resized = cv2.resize(image, (28, 28), interpolation=cv2.INTER_AREA)
                image_blurred = cv2.GaussianBlur(image_resized, (3, 3), 0)
                image_blurred = image_blurred / 255.0
                cv2.imwrite(file_path, (image_blurred * 255).astype(np.uint8))

                last_saved_image_path = file_path
                image_tensor = image_blurred.reshape(1, 28, 28)
                answer = predicting(image_tensor)

            elif CLEAR_BUTTON_POS[0] <= mouse_x <= CLEAR_BUTTON_POS[0] + BUTTON_WIDTH and \
                 CLEAR_BUTTON_POS[1] <= mouse_y <= CLEAR_BUTTON_POS[1] + BUTTON_HEIGHT:
                clear_drawing()
            else:
                drawing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False

    # Получение позиции мыши
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Заливка фона серым цветом
    screen.fill(GRAY)

    # Рисование черного поля для рисования
    drawing_area_rect = pygame.Rect(60, 60, DRAWING_AREA_SIZE, DRAWING_AREA_SIZE)
    pygame.draw.rect(screen, BLACK, drawing_area_rect)

    # Рисование на черном поле
    if drawing and drawing_area_rect.collidepoint(mouse_x, mouse_y):
        pygame.draw.circle(drawing_surface, WHITE, (mouse_x - 60, mouse_y - 60), brush_size)

    # Отображение поверхности для рисования на экране
    screen.blit(drawing_surface, (60, 60))

    # Рисование кнопок и ответа
    draw_button_prediction((mouse_x, mouse_y), drawing)
    draw_button_clear_or_restart((mouse_x, mouse_y), drawing)
    draw_answer()

    # Отображение последнего сохраненного изображения
    if last_saved_image_path:
        large_image = pygame.image.load(last_saved_image_path)
        large_image = pygame.transform.scale(large_image, (DRAWING_AREA_SIZE, DRAWING_AREA_SIZE))
        screen.blit(large_image, (60, 60))

    # Обновление экрана
    pygame.display.flip()

pygame.quit()
