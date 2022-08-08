// Add event listener
document.addEventListener("DOMContentLoaded", () => {
    document.querySelector("#sample-form").addEventListener('submit', sampleSubmit);
});


// Submit function
function sampleSubmit(event) {
    event.preventDefault();
    let messageHeader = document.querySelector("#message");
    let message = document.querySelector("#sample-input").value;

    let requestBody = {
        "message": message
    };

    sendHttpAsync("/return-message", "POST", requestBody)
        .then(response => {
            messageHeader.innerText = response.body.message;
        });
}


// Function to send HTTP requests
function sendHttpAsync(path, method, body) {
    let props = {
        method: method,
        headers: {
            "X-CSRFToken": getCookie("csrftoken")
        },
        mode: "same-origin",
    }

    if (body !== null && body !== undefined) {
        props.body = JSON.stringify(body);
    }

    return fetch(path, props)
        .then(response => {
            return response.json()
                .then(result => {
                    return {
                        ok: response.ok,
                        body: result
                    }
                });
        })
        .then(resultObj => {    
            return resultObj;
        })
        .catch(error => {
            throw error;
        });
}


// Function to get cookie by name; retrieved from https://docs.djangoproject.com/en/3.1/ref/csrf/
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}