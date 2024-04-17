import React, { useState } from 'react';
import BasicTable from './basictable'
import SearchBar from './searchbar';
import './css/app.css';

function App() {
  const [songName, setSongName] = useState('');
  const [isSub, setIsSub] = useState(false);

  return (
    <div className='background'>
      {isSub 
        ? <BasicTable songName={songName} isSub={isSub} setIsSub={setIsSub}/>  // This will be displayed if isSub is true
        : <SearchBar songName={songName} setSongName={setSongName} isSub={isSub} setIsSub={setIsSub} /> // This will be displayed if isSub is false
      }
      {/* <BasicTable songName={songName} /> */}
    </div>
  );
}

export default App;
