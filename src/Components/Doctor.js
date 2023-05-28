import React, { useRef } from 'react';
import NavBar from './NavBar';

const Doctor = () => {
  const fileInputRef = useRef(null);

  const handleFileChange = () => {
    const file = fileInputRef.current.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onloadend = () => {
        // Perform actions with the selected image data
        const imageData = reader.result;
        console.log('Selected image data:', imageData);

        // Redirect to a new page
        window.location.href = '/DocD';
      };
      reader.readAsDataURL(file);
    }
  };

  return (
    <div>
      <NavBar/>
       <p>Welcome Doctor!</p>
      <h1>Please Scan the QR </h1>
      <form>
        <input type="file" accept="image/*" ref={fileInputRef} onChange={handleFileChange}  className="hello" />
      </form>
    </div>
  );
};

export default Doctor;
