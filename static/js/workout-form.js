const workoutForm = document.getElementById("workout-form");
const formsContainer = document.getElementById("exercise-forms");
const totalForms = document.getElementById("id_exercises-TOTAL_FORMS");
const addExerciseButton = document.getElementById("add-exercise");
const emptyForm = document.getElementById("empty-exercise-form").innerHTML;
const lastExerciseDataUrl = workoutForm.dataset.lastExerciseDataUrl;
const workoutStateKey = "jurnalth-workout-form";

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
        row.querySelectorAll(".last-volume").forEach((element) => {
            element.textContent = data.volume || "";
        });
        updateExerciseSummary(select.closest(".exercise-row"));
    } catch (error) {
        return;
    }
}

function updateExerciseSummary(row) {
    if (!row) return;
    const exerciseField = row.querySelector("[name$='-exercise']");
    const nameElement = row.querySelector(".exercise-summary-name");
    if (!nameElement) return;

    if (exerciseField?.value && nameElement.textContent === "Choose an exercise") {
        nameElement.textContent = `Exercise ${exerciseField.value}`;
    }
}

function syncVolumeFromSets(row) {
    const volumeInput = row.querySelector("input[name$='-volume']");
    if (!volumeInput) return;

    const sets = [...row.querySelectorAll(".set-row")].map((set) => {
        const weight = set.querySelector(".set-weight").value.trim();
        const reps = set.querySelector(".set-reps").value.trim();
        if (!weight && !reps) return "";
        return `1x${weight || ""}x${reps || ""}`;
    }).filter(Boolean);
    if (sets.length) volumeInput.value = sets.join(", ");
    updateExerciseSummary(row);
}

function renumberSets(row) {
    row.querySelectorAll(".set-row").forEach((set, index) => {
        set.querySelector(".set-number").textContent = index + 1;
        updateSetCompletionState(set);
    });
}

