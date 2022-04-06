import React from 'react';
import './css/STBD.css';
import '../components/css/Dashboard.css';
import Dashboard from '../components/Dashboard';
import styled from 'styled-components';
import { useState, useEffect } from 'react';
import { Routes, Route, Link } from "react-router-dom";

function Shore({ content }) {

  const [shore, setShore] = useState();
  
  console.log(`from shore: ${content ?? ' '}`)
  return (
    <>
    <ShorePowerValues>
      <Card>
        <Meters>
          <VoltsGauge>
            <h3>
              { content['Shore Converter Output digital meter'][11]['L2-N Volts'] }V
            </h3>
            <h3>
              { content['Shore Converter Output digital meter'][10]['L1-N Volts'] }V
            </h3>
            <h3>
              { content['Shore Converter Output digital meter'][12]['L3-N Volts'] }V
            </h3>
            </VoltsGauge>
          <AmpsGauge>
            <h3>
              { content['Shore Converter Output digital meter'][0]['L1 Amps'] }A
            </h3>
            <h3>
              { content['Shore Converter Output digital meter'][1]['L2 Amps'] }A
            </h3>
            <h3>
              { content['Shore Converter Output digital meter'][2]['L3 Amps'] }A
            </h3>
          </AmpsGauge>
        </Meters>
      </Card>
      <Card>
        <Meters>
          <VoltsGauge><h2>210V</h2><h2>210V</h2><h2>210V</h2></VoltsGauge>
          <AmpsGauge><h2>30A</h2><h2> 32A</h2><h2>29A</h2></AmpsGauge>
          {/* <h3>L1 Volts: { content['Shore Converter Output digital meter'][10]['L1-N Volts'] }</h3>
          <h3>L2 Volts: { content['Shore Converter Output digital meter'][11]['L2-N Volts'] }</h3>
          <h3>L3 Volts: { content['Shore Converter Output digital meter'][12]['L3-N Volts'] }</h3> */}
        </Meters>
      </Card>
      <Card>
        <Meters>
        <VoltsGauge><h2>210V</h2><h2>210V</h2><h2>210V</h2></VoltsGauge>
          <AmpsGauge><h2>30A</h2><h2> 32A</h2><h2>29A</h2></AmpsGauge>
          {/* <h3>L1 Amps: { content['Shore Converter Output digital meter'][0]['L1 Amps'] }</h3>
          <h3>L2 Amps: { content['Shore Converter Output digital meter'][1]['L2 Amps'] }</h3>
          <h3>L3 Amps: { content['Shore Converter Output digital meter'][2]['L3 Amps'] }</h3> */}
        </Meters>
      </Card>
    </ShorePowerValues>
    <ShorePowerController>

    </ShorePowerController>
    </>
  )
}

const Card = styled.div`
  flex: 1;
  backgrund: rgb(21, 21, 21);
`

const VoltsGauge = styled.div`
  display: flex;
  justify-content: space-around;
  font-size: 1.8rem;
`

const AmpsGauge = styled.div`
  display: flex;
  justify-content: space-around;
  font-size: 1.8rem;
`

const ShorePowerValues = styled.div`
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  color: white;
`
const Meters = styled.div`
  color: green;
  background: black;
  padding: 2rem;
  margin: 20px;
  border-radius: 20px;
  font-size: 2.3rem;
  text-align: center;
  height: calc(100vh / 2.5);
`

const ShorePowerController = styled.div`
  background: black;
  width: calc(100vw - 10);
  height: calc(100vh / 4);
  margin: 20px;
`

export default Shore