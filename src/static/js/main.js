function confirmDelete(){
    const ok = confirm("Are you sure you want to delete item?")
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

function likeOrUnlikeVacation(vacationID, action) {
    fetch(`/vacations/like/${vacationID}/${action}`)
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            const likeBtn = document.getElementById(`like-btn-${vacationID}`);
            const heartIcon = document.getElementById(`heart-icon-${vacationID}`);
            const likeCount = document.getElementById(`like-count-${vacationID}`);
            const likedUrl = likeBtn.getAttribute('data-liked-url');
            const unlikedUrl = likeBtn.getAttribute('data-unliked-url');

            // Update like count
            likeCount.innerText = data.like_count;

            // Update heart icon
            if (data.user_liked) {
                heartIcon.src = likedUrl;
                likeBtn.setAttribute('onclick', `event.preventDefault(); likeOrUnlikeVacation('${vacationID}', 'unlike');`);
                
            } else {
                heartIcon.src = unlikedUrl;
                likeBtn.setAttribute('onclick', `event.preventDefault(); likeOrUnlikeVacation('${vacationID}', 'like');`);
            }

            // Toggle 'liked' class
            likeBtn.classList.toggle('liked', data.user_liked);
        } else {
            alert(data.message);
        }
    })
    .catch(error => console.error('Error:', error));
}

flatpickr("#start_date", {
    dateFormat: "d/m/Y",
    minDate: "1997-01-01",
    onChange: function(_, dateStr) {
        // Update the minDate for the end date input to be the selected start date
        endDatePicker.set("minDate", dateStr);
    }
});

// Initialize flatpickr for the end date
var endDatePicker = flatpickr("#end_date", {
    dateFormat: "d/m/Y",
    minDate: "1997-01-01" 
});

document.getElementById('country').addEventListener('change', function() {
    var selectedOption = this.options[this.selectedIndex];
    document.getElementById('country-name-input').value = selectedOption.getAttribute('data-country-name');
});
