document.addEventListener("DOMContentLoaded", function () {
  // Инициализация первой вкладки
  document.querySelector(".tablinks").click();
  // Привязка функции очистки к кнопке "Clear"
  document.getElementById("clearButton").addEventListener("click", clearOutput);
});

function openTab(evt, tabName) {
  closeSubTabs(); // Закрываем все субвкладки перед открытием новой вкладки
  var tabcontent = document.getElementsByClassName("tabcontent");
  var tablinks = document.getElementsByClassName("tablinks");

  // Скрываем все табы
  for (var i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Удаляем класс 'active' со всех кнопок табов
  for (var i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }

  // Отображаем текущий таб и добавляем класс 'active' к текущей кнопке
  document.getElementById(tabName).style.display = "block";
  evt.currentTarget.className += " active";

  // Автоматически открываем первую субвкладку, если есть
  var firstSubTab = document.querySelector(`#${tabName} .subtablinks`);
  if (firstSubTab) {
    firstSubTab.click();
  }
}

function openSubTab(evt, subTabName) {
  var subtabcontent = document.getElementsByClassName("subtabcontent");
  var subtablinks = document.getElementsByClassName("subtablinks");

  // Скрываем все субтабы
  for (var i = 0; i < subtabcontent.length; i++) {
    subtabcontent[i].style.display = "none";
  }

  // Удаляем класс 'active' со всех субвкладок
  for (var i = 0; i < subtablinks.length; i++) {
    subtablinks[i].className = subtablinks[i].className.replace(" active", "");
  }

  // Отображаем текущую субвкладку и добавляем класс 'active' к текущей кнопке
  document.getElementById(subTabName).style.display = "block";
  if (evt) {
    evt.currentTarget.className += " active";
  }

  // Отображение содержимого output только для активной субвкладки
  document.querySelector(".output").style.display = "block";
}

function addDictionaryElement(subTabId) {
  var container = document.getElementById("dictionary-container-" + subTabId);

  var newDiv = document.createElement("div");
  newDiv.className = "dictionary";

  newDiv.innerHTML = `
    <label for="count">Единиц:</label>
    <input id="count" type="text" name="count" oninput="checkFormFields('${subTabId}')">
    <label for="wage">Стоимость труда:</label>
    <input id="wage" type="text" name="wage" value="8" oninput="checkFormFields('${subTabId}')">
    <label for="cost_box">Стоимость упаковки:</label>
    <input id="cost_box" type="text" name="cost_box" value="8" oninput="checkFormFields('${subTabId}')">
    <label for="box_size">Размеры упаковки:</label>
    <input id="box_size" type="text" name="box_size" value="11*10*10" oninput="checkFormFields('${subTabId}')">
    <button type="button" onclick="removeDictionaryElement(this, '${subTabId}')">&#128465;</button>
  `;

  container.appendChild(newDiv);
  checkFormFields(subTabId); // Проверка полей после добавления нового элемента
}

function removeDictionaryElement(button, subTabId) {
  // Удаляем родительский элемент (div.dictionary) кнопки "Удалить"
  var dictionaryDiv = button.parentElement;
  dictionaryDiv.remove();
  checkFormFields(subTabId); // Проверка полей после удаления элемента
}

function checkFormFields(subTabId) {
  var form = document.querySelector(`#${subTabId} form`);
  var inputs = form.getElementsByTagName("input");
  var submitButton = form.querySelector("input[type='submit']");

  var allFilled = true;
  for (var i = 0; i < inputs.length; i++) {
    if (inputs[i].type === "text" && inputs[i].value.trim() === "") {
      allFilled = false;
      break;
    }
  }

  submitButton.disabled = !allFilled;
}

function closeSubTabs() {
  var subtabcontent = document.getElementsByClassName("subtabcontent");
  for (var i = 0; i < subtabcontent.length; i++) {
    subtabcontent[i].style.display = "none";
  }
}

// Функция очистки содержимого .output
function clearOutput() {
  var output = document.querySelector(".output .result");
  output.innerHTML = "";
}
