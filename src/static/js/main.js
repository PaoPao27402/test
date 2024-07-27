function confirmDelete(){
    const ok = confirm("Are you sure you want to delete item 👀?")
    if (!ok){
        event.preventDefault()
    }
}

const errorSpan = document.querySelector(".error");
if(errorSpan){
    setTimeout(()=>{
        errorSpan.parentElement.removeChild(errorSpan);
    }, 40000)
}

function saveUser(){
    let email = document.getElementById("email").value;
    localStorage.setItem("email", email);
    alert("ok")
}

function likeVacation(vacationID, csrfToken, userID) {
    fetch(`/vacations/like/${vacationID}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify({ user_ID: userID })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            const likeBtn = document.getElementById(`like-btn-${vacationID}`);
            const likeCount = document.getElementById(`like-count-${vacationID}`);
            likeCount.innerText = data.like_count;
            likeBtn.classList.toggle('liked', data.user_liked);
        } else {
            alert('Error liking the vacation.');
        }
    })
    .catch(error => console.error('Error:', error));
}

function confirmDelete(vacationID) {
    if (confirm("Are you sure you want to delete this vacation?")) {
        window.location.href = `/vacations/delete/${vacationID}`;
    }
}
