document.addEventListener("DOMContentLoaded", function () {
  document.querySelector(".tablinks").click();
});

// Функция открытия вкладки==========================================================================
function openTab(evt, tabName) {
  closeSubTabs(); // Закрываем все субвкладки перед открытием новой вкладки
  var i, tabcontent, tablinks;

  // Скрываем все табы
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Удаляем класс 'active' со всех кнопок табов
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }

  // Отображаем текущий таб и добавляем класс 'active' к текущей кнопке
  document.getElementById(tabName).style.display = "block";
  evt.currentTarget.className += " active";

  // Автоматически открываем субвкладку "Price"
  openSubTab(null, tabName + "Price");
}

// Функция открытия субвкладки=========================================================================
function openSubTab(event, subTabName) {
  var i, subtablinks, subtabcontent;

  // Скрываем все субтабы
  subtabcontent = document.getElementsByClassName("subtabcontent");
  for (i = 0; i < subtabcontent.length; i++) {
    subtabcontent[i].style.display = "none";
  }

  // Удаляем класс 'active' со всех субвкладок
  subtablinks = document.getElementsByClassName("subtablinks");
  for (i = 0; i < subtablinks.length; i++) {
    subtablinks[i].className = subtablinks[i].className.replace(" active", "");
  }

  // Отображаем текущую субвкладку и добавляем класс 'active' к текущей кнопке
  document.getElementById(subTabName).style.display = "block";
  if (event) {
    event.currentTarget.className += " active";
  }

  // Отображение содержимого output только для активной субвкладки
  document.querySelector(".output").style.display = "block";
}

// Функция обработки полей комплектов===================================================================
function addDictionaryElement(subTabId) {
  var container = document.getElementById("dictionary-container-" + subTabId);

  var newDiv = document.createElement("div");
  newDiv.className = "dictionary";

  newDiv.innerHTML = `
    <label for="count_per_one">Единиц в одном товаре:</label>
    <input type="text" name="count_per_one" oninput="checkFormFields('${subTabId}')">
    <label for="box_wage_cost">Стоимость труда на упаковку:</label>
    <input type="text" name="box_wage_cost" oninput="checkFormFields('${subTabId}')">
    <label for="box_cost">Стоимость упаковки:</label>
    <input type="text" name="box_cost" oninput="checkFormFields('${subTabId}')">
    <label for="box_size">Размер упаковки:</label>
    <input type="text" name="box_size" oninput="checkFormFields('${subTabId}')">
    <button type="button" onclick="removeDictionaryElement(this, '${subTabId}')">Удалить</button>
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

// Привязка функции очистки к кнопке "Clear"
document.addEventListener("DOMContentLoaded", function () {
  document.getElementById("clearButton").addEventListener("click", clearOutput);
});
