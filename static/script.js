console.log("JavaScript loaded successfully");

document.getElementById("loanForm").addEventListener("submit", function(event) {

    event.preventDefault();

    let name = document.getElementById("name").value.trim();
    let studentId = document.getElementById("student_id").value.trim();
    let course = document.getElementById("course").value.trim();
    let loanAmount = document.getElementById("loan_amount").value;

    if (name === "") {
        alert("Please enter your full name.");
        return;
    }

    if (studentId === "") {
        alert("Please enter your Student ID.");
        return;
    }

    if (course === "") {
        alert("Please enter your course.");
        return;
    }

    if (loanAmount === "") {
        alert("Please enter the loan amount.");
        return;
    }

    if (Number(loanAmount) <= 0) {
        alert("Loan amount must be greater than 0.");
        return;
    }

    fetch("/api/loan", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            name: name,
            student_id: studentId,
            course: course,
            loan_amount: loanAmount
        })
    })
    .then(response => response.json())
    .then(data => {

        if (data.error) {
            alert(data.error);
            return;
        }

        document.getElementById("result").innerHTML =
            "<h2>" + data.status + "</h2>" +
            "<p>" + data.message + "</p>" +
            "<p>Applicant: " + data.name + "</p>" +
            "<p>Student ID: " + data.student_id + "</p>" +
            "<p>Course: " + data.course + "</p>" +
            "<p>Loan Amount: " + data.loan_amount + "</p>";

    })
    .catch(error => {

        console.error("Error:", error);

        alert("Something went wrong while submitting the application.");

    });

});

function editApplication(id) {

    let name = prompt("Enter new student name:");

    if (name === null) {
        return;
    }

    name = name.trim();

    if (name === "") {
        alert("Student name cannot be empty.");
        return;
    }

    let course = prompt("Enter new course:");

    if (course === null) {
        return;
    }

    course = course.trim();

    if (course === "") {
        alert("Course cannot be empty.");
        return;
    }

    let loanAmount = prompt("Enter new loan amount:");

    if (loanAmount === null) {
        return;
    }

    loanAmount = loanAmount.trim();

    if (loanAmount === "" || Number(loanAmount) <= 0) {
        alert("Loan amount must be greater than 0.");
        return;
    }

    fetch("/api/applications/" + id, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            name: name,
            course: course,
            loan_amount: loanAmount
        })
    })
    .then(response => response.json())
    .then(data => {

        if (data.error) {
            alert(data.error);
            return;
        }

        alert(data.message);

        location.reload();

    })
    .catch(error => {

        console.error("Edit error:", error);

        alert("Failed to update application.");

    });

}

function searchApplications() {

    let searchValue = document
        .getElementById("searchInput")
        .value
        .toLowerCase();

    let rows = document.querySelectorAll("#applications tr");

    rows.forEach(row => {

        let rowText = row.innerText.toLowerCase();

        if (rowText.includes(searchValue)) {
            row.style.display = "";
        } else {
            row.style.display = "none";
        }

    });

}

function filterApplications() {

    let selectedStatus = document
        .getElementById("statusFilter")
        .value;

    let rows = document.querySelectorAll("#applications tr");

    rows.forEach(row => {

        let status = row.cells[5].innerText.trim();

        if (selectedStatus === "All" || status === selectedStatus) {

            row.style.display = "";

        } else {

            row.style.display = "none";

        }

    });

}

function deleteApplication(id) {

    if (!confirm("Are you sure you want to delete this application?")) {
        return;
    }

    fetch("/api/applications/" + id, {
        method: "DELETE"
    })
    .then(response => response.json())
    .then(data => {

        if (data.error) {
            alert(data.error);
            return;
        }

        alert(data.message);

        location.reload();

    })
    .catch(error => {

        console.error("Delete error:", error);

        alert("Failed to delete application.");

    });

}