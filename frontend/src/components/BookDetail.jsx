import { React, useState, useEffect } from 'react'

const BookDetail = () => {

  const [bookDetail, SetBookDetail] = useState([])

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/book-detail/1/')
    .then(response => response.json())
    .then(data => {
      // SetBookDetail(data)
      console.log(data)
    })
  }, [])
  
  return (
    <div>BookDetail</div>
  )
}

export default BookDetail