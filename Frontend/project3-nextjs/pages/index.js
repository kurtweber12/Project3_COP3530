import Image from 'next/image'
import { Inter } from 'next/font/google'
import { useState } from 'react';
import {
	Chart as ChartJS,
	CategoryScale,
	LinearScale,
	BarElement,
	Title,
	Tooltip,
	Legend,
  } from 'chart.js';
import { Bar } from 'react-chartjs-2';
import { BarLoader } from "react-spinners";

ChartJS.register(
	CategoryScale,
	LinearScale,
	BarElement,
	Title,
	Tooltip,
	Legend
  );


export default function Home() {

	const locations_dropdown = ["location1", "location2", "location3", "location4"]
	const dates_dropdown = ["date1", "date2", "date3", "date4"]
	const dummy_chart_data = {
		labels: ["Search 1", "Search 2"],
		datasets: [{
			label: "Time for Search Algorithm (Seconds)",
			data: [36, 4],
			borderWidth: 1,
			backgroundColor: 'rgba(255, 99, 132, 0.5)',
		}]
	}

	const chart_options = {
		title: {
			display: true,
			text: "Search Times Comparison",
		},
		scales: {
			y: {
				beginAtZero: true
			},
		}
	}

	const [formValues, setFormValues] = useState({
		location: "",
		date: ""
	})

	const [loading, setLoading] = useState(true)

	const handleInputChange = (event) => {
		const { name, value } = event.target;
		setFormValues((prevValues) => ({
			...prevValues,
			[name]: value,
		}));
	};

	const handleSubmit = (event) => {
		event.preventDefault();
		// onSubmit(formValues);
	};

	return (
		<main
		className="flex min-h-screen flex-col items-center space-y-16 p-24"
		>
			<div className='flex flex-row space-x-16'>
				<form className='form-container' onSubmit={handleSubmit}>
					<div className='form-field'>
						<label>Location:</label>
						<select
							name="location"
							value={formValues.location}
							onChange={handleInputChange} 
							className='dropdown-field'
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
						<label>Date:</label>
						<select
							name="location"
							value={formValues.location}
							onChange={handleInputChange} 
							className='dropdown-field'
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
				<div className='chart-container'>
					<Bar data={dummy_chart_data} options={chart_options} />
				</div>

			</div>
			<div className='flex flex-col'>
				<h2 className='text-2xl mb-2'><span className='border-b'>Search Times</span></h2>
				<div className='flex flex-row w-[300px] justify-between'>
					<p>Sentinel Linear Search: </p>
					{loading ? (<p className='text-gray-400'>Loading...</p>) : (<p>36 seconds</p>)}
				</div>
				<div className='flex flex-row w-[300px] justify-between'>
					<p>Ternary Search: </p>
					{loading ? (<p className='text-gray-400'>Loading...</p>) : (<p>4 seconds</p>)}
				</div>
			</div>
		</main>
	)
}
