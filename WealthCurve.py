"""
An investment calculator named WealthCurve defines a React functional component that calculates and visualizes either 
the total investment value over time or the number of years needed to reach an investment goal
based on the user inputs, use Recharts for data visualization with a line chart.
"""


import { useState } from 'react';
import { LineChart, XAxis, YAxis, Line, CartesianGrid, Tooltip } from 'recharts';

interface WealthCurveProps {}

const WealthCurve: React.FC<WealthCurveProps> = () => {
  const [initialInvestment, setInitialInvestment] = useState<number>(0);
  const [timePeriod, setTimePeriod] = useState<number>(0);
  const [additionalAmount, setAdditionalAmount] = useState<number>(0);
  const [additionalAmountOption, setAdditionalAmountOption] = useState<string>('');
  const [rateOfReturn, setRateOfReturn] = useState<number>(0);
  const [investmentGoal, setInvestmentGoal] = useState<number>(0);
  const [yearsToReachGoal, setYearsToReachGoal] = useState<number>(0);
  const [totalAmount, setTotalAmount] = useState<number>(0);
  const [option, setOption] = useState<string>('');
  const [chartData, setChartData] = useState<Array<{ year: number; value: number }>>([]);

  const calculateInvestmentValue = () => {
    let investmentValue = initialInvestment;
    let chartDataArray = [];
    for (let i = 0; i < timePeriod; i++) {
      if (rateOfReturn >= 0) {
        investmentValue += (rateOfReturn / 100) * investmentValue;
      } else {
        investmentValue -= Math.abs((rateOfReturn / 100) * investmentValue);
      }
      if(additionalAmountOption === 'yearly'){
        investmentValue += additionalAmount;
      } else if(additionalAmountOption === 'monthly'){
        investmentValue += additionalAmount * 12;
      }
      chartDataArray.push({ year: i + 1, value: investmentValue });
    }
    setTotalAmount(investmentValue);
    setChartData(chartDataArray);
  };

  const calculateYearsToReachGoal = () => {
    let years = 0;
    let investmentValue = initialInvestment;
    let chartDataArray = [];
    while (investmentValue < investmentGoal) {
      if(additionalAmountOption === 'yearly'){
        investmentValue += additionalAmount;
      } else if(additionalAmountOption === 'monthly'){
        investmentValue += additionalAmount * 12;
      }
      if (rateOfReturn >= 0) {
        investmentValue += (rateOfReturn / 100) * investmentValue;
      } else {
        investmentValue -= Math.abs((rateOfReturn / 100) * investmentValue);
      }
      years++;
      chartDataArray.push({ year: years, value: investmentValue });
    }
    setYearsToReachGoal(years);
    setChartData(chartDataArray);
  };

  const handleOptionChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
    setOption(event.target.value);
  };

  const handleAdditionalAmountOptionChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
    setAdditionalAmountOption(event.target.value);
  };

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    if (option === 'totalAmount') {
      calculateInvestmentValue();
    } else if (option === 'yearsToReachGoal') {
      calculateYearsToReachGoal();
    }
  };

  return (
    <div className="max-w-7xl mx-auto p-4 md:p-6 lg:p-8 bg-white rounded-md shadow-md flex flex-row">
      <div className="w-full md:w-1/2 lg:w-1/2 xl:w-1/2 p-4 md:p-6 lg:p-8">
        <h2 className="text-lg font-bold mb-4">WealthCurve</h2>
        <form onSubmit={handleSubmit}>
          <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="option">
              Option
            </label>
            <select
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              id="option"
              value={option}
              onChange={handleOptionChange}
            >
              <option value="">Select an option</option>
              <option value="totalAmount">Total Amount</option>
              <option value="yearsToReachGoal">Years to Reach Goal</option>
            </select>
          </div>
          <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="initialInvestment">
              Initial Investment
            </label>
            <input
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              id="initialInvestment"
              type="number"
              value={initialInvestment === 0 ? '' : initialInvestment}
              onChange={(event) => setInitialInvestment(Number(event.target.value))}
            />
          </div>
          <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="additionalAmount">
              Additional Amount
            </label>
            <input
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              id="additionalAmount"
              type="number"
              value={additionalAmount === 0 ? '' : additionalAmount}
              onChange={(event) => setAdditionalAmount(Number(event.target.value))}
            />
            <select
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              id="additionalAmountOption"
              value={additionalAmountOption}
              onChange={handleAdditionalAmountOptionChange}
            >
              <option value="">Select an option</option>
              <option value="yearly">Yearly</option>
              <option value="monthly">Monthly</option>
            </select>
          </div>
          <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="rateOfReturn">
              Rate of Return (in percentage)
            </label>
            <input
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              id="rateOfReturn"
              type="number"
              value={rateOfReturn === 0 ? '' : rateOfReturn}
              onChange={(event) => setRateOfReturn(Number(event.target.value))}
            />
          </div>
          {option === 'totalAmount' && (
            <div className="mb-4">
              <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="timePeriod">
                Time Period (in years)
              </label>
              <input
                className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                id="timePeriod"
                type="number"
                value={timePeriod === 0 ? '' : timePeriod}
                onChange={(event) => setTimePeriod(Number(event.target.value))}
              />
            </div>
          )}
          {option === 'yearsToReachGoal' && (
            <div className="mb-4">
              <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="investmentGoal">
                Investment Goal
              </label>
              <input
                className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                id="investmentGoal"
                type="number"
                value={investmentGoal === 0 ? '' : investmentGoal}
                onChange={(event) => setInvestmentGoal(Number(event.target.value))}
              />
            </div>
          )}
          <button
            className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
            type="submit"
          >
            Calculate
          </button>
        </form>
        {option === 'totalAmount' && (
          <p className="text-lg font-bold mb-4">Total Amount: ${Math.round(totalAmount)}</p>
        )}
        {option === 'yearsToReachGoal' && (
          <p className="text-lg font-bold mb-4">Years to Reach Goal: {yearsToReachGoal}</p>
        )}
      </div>
      <div className="w-full md:w-1/2 lg:w-1/2 xl:w-1/2 p-4 md:p-6 lg:p-8 md:ml-4">
        <LineChart width={400} height={400} data={chartData}>
          <XAxis dataKey="year" />
          <YAxis />
          <CartesianGrid stroke="#ccc" />
          <Tooltip />
          <Line type="monotone" dataKey="value" stroke="#8884d8" />
        </LineChart>
      </div>
    </div>
  );
};

export default WealthCurve;
