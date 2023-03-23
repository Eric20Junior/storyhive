import { React, useState, useEffect } from 'react'
import { Link } from 'react-router-dom'

const Books = () => {
    const [books, SetBooks] = useState([])

    useEffect(() => {
        fetch('http://127.0.0.1:8000/api/books/')
        .then(response => response.json())
        .then(data => SetBooks(data))
    }, [])

  return (
    <div className="container">
        <h1 className='text-center mt-8 font-bold underline'>Lastest Books</h1>

        <div className='flex justify-evenly m-16'>
        {books?.map((obj, index) => (
            <div key={obj.id} className="max-w-sm rounded overflow-hidden shadow-lg">
            <div className="px-6 py-4">
                <Link to={'/BookDetail/'} className="font-bold text-xl mb-2">{obj.title}</Link>
              <div className="text-gray-700 text-base">
                {obj.description}
              </div>
            </div>
            
          </div>
        ))}
    </div>
    </div>
  )
}

export default Books