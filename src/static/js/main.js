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

function likeVacation(vacations_ID, csrf_token, user_ID) {
    fetch(`/vacations/like/${vacations_ID}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrf_token
        },
        body: JSON.stringify({ user_ID: user_ID })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            const likeBtn = document.getElementById(`like-btn-${vacations_ID}`);
            const likeCount = document.getElementById(`like-count-${vacations_ID}`);
            likeCount.innerText = data.like_count;
            likeBtn.classList.toggle('liked', data.user_liked);
        } else {
            alert('Error liking the vacation.');
        }
    })
    .catch(error => console.error('Error:', error));
}

function confirmDelete(vacationID) {
    if (confirm('Are you sure you want to delete this vacation?')) {
        window.location.href = `/vacation/delete/${vacationID}`;
    }
}