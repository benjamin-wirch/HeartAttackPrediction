$('span[data-role="create-btn"]').on('click', event => {
    const username = $('input#username').val().trim().toLowerCase()

    if (username === '') {
        alert('Username is a required field!')
        return
    }

    const name = $('input#name').val().trim()

    if (name === '') {
        alert('Name is a required field!')
        return
    }

    const age = parseInt($('input#age').val().trim())

    if (age === NaN) {
        alert('Invalid age. Age is a required field!')
        return
    }

    let sex = Array.from($('input[name="sex"]').list()).find(radio => radio.get().checked)

    if (!sex) {
        alert('Sex is a required field!')
        return
    } else {
        sex = sex.value
    }

    let chest_pain = Array.from($('input[name="chest-pain"]').list()).find(radio => radio.get().checked)

    if (!chest_pain) {
        alert('Chest Pain is a required field!')
        return
    } else {
        chest_pain = chest_pain.value
    }

    const resting_blood_pressure = parseInt($('input#blood-pressure').val().trim())

    if (resting_blood_pressure === NaN || resting_blood_pressure < 0) {
        alert('Invalid Blood Pressure. Blood Pressure is a required field!')
        return
    }

    const serum_cholestrol = parseInt($('input#serum-cholestrol').val().trim())

    if (serum_cholestrol === NaN || serum_cholestrol < 0) {
        alert('Invalid Serum Cholestrol. Serum Cholestrol is a required field!')
        return
    }

    let fasting_blood_sugar = Array.from($('input[name="fasting-blood-sugar"]').list()).find(radio => radio.get().checked)

    if (!fasting_blood_sugar) {
        alert('Fasting Blood Sugar is a required field!')
        return
    } else {
        fasting_blood_sugar = fasting_blood_sugar.value
    }

    let resting_ecg = Array.from($('input[name="ecg"]').list()).find(radio => radio.get().checked)

    if (!resting_ecg) {
        alert('Resting ECG is a required field!')
        return
    } else {
        resting_ecg = resting_ecg.value
    }

    const max_heart_rate = parseInt($('input#max-heart-rate').val().trim())

    if (max_heart_rate === NaN || max_heart_rate < 0) {
        alert('Invalid Heart Rate. Heart Rate is a required field!')
        return
    }

    let exercise_induced_angina = Array.from($('input[name="angina"]').list()).find(radio => radio.get().checked)

    if (!exercise_induced_angina) {
        alert('Exercise Angina is a required field!')
        return
    } else {
        exercise_induced_angina = exercise_induced_angina.value
    }

    let fluoroscopy_count = Array.from($('input[name="flouroscopy"]').list()).find(radio => radio.get().checked)

    if (!fluoroscopy_count) {
        alert('Fluoroscopy is a required field!')
        return
    } else {
        fluoroscopy_count = fluoroscopy_count.value
    }

    let thalassemia = Array.from($('input[name="thalassaemia"]').list()).find(radio => radio.get().checked)

    if (!thalassemia) {
        alert('Thalassaemia is a required field!')
        return
    } else {
        thalassemia = thalassemia.value
    }

    fetch('/create-patient-record/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': $('input[type="hidden"]').val(),
      },
      body: JSON.stringify({
        username,
        name,
        age,
        sex,
        chest_pain,
        resting_blood_pressure,
        serum_cholestrol,
        fasting_blood_sugar,
        resting_ecg,
        max_heart_rate,
        exercise_induced_angina,
        fluoroscopy_count,
        thalassemia,
      })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Created Successfully!')
            $('label > input[id]').val('')
            $('input[type="radio"]').each(e => {e.get().checked = false})
        } else {
            alert(`Unexpected Error Occurred!\n${data.reason}`)
        }
    })
})
