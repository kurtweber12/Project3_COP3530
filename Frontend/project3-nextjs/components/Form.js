import React from 'react'
import { BarLoader } from "react-spinners";

const Form = ({onSubmit, handleInputChange, formValues, setFormValues, loading}) => {

    const locations_dropdown = ["location1", "location2", "location3", "location4"]
    const dates_dropdown = ["date1", "date2", "date3", "date4"]

    const handleSubmit = (event) => {
		event.preventDefault();
		onSubmit(formValues);
	};


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
                    {locations_dropdown.map((item, i) => (
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
                    {dates_dropdown.map((item, i) => (
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
                    {dates_dropdown.map((item, i) => (
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
                    {dates_dropdown.map((item, i) => (
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