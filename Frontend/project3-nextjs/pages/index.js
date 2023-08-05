import Image from 'next/image'
import { Inter } from 'next/font/google'
import { useEffect, useState } from 'react';
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
import { HttpDropdown, HttpSubmitForm } from '@/requests/httpRequests';

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

	const [timeChartData, setTimeChartData] = useState([0,0])
	const [covidCases, setCovidCases] = useState(0)
	const [covidDeaths, setCovidDeaths] = useState(0)
	const [countryName, setCountryName] = useState("")
	const [continent, setContinent] = useState("")
	const [population, setPopulation] = useState(0)


	const search_chart_data = {
		labels: ["Sentinel Linear Search ", "Ternary Search"],
		datasets: [{
			label: "Time for Search Algorithm (ms)",
			data: timeChartData,
			borderWidth: 1,
			backgroundColor: 'rgba(255, 99, 132, 0.5)',
		}]
	}

	const covid_chart_data = {
		labels: ["Cases", "Deaths"],
		datasets: [{
			data: [covidCases, covidDeaths],
			borderWidth: 1,
			backgroundColor: 'rgba(19, 144, 90, 0.8)',
		}]
	}

	const chart_options = {
		responsive: true,
		plugins: {
			legend: false,
			title: {
				display: true,
				text: "Search Times Comparison",
			},
		},
		scales: {
			y: {
				beginAtZero: true
			},
		}
	}
	const covid_chart_options = {
		responsive: true,
		plugins: {
			legend: false,
			title: {
				display: true,
				text: "Cases and Deaths",
			},
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
	const [httpResponse, setHttpResponse] = useState({})


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
		if(response.ok){
			let json_response = await response.json()
			console.log(json_response)
			setHttpResponse(json_response)
			setTimeChartData([json_response.linear_time, json_response.ternary_time])
			if(json_response.linear_covid.length < 1){
				setCovidCases(0)
				setCovidDeaths(0)
				setContinent("")
				setCountryName("")
				setPopulation(0)
			} else {
				setCovidCases(json_response.linear_covid[3])
				setCovidDeaths(json_response.linear_covid[4])
				setContinent(json_response.linear_covid[8])
				setCountryName(json_response.linear_covid[5])
				setPopulation(json_response.linear_covid[7])
			}
		}
		setLoading(false)

	}

	

	return (
		<main
		className="flex min-h-screen flex-col items-center space-y-16 p-24"
		>
			<div className='flex flex-col items-center'>
				<h1 className='text-4xl font-thin tracking-widest'>DeGenerates Covid</h1>
				<h2 className='text-lg font-semibold text-gray-500'>By Zero Segmentation Fault</h2>
			</div>
			<div className='flex flex-row space-x-16'>
				<Form 
					onSubmit={handleSubmit}
					handleInputChange={handleInputChange}
					formValues={formValues}
					setFormValues={setFormValues}
					loading={loading}
				/>
			</div>
			<div className='flex flex-col'>
				<div className='mt-8 data-containers'>
					<div>
						<h2 className='text-2xl mb-2'><span className='border-b'>Covid Data</span></h2>
						<div className='search-covid-sections'>
							<p>Continent: </p>
							{loading ? (<p className='text-gray-400'>Loading...</p>) : (<p>{continent}</p>)}
						</div>
						<div className='search-covid-sections'>
							<p>Country: </p>
							{loading ? (<p className='text-gray-400'>Loading...</p>) : (<p>{countryName}</p>)}
						</div>
						<div className='search-covid-sections'>
							<p>Population: </p>
							{loading ? (<p className='text-gray-400'>Loading...</p>) : (<p>{population}</p>)}
						</div>
						<div className='search-covid-sections'>
							<p>Cases: </p>
							{loading ? (<p className='text-gray-400'>Loading...</p>) : (<p>{covidCases}</p>)}
						</div>
						<div className='search-covid-sections'>
							<p>Deaths: </p>
							{loading ? (<p className='text-gray-400'>Loading...</p>) : (<p>{covidDeaths}</p>)}
						</div>
					</div>
					<div className='chart-container'>
						<Bar data={covid_chart_data} options={covid_chart_options} />
					</div>
				</div>
				<div className='data-containers'>
					<div>
						<h2 className='text-2xl mb-2'><span className='border-b'>Search Times (ms)</span></h2>
						<div className='flex flex-row w-[400px] justify-between'>
							<p>Sentinel Linear Search: </p>
							{loading ? (<p className='text-gray-400'>Loading...</p>) : (<p>{httpResponse?.linear_time}</p>)}
						</div>
						<div className='flex flex-row w-[400px] justify-between'>
							<p>Ternary Search: </p>
							{loading ? (<p className='text-gray-400'>Loading...</p>) : (<p>{httpResponse?.ternary_time}</p>)}
						</div>
						<div className='flex flex-row w-[400px] justify-between mt-4 text-gray-500 text-sm'>
							<p>Note: Each iteration for the searches contains a sleep period of 0.00001 seconds in order to exagerate results</p>
						</div>
					</div>
					<div className='chart-container'>
						<Bar data={search_chart_data} options={chart_options} />
					</div>
				</div>
				
			</div>
		</main>
	)
}
