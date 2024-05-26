// Функция открытия главной вкладки
function openTab(evt, tabName) {
  closeSubTabs(); // Закрываем все субвкладки перед открытием новой вкладки
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(tabName).style.display = "block";
  evt.currentTarget.className += "active";

  // Автоматически открываем субвкладку "Price"
  openSubTab(evt, tabName + "Price");
}

// Функция открытия субвкладки
function openSubTab(event, subTabName) {
  closeSubTabs();
  var i, subtablinks, subtabcontent;
  subtabcontent = document.getElementsByClassName("subtabcontent");
  for (i = 0; i < subtabcontent.length; i++) {
    subtabcontent[i].style.display = "none";
  }
  subtablinks = document.getElementsByClassName("subtablinks");
  for (i = 0; i < subtablinks.length; i++) {
    subtablinks[i].className = subtablinks[i].className.replace(" active", "");
  }
  document.getElementById(subTabName).style.display = "block";
  if (event) {
    event.currentTarget.className += " active";
  }

  // Отображение содержимого output только для активной субвкладки
  document.querySelector(".output").style.display = "block";
}

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

// Установить отображение первой вкладки и субвкладки "Price" при загрузке страницы
document.addEventListener("DOMContentLoaded", function () {
  document.querySelector(".tablinks").click();
});
