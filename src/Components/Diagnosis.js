import { useState, useEffect } from 'react';
import { Puff } from 'react-loader-spinner';

function MyComponent() {
  const [showLoader, setShowLoader] = useState(true);

  useEffect(() => {
    const timer = setTimeout(() => {
      setShowLoader(false);
    }, 5000); // 5000 milliseconds = 5 seconds

    return () => {
      clearTimeout(timer);
    };
  }, []);

  return (
    <div>
      
      {showLoader ? (
        <Puff
          color="#00BFFF" // Color of the loader
          height={100} // Height of the loader in pixels
          width={100} // Width of the loader in pixels
        />
      ) : (
        <div>
           <div className="subHead">

<h1 className='homeText'>ATOMCure</h1>


</div>
    <img src="brain.jpeg" alt=""  className="imgBrain" />
     


<p className='diagBox'>Based on initial AI analysis, it is advisable to consult a medical specialist for further evaluation, as there is a potential indication of a brain tumor.</p>
     
     <p>Below is a list of doctors near by, you may present the <a href='qr.jpeg'>QR Code </a></p>
        </div>
      )}
    </div>
  );
}

export default MyComponent;
