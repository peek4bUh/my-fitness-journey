const workoutForm = document.getElementById("workout-form");
const formsContainer = document.getElementById("exercise-forms");
const totalForms = document.getElementById("id_exercises-TOTAL_FORMS");
const addExerciseButton = document.getElementById("add-exercise");
const emptyForm = document.getElementById("empty-exercise-form").innerHTML;
const lastExerciseDataUrl = workoutForm.dataset.lastExerciseDataUrl;

async function fillLastExerciseData(select) {
    const row = select.closest(".exercise-row");
    const volumeInput = row.querySelector("input[name$='-volume']");
    const restInput = row.querySelector("input[name$='-rest']");
    if (!select.value || !volumeInput || !restInput) return;

    try {
        const response = await fetch(
            lastExerciseDataUrl.replace("/0/", `/${select.value}/`));
        if (!response.ok) return;

        const data = await response.json();
        volumeInput.value = data.volume;
        restInput.value = data.rest;
    } catch (error) {
        return;
    }
}

function renumberForms() {
    const rows = formsContainer.querySelectorAll(".exercise-row");
    rows.forEach((row, index) => {
        row.querySelectorAll("[name], [id], [for]").forEach((element) => {
            ["name", "id", "for"].forEach((attribute) => {
                const value = element.getAttribute(attribute);
                if (value) element.setAttribute(attribute, value.replace(/exercises-(?:\d+|__prefix__)-/, `exercises-${index}-`));
            });
        });

        row.querySelector(".move-exercise-up").disabled = index === 0;
        row.querySelector(".move-exercise-down").disabled = index === rows.length - 1;
    });
    totalForms.value = rows.length;
}

addExerciseButton.addEventListener("click", () => {
    formsContainer.insertAdjacentHTML("beforeend", emptyForm.replaceAll("__prefix__", formsContainer.children.length));
    renumberForms();
});

formsContainer.addEventListener("click", (event) => {
    const row = event.target.closest(".exercise-row");
    if (!row) return;

    if (event.target.classList.contains("remove-exercise")) {
        const deleteInput = row.querySelector("input[name$='-DELETE']");
        if (deleteInput) {
            deleteInput.checked = true;
            row.classList.add("hidden");
        } else {
            row.remove();
        }
        renumberForms();
    }

    if (event.target.classList.contains("move-exercise-up")) {
        const previousRow = row.previousElementSibling;
        if (previousRow) formsContainer.insertBefore(row, previousRow);
        renumberForms();
    }

    if (event.target.classList.contains("move-exercise-down")) {
        const nextRow = row.nextElementSibling;
        if (nextRow) formsContainer.insertBefore(nextRow, row);
        renumberForms();
    }
});

formsContainer.addEventListener("change", (event) => {
    if (event.target.matches("select[name$='-exercise']")) {
        fillLastExerciseData(event.target);
    }
});

renumberForms();