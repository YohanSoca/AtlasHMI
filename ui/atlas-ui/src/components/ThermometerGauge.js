import React from 'react';
import Thermometer from 'react-thermometer-component';
import './css/ThermometerGauge.css';

function ThermometerGauge() {
  return (
    <div className='thermometer-wrapper'>
    <Thermometer
        theme="dark"
        value="18"
        max="100"
        steps="3"
        format="°C"
        size="medium"
        height="150"
      />
    </div>
  )
}

export default ThermometerGauge