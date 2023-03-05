$('input[type="checkbox"]').on('click', event => {
    if ($('input[type="checkbox"]').get().checked) {
        $('input#password-input').get().type = 'text'
    } else {
        $('input#password-input').get().type = 'password'
    }
})

$('span[data-role="sign-up"]').on('click', event => {
    let error = false
    const username = $('input#username-input').val().trim().toLowerCase()
    if (username === '') {
        $('small[data-role="username-error"]').addClass('err')
        error = true
    } else {
        $('small[data-role="username-error"]').removeClass('err')
        error = false
    }

    const password = $('input#password-input').val().trim().toLowerCase()
    if (password === '') {
        $('small[data-role="password-error"]').addClass('err')
        error = true
    } else {
        $('small[data-role="password-error"]').removeClass('err')
        error = false
    }

    if (error) return

    fetch(`/signup/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': $('input[type="hidden"]').val(),
      },
      body: JSON.stringify({
        username,
        password
      })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            window.location.replace('/dashboard/')
        } else {
            alert('Unexpected Error Occurred!')
            console.error({username, password});
        }
    })
})
