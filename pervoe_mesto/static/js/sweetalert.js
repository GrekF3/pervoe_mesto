document.addEventListener('DOMContentLoaded', function () {
    // Получаем все формы на странице
    var forms = document.querySelectorAll('form');

    // Для каждой формы добавляем обработчик события отправки
    forms.forEach(function(form) {
      form.addEventListener('submit', function (event) {
        event.preventDefault();

        // Получение данных из формы
        var formData = new FormData(form);

        // AJAX-запрос
        fetch(form.action, {
          method: 'POST',
          body: formData,
          headers: {
            'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value
          }
        })
        .then(response => response.json())
        .then(data => {
          // Проверка ответа от сервера
          if (data.success) {
            // Ответ успешен, отображаем SweetAlert
            Swal.fire({
              title: 'Успех!',
              text: 'Форма успешно отправлена!',
              icon: 'success',
              confirmButtonText: 'Ок'
            }).then(function () {
              // Дополнительные действия при нажатии кнопки "Ок"
              // Например, перенаправление на другую страницу
              // window.location.href = '/home/';
            });
          } else {
            // Ответ неуспешен, отображаем SweetAlert с ошибкой
            Swal.fire({
              title: 'Ошибка!',
              text: data.message || 'Что-то пошло не так. Попробуйте еще раз.',
              icon: 'error',
              confirmButtonText: 'Ок'
            });
          }
        })
        .catch(error => {
          console.error('Error:', error);
          // Отображаем SweetAlert с ошибкой при неудачном запросе
          Swal.fire({
            title: 'Ошибка!',
            text: 'Что-то пошло не так. Попробуйте еще раз.',
            icon: 'error',
            confirmButtonText: 'Ок'
          });
        });
      });
    });
  });

  document.addEventListener('DOMContentLoaded', function() {
    var form = document.getElementById('get-price-form');
    var submitBtn = document.getElementById('submitBtn');

    submitBtn.addEventListener('click', function() {
        var selectedType = document.querySelector('.get-price__form-type.checked');
        if (selectedType) {
            var typeValue = selectedType.getAttribute('data-value');
            var typeField = document.createElement('input');
            typeField.type = 'hidden';
            typeField.name = 'type';
            typeField.value = typeValue;

            form.appendChild(typeField);

            // Отправка формы через AJAX (пример с использованием Fetch API)
            fetch(form.action, {
                method: form.method,
                body: new FormData(form),
            })
            .then(response => response.json())
            .then(data => {
                // Обработка успешного ответа от сервера
                Swal.fire({
                    title: 'Успех!',
                    text: 'Форма успешно отправлена!',
                    icon: 'success',
                    confirmButtonText: 'Ок'
                });
            })
            .catch(error => {
                // Обработка ошибки
                console.error('Ошибка при отправке формы:', error);
                Swal.fire({
                    title: 'Ошибка!',
                    text: 'Произошла ошибка при отправке формы',
                    icon: 'error',
                    confirmButtonText: 'Ок'
                });
            });
        } else {
            Swal.fire({
                title: 'Внимание!',
                text: 'Выберите тип',
                icon: 'warning',
                confirmButtonText: 'Ок'
            });
        }
    });

    var typeButtons = document.querySelectorAll('.get-price__form-type');
    typeButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            typeButtons.forEach(function(btn) {
                btn.classList.remove('checked');
            });
            button.classList.add('checked');
        });
    });
});


document.addEventListener("DOMContentLoaded", function() {
  var button = document.querySelector('.about-complex__btn');
  var second_button = document.querySelector('.catalog-tabs__btn');

  // Функция для прокрутки к элементу с идентификатором "quiz"
  function scrollToQuiz() {
    var quizSection = document.querySelector('#quiz');
    quizSection.scrollIntoView({ behavior: 'smooth' });
  }

  // Добавляем обработчик события click для первой кнопки
  button.addEventListener('click', scrollToQuiz);

  // Добавляем обработчик события click для второй кнопки
  second_button.addEventListener('click', scrollToQuiz);
});