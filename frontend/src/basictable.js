import React, { useState, useEffect } from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import './css/basictable.css'
import { Container } from '@mui/material';

async function callBackend(requestName) {
  const requestBody = {
      song: requestName
  };

  try {
      const response = await fetch('http://localhost:5000/frontend', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json'
          },
          body: JSON.stringify(requestBody)
      });

      const data = await response.json();
      console.log('Result from backend:', data);
      return data
  } catch (error) {
      console.error('Error calling backend:', error);
  }
}

function createData(name, song1, song2, song3, song4, song5) {
  return { name, song1, song2, song3, song4, song5};
}

export default function BasicTable({songName, isSub, setIsSub}){ 
  var songNamesMin = []
  var songValuesMin = []
  var songNamesMax = []
  var songValuesMax = []
  var timeMin;
  var timeMax;

  const [songData, setSongData] = useState(null);
    useEffect(() => {
        if (songName) {
            callBackend(songName).then(data => setSongData(data));
        }
    }, [songName]);

  if(!songData){
    console.log("Loading")
  }
  else{
    timeMin = songData[0].exec_time_min
    const min = Object.values(songData[0].song_data_min)
    for(var i in min[0]){
      const songObj = min[0][i]
      const name = Object.keys(songObj)[0]
      const value = songObj[name];
      songNamesMin.push(name)
      songValuesMin.push(value)
    }
    timeMax = songData[1].exec_time_max
    const max = Object.values(songData[1].song_data_max)
    for(var i in max[0]){
      const songObj = max[0][i]
      const name = Object.keys(songObj)[0]
      const value = songObj[name];
      songNamesMax.push(name)
      songValuesMax.push(value)
    }
  }

  const handleSub = (event) => {
      setIsSub(false);
  };

  const handleOnClick = () => {
      handleSub();
  }

  const rows = [];
  const rows2 = [];
  rows.push(createData(songName, songNamesMin[0], songNamesMin[1], songNamesMin[2], songNamesMin[3], songNamesMin[4]))
  rows2.push(createData(songName, songNamesMax[0], songNamesMax[1], songNamesMax[2], songNamesMax[3], songNamesMax[4]))

  return (
    <Container>
      {!songData
      ? <div className="loader-container">
      <div className="loader"></div>
    </div>
      :<div><TableContainer className='tablecont' style={{ width: "100%" }}>
      <Table sx={{ minWidth: 650 }} aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell align="center" colSpan={3} style={{ fontSize: '40px', fontWeight: 'bold' }}>
              Root Song: {songName}
            </TableCell>
          </TableRow>
          <TableRow>
            <TableCell align="center" colSpan={3} style={{ fontSize: '20px', fontWeight: 'bold' }}>
              Min Heap: {timeMin} seconds
            </TableCell>
          </TableRow>
          <TableRow>
            <TableCell align="center" style={{ fontSize: '20px', fontWeight: 'bold' }}>Similar Songs</TableCell>
            <TableCell align="center" style={{ fontSize: '20px', fontWeight: 'bold' }}>Playlists Shared</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {songNamesMin.map((song, index) => (
            <TableRow hover key={index}>
              <TableCell align="center">{song}</TableCell>
              <TableCell align="center">{songValuesMin[index]}</TableCell>
            </TableRow>
          ))}
        </TableBody>
        <TableRow>
            <TableCell align="center" colSpan={3} style={{ fontSize: '20px', fontWeight: 'bold' }}>
              Max Heap: {timeMax} seconds
            </TableCell>
        </TableRow>
        <TableRow>
            <TableCell align="center" style={{ fontSize: '20px', fontWeight: 'bold' }}>Similar Songs</TableCell>
            <TableCell align="center" style={{ fontSize: '20px', fontWeight: 'bold' }}>Playlists Shared</TableCell>
        </TableRow>
        <TableBody>
          {songNamesMax.map((song, index) => (
            <TableRow hover key={index}>
              <TableCell align="center">{song}</TableCell>
              <TableCell align="center">{songValuesMax[index]}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
    <button className='backButton' onClick={handleOnClick}>Return</button></div>
      }
    </Container>
  );
}