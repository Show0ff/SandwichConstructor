let allIngredients = {};


$(document).ready(function () {
    loadIngredients(function () {
        loadSandwiches();
    });
    $('#sandwichModal').on('shown.bs.modal', function () {
        console.log("Modal is shown!");
        populateIngredientsDropdown();
    });
    $('#sandwichForm').on('submit', function (event) {
        event.preventDefault();
        createSandwich();
    });
    $('#ingredientForm').on('submit', function (event) {
        event.preventDefault(); // Останавливаем стандартное поведение формы
        createIngredient();
    });
});

function loadSandwiches() {
    $.get('http://127.0.0.1:8000/api/sandwich/all/', function (data) {
        $('#sandwiches').empty();

        data.forEach(sandwich => {
            let ingredients = sandwich.ingredients.map(ingId => allIngredients[ingId]).join(', ');

            let sandwichCard = `
                <div class="col-md-4">
                    <div class="card mb-4">
                        <div class="card-body">
                            <h5 class="card-title">${sandwich.name}</h5>
                            <p class="card-text">${sandwich.description}</p>
                            <p><strong>Ингредиенты:</strong> ${ingredients}</p>
                            <button onclick="deleteSandwich(${sandwich.id})" class="btn btn-danger">Удалить</button>
                        </div>
                    </div>
                </div>
            `;
            console.log(allIngredients);

            $('#sandwiches').append(sandwichCard);
        });
    });
}


function loadIngredients(callback) {
    $.get('http://127.0.0.1:8000/api/ingredient/all', function (data) {
        $('#ingredients').empty();
        console.log(data);
        data.forEach(ingredient => {
            allIngredients[ingredient.id] = ingredient.name;

            let ingredientCard = `
                <div class="col-md-3">
                    <div class="card mb-4">
                        <div class="card-body">
                            <h5 class="card-title">${ingredient.name}</h5>
                            <p><strong>Вес:</strong> ${ingredient.weight}</p>
                            <p><strong>Ккал:</strong> ${ingredient.kcal}</p>
                            <button onclick="deleteIngredient(${ingredient.id})" class="btn btn-danger">Удалить</button>
                        </div>
                    </div>
                </div>
            `;

            $('#ingredients').append(ingredientCard);
        });

        if (callback) {
            callback();
        }
    });
}


function deleteSandwich(id) {
    $.ajax({
        url: `http://127.0.0.1:8000/api/sandwich/delete/${id}/`,
        type: 'DELETE',
        success: function () {
            loadSandwiches();
        }
    });
}

function deleteIngredient(id) {
    $.ajax({
        url: `http://127.0.0.1:8000/api/ingredient/delete/${id}/`,
        type: 'DELETE',
        success: function () {
            loadIngredients();
        }
    });
}

function populateIngredientsDropdown() {
    const $sandwichIngredients = $('#sandwichIngredients');
    $sandwichIngredients.empty();

    for (const id in allIngredients) {
        if (allIngredients.hasOwnProperty(id)) {
            const option = `<option value="${id}">${allIngredients[id]}</option>`;
            $sandwichIngredients.append(option);
        }
    }
}

function getSandwichDataFromForm() {
    return {
        name: $('#sandwichName').val(),
        description: $('#sandwichDescription').val(),
        ingredients: $('#sandwichIngredients').val()
    };
}

function createSandwich() {
    let sandwichData = getSandwichDataFromForm();

    $.ajax({
        url: 'http://127.0.0.1:8000/api/sandwich/all/',
        type: 'POST',
        data: JSON.stringify(sandwichData),
        contentType: 'application/json',
        success: function (response) {
            $('#sandwichModal').modal('hide');
            loadSandwiches();
        },
        error: function (error) {
            console.error("Ошибка при добавлении бутерброда: ", error);
        }
    });
}

function getIngredientDataFromForm() {
    return {
        name: $('#ingredientName').val(),
        weight: $('#ingredientWeight').val(),
        kcal: $('#ingredientKcal').val()
    };
}
function createIngredient() {
    let ingredientData = getIngredientDataFromForm();

    $.ajax({
        url: 'http://localhost:8000/api/ingredient/all',
        type: 'POST',
        data: JSON.stringify(ingredientData),
        contentType: 'application/json',
        success: function(response) {
            $('#ingredientModal').modal('hide');
            loadIngredients();
        },
        error: function(error) {
            console.error("Ошибка при добавлении ингредиента: ", error);
        }
    });
}

