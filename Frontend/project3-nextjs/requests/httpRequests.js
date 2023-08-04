const API_URL = 'http://localhost:8000'

async function HttpSubmitForm(day, month, year, location){
    const data = {
        "day": day,
        "month": month,
        "year": year,
        "location": location
    }

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

export { HttpSubmitForm }