function updateSetCompletionState(set) {
    const reps = set.querySelector(".set-reps")?.value.trim();
    const weight = set.querySelector(".set-weight")?.value.trim();
    const checkbox = set.querySelector(".set-completed");
    const label = checkbox?.closest("label");
    if (!checkbox || !label) return;

    const canComplete = Boolean(reps && weight);
    checkbox.disabled = !canComplete;
    if (!canComplete) checkbox.checked = false;
    label.classList.toggle("cursor-pointer", canComplete);
    label.classList.toggle("cursor-not-allowed", !canComplete);
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

function addSelectedExercise() {
    const params = new URLSearchParams(window.location.search);
    const exerciseIds = params.getAll("exercise_id");
    const exerciseNames = params.getAll("exercise_name");
    if (!exerciseIds.length) return;

    exerciseIds.forEach((exerciseId, index) => {
        let row = [...formsContainer.querySelectorAll(".exercise-row")]
            .find((candidate) => !candidate.querySelector("[name$='-exercise']").value);

        if (!row) row = addEmptyRow();

        const exerciseField = row.querySelector("[name$='-exercise']");
        exerciseField.value = exerciseId;
        if (exerciseNames[index]) {
            row.querySelector(".exercise-summary-name").textContent = exerciseNames[index];
        }
        updateExerciseSummary(row);
        fillLastExerciseData(exerciseField);
    });
    window.history.replaceState({}, document.title, window.location.pathname);
}

function addEmptyRow() {
    formsContainer.insertAdjacentHTML("beforeend", emptyForm.replaceAll("__prefix__", formsContainer.children.length));
    renumberForms();
    return formsContainer.lastElementChild;
}

function saveWorkoutState() {
    const fields = [...workoutForm.elements]
        .filter((element) => element.name && element.type !== "submit")
        .map((element) => ({
            name: element.name,
            value: element.value,
            checked: element.checked,
        }));
    const names = [...formsContainer.querySelectorAll(".exercise-summary-name")]
        .map((element) => element.textContent.trim());
    sessionStorage.setItem(workoutStateKey, JSON.stringify({ fields, names }));
}

function restoreWorkoutState() {
    const savedFields = sessionStorage.getItem(workoutStateKey);
    if (!savedFields) return;

    const savedState = JSON.parse(savedFields);
    const fieldsToRestore = savedState.fields || savedState;
    const rowIndexes = fieldsToRestore
        .map((field) => field.name.match(/^exercises-(\d+)-/))
        .filter(Boolean)
        .map((match) => Number(match[1]));
    const rowsNeeded = rowIndexes.length ? Math.max(...rowIndexes) + 1 : 0;
    while (formsContainer.children.length < rowsNeeded) addEmptyRow();

    fieldsToRestore.forEach((savedField) => {
        const fields = [...workoutForm.elements].filter(
            (element) => element.name === savedField.name);
        const field = fields[0];
        if (!field) return;
        field.value = savedField.value;
        if (field.type === "checkbox") field.checked = savedField.checked;
    });
    (savedState.names || []).forEach((name, index) => {
        const nameElement = formsContainer.children[index]?.querySelector(".exercise-summary-name");
        if (nameElement && name) nameElement.textContent = name;
    });
    sessionStorage.removeItem(workoutStateKey);
}

addExerciseButton.addEventListener("click", (event) => {
    event.preventDefault();
    saveWorkoutState();
    window.location.href = addExerciseButton.href;
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

    if (event.target.classList.contains("toggle-exercise-edit")) {
        const fields = row.querySelector(".exercise-edit-fields");
        const isCollapsed = fields.classList.toggle("hidden");
        event.target.textContent = isCollapsed ? "Edit" : "Close";
        event.target.setAttribute("aria-expanded", String(!isCollapsed));
    }

    if (event.target.classList.contains("add-set")) {
        const rows = row.querySelector(".set-rows");
        rows.insertAdjacentHTML("beforeend", `
            <div class="set-row grid grid-cols-[3rem_minmax(0,1fr)_minmax(0,1fr)_4rem] items-center py-2 transition-colors hover:bg-gray-50">
                <span class="set-number px-2 text-sm text-gray-500"></span>
                <input type="number" min="1" class="set-reps mx-2 min-w-0 rounded-sm border border-gray-200 px-2 py-1.5 text-sm focus:border-gray-700 focus:outline-none focus:ring-0">
                <input type="number" step="0.5" class="set-weight mx-2 min-w-0 rounded-sm border border-gray-200 px-2 py-1.5 text-sm focus:border-gray-700 focus:outline-none focus:ring-0">
                <div class="flex items-center justify-end gap-1">
                    <label class="inline-flex h-7 w-7 cursor-pointer items-center justify-center" title="Mark set as done">
                        <input type="checkbox" disabled class="set-completed h-4 w-4 rounded-sm border-gray-300 text-gray-900 focus:border-gray-700 focus:ring-0 disabled:cursor-not-allowed disabled:opacity-50">
                        <span class="sr-only">Mark set as done</span>
                    </label>
                    <button type="button" class="remove-set inline-flex h-7 w-7 cursor-pointer items-center justify-center rounded-sm text-sm font-medium text-gray-400 transition-colors hover:bg-gray-200 hover:text-gray-900" title="Delete set" aria-label="Delete set">×</button>
                </div>
            </div>`);
        renumberSets(row);
    }

    if (event.target.classList.contains("remove-set")) {
        event.target.closest(".set-row").remove();
        renumberSets(row);
        syncVolumeFromSets(row);
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
    if (event.target.matches("[name$='-exercise']")) {
        updateExerciseSummary(event.target.closest(".exercise-row"));
        fillLastExerciseData(event.target);
    }
});

formsContainer.addEventListener("input", (event) => {
    if (event.target.matches(".set-weight, .set-reps")) {
        const set = event.target.closest(".set-row");
        updateSetCompletionState(set);
        syncVolumeFromSets(event.target.closest(".exercise-row"));
    }
    if (event.target.matches("input[name$='-volume'], input[name$='-rest']")) {
        updateExerciseSummary(event.target.closest(".exercise-row"));
    }
});

workoutForm.addEventListener("submit", () => {
    formsContainer.querySelectorAll(".exercise-row").forEach(syncVolumeFromSets);
});

restoreWorkoutState();
renumberForms();
formsContainer.querySelectorAll(".set-row").forEach(updateSetCompletionState);
addSelectedExercise();
