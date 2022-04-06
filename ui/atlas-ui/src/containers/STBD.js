import React from 'react';
import { styled } from '@mui/material/styles';
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import Grid from '@mui/material/Grid';
import './css/STBD.css';
import '../components/css/Dashboard.css';
import Dashboard from '../components/Dashboard';
import Gauge from '../components/Gauge';
import Header from '../components/Header';
import Controller from '../components/Controller';
import ThermometerGauge from '../components/ThermometerGauge';

function STBD() {
  return (
    <Dashboard className='dashboard'>
    <Grid item xs={12}>
        <Controller />
    </Grid>
    <Box sx={{ flexGrow: 1 }}>
    <Grid container spacing={2}>
      <Grid item xs={4}>
        <Gauge />
      </Grid>
      <Grid item xs={4}>
        <Gauge />
      </Grid>
      <Grid item xs={4}>
      <Gauge />
      </Grid>
      <Grid item xs={4}>
        <ThermometerGauge />
      </Grid>
      <Grid item xs={4}>
        <ThermometerGauge />
      </Grid>
      <Grid item xs={4}>
        <ThermometerGauge />
      </Grid>
      <Grid item xs={12}>
        <Controller />
      </Grid>
    </Grid>
    </Box>
  </Dashboard>  
  )
}

export default STBD