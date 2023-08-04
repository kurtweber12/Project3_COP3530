import React, { useEffect, useState } from 'react'
import { BarLoader } from "react-spinners";
import { HttpDropdown } from '@/requests/httpRequests';

const Form = ({onSubmit, handleInputChange, formValues, setFormValues, loading}) => {

    const [dropDownList, setDropDownList] = useState([])
    const months_dropdown = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
    const years_dropdown = ["2019", "2020"]
    const days_dropdown = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", 
        "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"
    ]

    const handleSubmit = (event) => {
		event.preventDefault();
        //console.log(formValues)
		onSubmit(formValues);
	};

    useEffect(() => {
		const fetch_dropdown = async () => {
			const dropdown_response = await HttpDropdown()
			console.log(dropdown_response)
			console.log(dropdown_response["unique_countries"])
            
            const dropdown = dropdown_response["unique_countries"]
            dropdown.sort(function(a,b) {
                if(a < b){
                    return -1;
                } 
                if(a > b) {
                    return 1
                }
                return 0
            })

			setDropDownList(dropdown_response["unique_countries"])
		}

		fetch_dropdown()
	}, [])


    return (
        <form className='form-container' onSubmit={handleSubmit}>
            <p className='text-red-400'>* denoted required field</p>
            <div className='form-field'>
                <label><span className='text-red-400'>* </span>Location:</label>
                <select
                    name="location"
                    value={formValues.location}
                    onChange={handleInputChange} 
                    className='dropdown-field'
                    required
                >
                    <option value="">Select Option</option>
                    {dropDownList?.map((item, i) => (
                        <option value={item} key={i}>
                            {item}
                        </option>
                    )

                    )}
                </select>
            </div>
            <div className='form-field'>
                <label><span className='text-red-400'>* </span>Month:</label>
                <select
                    name="month"
                    value={formValues.month}
                    onChange={handleInputChange} 
                    className='dropdown-field'
                    required
                >
                    <option value="">Select Option</option>
                    {months_dropdown.map((item, i) => (
                        <option value={item} key={i}>
                            {item}
                        </option>
                    )
                    )}
                </select>
            </div>
            <div className='form-field'>
                <label><span className='text-red-400'>* </span>Day:</label>
                <select
                    name="day"
                    value={formValues.day}
                    onChange={handleInputChange} 
                    className='dropdown-field'
                    required
                >
                    <option value="">Select Option</option>
                    {days_dropdown.map((item, i) => (
                        <option value={item} key={i}>
                            {item}
                        </option>
                    )
                    )}
                </select>
            </div>
            <div className='form-field'>
                <label><span className='text-red-400'>* </span>Year:</label>
                <select
                    name="year"
                    value={formValues.year}
                    onChange={handleInputChange} 
                    className='dropdown-field'
                    required
                >
                    <option value="">Select Option</option>
                    {years_dropdown.map((item, i) => (
                        <option value={item} key={i}>
                            {item}
                        </option>
                    )
                    )}
                </select>
            </div>
            <button className='form-button'>Search</button>
            <BarLoader loading={loading} color='#fff' className="self-center mt-8" />
        </form>
    )
}

export default Form