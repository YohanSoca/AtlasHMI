// import './App.css';
// import axios from "axios"
// import {useEffect, useState} from 'react'
// import styled from 'styled-components'

// function App() {
//   const [coils, setCoils] = useState([]);

//   useEffect(() => {
//     const interval = setInterval(function() {
//       axios.get('http://192.168.50.92:8000/status').then((response) => {
//       if(response.data) {
//         console.log(response.data)
//       }
//     }).catch(e => e);
//     }, 500);
    
//   }, [])

//   const coilHandler = (index, e) => {
//       axios.post('http://192.168.0.12:8000/setCoil', {'coil': index + 8192, 'value': !e}).then(res => console.log('sent'))
//   }

//   const elements = coils && coils.map((e, idx) =>  e ? <StateOn><button onClick={() => coilHandler(idx, e)}>OFF</button><img src='./light.png' style={{width: '40px',}}/></StateOn> : <StateOff><button onClick={() => coilHandler(idx, e)}>ON</button><img src='./light.png' style={{width: '40px',}}/></StateOff>) || [false, false, false, false, false, false]
//   console.log(elements)
//   return (
//     <Dashboard>
//       { elements }
//     </Dashboard>
//   );
// }

// export default App

// const StateOn = styled.div`
//   color: white;
//   background: green;
//   margin: 10px;
//   box-shadow: 3px 3px 3px black;
//   text-shadow: 3px 3px 3px black;
//   text-align: center;
//   font-size: 3rem;
//   border-radius: 20px;
//   width: 80%;
//   height: calc(100hw / 10);
//   padding: 10px;

//   display: flex;
//   justify-content: space-between;

//   button {
//     width: 80px;
//     padding: 8px;
//     font-size: 1.2rem;
//     font-family: 'Chakra Petch', sans-serif;
//   }
// `
// const StateOff = styled.div`
//   color: white;
//   background: gray;
//   margin: 10px;
//   box-shadow: 3px 3px 3px black;
//   text-shadow: 3px 3px 3px black;
//   text-align: center;
//   font-size: 3rem;
//   border-radius: 20px;
//   width: 80%;
//   height: calc(100hw / 10);
//   padding: 10px;

//   display: flex;
//   justify-content: space-between;

//   button {
//     width: 80px;
//     padding: 8px;
//     font-size: 1.2rem;
//     font-family: 'Chakra Petch', sans-serif;
//     font-weight: bold;
//     border-shadow: 3px 3px 3px black;
//   }
// `

// const Dashboard = styled.div`
//   padding: 10px;
//   background: salmon;
//   height: 180vw;
//   display: flex;
//   flex-direction: column;
//   justify-content: center;
// `

// const Status = styled.div`
//   background: green;
//   width: 100px;
//   height: 100px;
//   border-radius: 50%;

//   position: fixed;
//   top: calc(100vh / 1.3);
//   left: calc(100vw / 1.2);
//   box-shadow: 3px 3px 3px black;
// `

// const Clock = styled.h1`
// padding: 2em;
// color: white;
// background: navy;
// margin: 20px 60px;
// box-shadow: 3px 3px 3px black;
// text-shadow: 3px 3px 3px black;
// text-align: center;
// font-size: 3rem;
// border-radius: 20px,
// `


import './App.css';
import axios from "axios"
import {useEffect, useState} from 'react'
import styled from 'styled-components'
import { Atlas } from './containers/Atlas';

function App() {
    return (
    <Screen>
      <Atlas />
    </Screen>
  );
}

const Screen = styled.div`
  
`

export default App;
