# Digit_Recognizer


## Описание

Digit Recognizer — это приложение, написанное с использованием библиотеки Pygame, для распознавания нарисованных вручную цифр. Пользователи могут рисовать цифры в специальной области, а затем получить предсказание от предварительно обученной модели нейронной сети.


## Графики
Графики, которые показывают результаты обучения модели:
### График точности обучения и валидации
На графике изображены две линии:

   - Training Accuracy (Точность обучения): Линия, отображающая точность модели на обучающем наборе данных на протяжении эпох. Эта линия показывает, как хорошо модель обучалась на тренировочных данных.

   - Validation Accuracy (Точность валидации): Линия, показывающая точность модели на валидационном наборе данных по мере тренировки. Эта линия помогает понять, как хорошо модель обобщает на невиданных данных.

<table>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/772f90da-fdac-403e-b7f6-36a353305cec" alt="График 1" width="400"/></td>
    <td><img src="https://github.com/user-attachments/assets/34f61063-030c-4ce7-867d-c88424adffd0" alt="График 2" width="400"/></td>
  </tr>
</table>

## Как запустить проект

1. Клонируйте репозиторий:
   ```bash
   git clon https://github.com/Robert-Vardanyan/Digit_Recognizer.git

2. Перейдите в каталог проекта:
   ```bash
   cd Digit_Recognizer

3. Создайте виртуальное окружение и активируйте его:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Linux/Mac
   venv\Scripts\activate  # Для Windows

4. Установите зависимости:
   ```bash
   pip install -r requirements.txt

5. Запустите файл main.py / main_CNN.py:
   ```bash
   python main_CNN.py


## Использование

1. Откройте приложение.
2. Нарисуйте цифру в черной области для рисования.
3. Нажмите кнопку "Prediction" для получения предсказания.
4. Нажмите кнопку "Clear" для очистки области рисования или "Restart" для перезапуска с сохранением текущего изображения.


## Файловая структура

- main.py / main_CNN.py: Основной файл приложения.
- model.pkl / model_CNN.pkl: Предварительно обученная модель нейронной сети.
- Draws/: Каталог для сохранения нарисованных изображений.
- neural-network.png: Иконка для приложения.


## Примечания

- Убедитесь, что файл модели (model.pkl / model_CNN.pkl) находится в той же директории, что и main.py.
- Все нарисованные и предсказанные изображения сохраняются в каталоге Draws.


## Пример работы

<p align="center">
  <img src="https://github.com/user-attachments/assets/0e9aa3f7-e6e1-405c-9eb8-b60cb0ef84d7" alt="Screenshot 2024-08-03_0" width="600"/>
  <br>
  <em>Фото 0</em>
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/814378ec-3d39-45c9-b1ef-6b8bdc7f0b60" alt="Screenshot 2024-08-03_1" width="600"/>
  <br>
  <em>Фото 1</em>
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/834efd5b-f5da-42a7-a7bf-55b2a08606e0" alt="Screenshot 2024-08-03_2" width="600"/>
  <br>
  <em>Фото 2</em>
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/6f75406c-1222-42e9-b19d-f255867ae36a" alt="Screenshot 2024-08-03_3" width="600"/>
  <br>
  <em>Фото 3</em>
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/9b0b7a08-d5fc-4c92-997c-c7ba1814b327" alt="Screenshot 2024-08-03_4" width="600"/>
  <br>
  <em>Фото 4</em>
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/11fd3c98-4b00-4b88-9db4-d303f5b2a259" alt="Screenshot 2024-08-03_5" width="600"/>
  <br>
  <em>Фото 5</em>
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/01d8c181-2c85-46e0-8aaa-f41b3dc01996" alt="Screenshot 2024-08-03_6" width="600"/>
  <br>
  <em>Фото 6</em>
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/7547a83b-6ff9-405a-95ec-c8a1c8bab5d5" alt="Screenshot 2024-08-03_7" width="600"/>
  <br>
  <em>Фото 7</em>
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/9fd6c6c2-7807-4d6e-a945-9edbeb33ce8a" alt="Screenshot 2024-08-03_8" width="600"/>
  <br>
  <em>Фото 8</em>
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/444df001-6c0d-41bf-870a-0c55e3ea03e6" alt="Screenshot 2024-08-03_9" width="600"/>
  <br>
  <em>Фото 9</em>
</p>
