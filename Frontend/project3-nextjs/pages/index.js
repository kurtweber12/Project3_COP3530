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
import { HttpSubmitForm } from '@/requests/httpRequests';

import Form from '@/components/Form';

ChartJS.register(
	CategoryScale,
	LinearScale,
	BarElement,
	Title,
	Tooltip,
	Legend
  );


export default function Home() {


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
		month: "",
		day: "",
		year: "",
	})

	const [loading, setLoading] = useState(false)

	const handleInputChange = (event) => {
		const { name, value } = event.target;
		setFormValues((prevValues) => ({
			...prevValues,
			[name]: value,
		}));
	};

	const handleSubmit = async () => {
		setLoading(true)
		let response = await HttpSubmitForm(formValues.day, formValues.month, formValues.year, formValues.location)
		console.log(response)
		setLoading(false)

	}

	return (
		<main
		className="flex min-h-screen flex-col items-center space-y-16 p-24"
		>
			<div className='flex flex-row space-x-16'>
				<Form 
					onSubmit={handleSubmit}
					handleInputChange={handleInputChange}
					formValues={formValues}
					setFormValues={setFormValues}
					loading={loading}
				/>
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
