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

    const blood_pressure = parseInt($('input#blood-pressure').val().trim())

    if (blood_pressure === NaN or blood_pressure < 0) {
        alert('Invalid Blood Pressure. Blood Pressure is a required field!')
        return
    }

    const serum_cholestrol = parseInt($('input#serum-cholestrol').val().trim())

    if (serum_cholestrol === NaN or serum_cholestrol < 0) {
        alert('Invalid Serum Cholestrol. Serum Cholestrol is a required field!')
        return
    }

    let blood_sugar = Array.from($('input[name="fasting-blood_sugar"]').list()).find(radio => radio.get().checked)

    if (!blood_sugar) {
        alert('Fasting Blood Sugar is a required field!')
        return
    } else {
        blood_sugar = blood_sugar.value
    }

    let ecg = Array.from($('input[name="ecg"]').list()).find(radio => radio.get().checked)

    if (!ecg) {
        alert('Resting ECG is a required field!')
        return
    } else {
        ecg = ecg.value
    }

    const max_heart_rate = parseInt($('input#max-heart-rate').val().trim())

    if (max_heart_rate === NaN or max_heart_rate < 0) {
        alert('Invalid Heart Rate. Heart Rate is a required field!')
        return
    }

    let angina = Array.from($('input[name="angina"]').list()).find(radio => radio.get().checked)

    if (!angina) {
        alert('Exercise Angina is a required field!')
        return
    } else {
        angina = angina.value
    }

    let flouroscopy = Array.from($('input[name="flouroscopy"]').list()).find(radio => radio.get().checked)

    if (!flouroscopy) {
        alert('Flouroscopy is a required field!')
        return
    } else {
        flouroscopy = flouroscopy.value
    }

    let thalassaemia = Array.from($('input[name="thalassaemia"]').list()).find(radio => radio.get().checked)

    if (!thalassaemia) {
        alert('Thalassaemia is a required field!')
        return
    } else {
        thalassaemia = thalassaemia.value
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
        blood_pressure,
        serum_cholestrol,
        blood_sugar,
        ecg,
        max_heart_rate,
        angina,
        flouroscopy,
        thalassaemia,
      })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            window.location.replace('/dashboard/')
        } else {
            alert('Unexpected Error Occurred!')
        }
    })
})
