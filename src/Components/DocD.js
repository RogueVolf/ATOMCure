import { useState, useEffect } from 'react';
import { Puff } from 'react-loader-spinner';

function DocD() {
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
     

<p className='red'>

85% of similar cases may lead to a brain tumor. Please consider further investigation

</p>
<p className='diagBox'>
The brain MRI scan of a 45-year-old male with persistent headaches and dizziness reveals no abnormal findings. There are no signs of hemorrhage, mass effect, midline shift, infarcts, or ischemic changes. The brain structures, cranial nerves, and intracranial vessels appear normal. The pituitary gland shows no abnormalities. 
</p>
        </div>
      )}
    </div>
  );
}

export default DocD;
