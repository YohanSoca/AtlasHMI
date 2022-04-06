import React from 'react';
import GaugeChart from 'react-gauge-chart';
import '../components/css/Gauge.css';

function Gauge() {
    const chartStyle = {
        height: 200,
        width: 300
      }

  return (
    <div className="gauge-wrapper">
        <h3>Name: Value</h3>
        <GaugeChart id="gauge" style={chartStyle} />
    </div>
  )
}

export default Gauge