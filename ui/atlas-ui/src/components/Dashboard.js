import React from 'react';
import '../components/css/Dashboard.css';

function Dashboard({ children }) {
    
  return (
    <div className='dashboard'>
        { children }
    </div>
  )
}

export default Dashboard