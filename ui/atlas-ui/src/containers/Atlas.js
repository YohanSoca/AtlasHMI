import React from 'react';
import Shore from '../containers/Shore';
import axios from "axios"
import {useEffect, useState} from 'react'
import styled from 'styled-components';


export const Atlas = () => {
  
  const [connected, setConnected] = useState(false);
  const [data, setData] = useState();

  useEffect(() => {
    const interval = setInterval(function() {
      axios.get('http://192.168.79.95:8000/status').then((response) => {
      if(response.data) {
        console.log(response.data.request['Shore Converter Output digital meter'])
        console.log(response.data.request['connected'])
        setConnected(response.data.request['connected'])
        let responseData = response.data.request ?? '';
        setData(responseData)
      }
    }).catch(e => e);
    }, 1000);
    
  }, [])

  return (
    <div>
      <MainNavBar>
        <NavBar>
          <h3>Shore</h3>
          <h3>Port</h3>
          <h3>STBD</h3>
          <h3>Alarms</h3>
          <h3>PMS</h3>
        </NavBar>
      </MainNavBar>
      {/* <div style={{width: '50px', height: '50px', backgroundColor: connected ? 'green' : 'red', borderRadius: '50%'}}></div> */}
      <Shore content={ data || '' }/>
    </div>
  )
}

const MainNavBar = styled.div`
  width: calc(100vw - 10);
  height: calc(100vh / 6);
  background: black;
  margin: 20px;
  color: white;
  
  display: flex;
  flex: 1;
  justify-content: flex-end;
  align-items: center;

  h1 {
    padding: 20px;
    font-size: 5rem;
  }
`

const NavBar = styled.div`
  display: flex;
  flex: 1;
  flex-direction: row;
  justify-content: space-around;

  h3 {
    font-size: 3rem;
  }
`
