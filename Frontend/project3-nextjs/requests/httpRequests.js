const API_URL = 'http://localhost:8000' // url for our django server

// called inside the handleSubmit function for the Form
async function HttpSubmitForm(day, month, year, location){
    // 'data' is the structure of our data we send with our post requesr
    const data = {
        "day": day,
        "month": month,
        "year": year,
        "location": location
    }

    console.log(data)

    try{
        const response = await fetch(`${API_URL}/search-results/`, {
            method: "post",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data),
        })

        return response
    } catch(error) {
        console.log(error)
        return error
    }
}

// called by the fetch_dropdown function inside of the useEffect on the Form component
async function HttpDropdown() {
    try {
        const response = await fetch(`${API_URL}/dropdown/`)
        return response.json()
    } catch(error){
        return error
    }
}

export { HttpSubmitForm, HttpDropdown }