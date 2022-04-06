import React from 'react';
import { Routes, Route, Link } from "react-router-dom";

function Home() {
  return (
    <div>
    <div>
    <Link className='page-link' to="/">Home</Link>
    <Link className='page-link' to="port">PORT</Link>
    <Link className='page-link' to="stbd">STBD</Link>
    <Link className='page-link' to="shore">Shore</Link>
    <Link className='page-link' to="alarms">Alarms</Link>
    <Link className='page-link' to="transfer">Transfer</Link>
    <Link className='page-link' to="setup">Setup</Link>
  </div>
    </div>
  )
}

export default Home