import './css/searchbar.css';

function SearchBar({songName, setSongName, isSub, setIsSub}){
    
    const handleChange = (event) => {
        setSongName(event.target.value);
    };
    
    const handleSub = (event) => {
        setIsSub(true);
        console.log(isSub);
    };

    const handleSubmit = () => {
        console.log(songName); 
    };

    const handleOnClick = () => {
        handleSubmit();
        handleSub();
    }

    return (
        <div className='search'>
          <input id= 'barId' className='bar' placeholder="Enter Song Tittle" onChange={handleChange}/>
          <button id='submitButton' className='button' onClick={handleOnClick}>Submit</button>
        </div>
     );
}

export default SearchBar;
