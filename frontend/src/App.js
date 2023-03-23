import './App.css';
import { Routes, Route } from 'react-router-dom';

import { Navbar, Books, BookDetail } from './components';

function App() {
  return (
    <div className="App">
        <Navbar />
        <Routes>
          <Route path='/' element={ <Books /> }/>
          <Route path='/BookDetail/' element={ <BookDetail /> }/>
        </Routes>
      </div>
  );
}

export default App;
