
import React, { useState } from 'react';

const MultiStepForm = () => {
  const [currentStep, setCurrentStep] = useState(1);
  const [formData, setFormData] = useState({
    symptoms: [],
    hasImage: '',
    image: '',
    remarks: '',
  });


  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setFormData((prevState) => ({ ...prevState, [name]: value }));
  };

  const handleCheckboxChange = (event) => {
    const { name, checked } = event.target;
    let updatedSymptoms = [...formData.symptoms];
    if (checked) {
      updatedSymptoms.push(name);
    } else {
      updatedSymptoms = updatedSymptoms.filter((symptom) => symptom !== name);
    }
    setFormData((prevState) => ({ ...prevState, symptoms: updatedSymptoms }));
  };

  const handleFileUpload = (event) => {
    const file = event.target.files[0];
    setFormData((prevState) => ({ ...prevState, image: file }));
  };

  const handleNextStep = () => {
    setCurrentStep((prevStep) => prevStep + 1);
  };

  const handlePreviousStep = () => {
    setCurrentStep((prevStep) => prevStep - 1);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
   
    console.log(formData);


    window.location.href = '/Diagnosis';
    

    // Reset form data
    setFormData({
      symptoms: [],
      hasImage: '',
      image: '',
      remarks: '',
    });
    // Reset current step
    setCurrentStep(1);
  };

  return (
    <div className="container">
      <form onSubmit={handleSubmit}>
        {currentStep === 1 && (
          <div className="form-group">
            <p className="topHead">1</p>

            <h5>Please select your symptons from the list:</h5>
            <div className="form-check">
              <input
                type="checkbox"
                name="skin_rash"
                id="skinRash"
                className="form-check-input"
                checked={formData.symptoms.includes('skin_rash')}
                onChange={handleCheckboxChange}
                required

              />
              <label htmlFor="skinRash" className="form-check-label check1">
                Skin Rash
              </label>
            </div>
            <div className="form-check">
              <input
                type="checkbox"
                name="continuous_sneezing"
                id="continuousSneezing"
                className="form-check-input"
                checked={formData.symptoms.includes('continuous_sneezing')}
                onChange={handleCheckboxChange}
                
                required
              />
              <label htmlFor="continuousSneezing" className="form-check-label check1">
                Continuous Sneezing
              </label>
            </div>
            <div className="form-check">
              <input
                type="checkbox"
                name="shivering"
                id="shivering"
                className="form-check-input"
                checked={formData.symptoms.includes('shivering')}
                onChange={handleCheckboxChange}
                required
              />
              <label htmlFor="shivering" className="form-check-label check1">
                Shivering
              </label>
            </div>
            <div className="form-check">
              <input
                type="checkbox"
                name="stomach_pain"
                id="stomachPain"
                className="form-check-input"
                checked={formData.symptoms.includes('stomach_pain')}
                onChange={handleCheckboxChange}
                
                required
              />
              <label htmlFor="stomachPain" className="form-check-label check1">
                Stomach Pain
              </label>
            </div>
            <div className="form-check">
              <input
                type="checkbox"
                name="acidity"
                id="acidity"
                className="form-check-input"
                checked={formData.symptoms.includes('acidity')}
                onChange={handleCheckboxChange}
                
                required
              />
              <label htmlFor="acidity" className="form-check-label check1">
                Acidity
              </label>
            </div>
           
          
          
          
          
          </div>
        )}

        {currentStep === 2 && (
          <div className="form-group1">
             <p className="topHead">2</p>
             <label className='label1'>Do you have an image?</label>
            <div>
              <div className="form-check1 form-check-inline">
                <input
                  type="radio"
                  name="hasImage"
                  id="hasImageYes"
                  className="form-check-input display1"
                  value="yes"
                  checked={formData.hasImage === 'yes'}
                  onChange={handleInputChange}
                  required
                />
                <label htmlFor="hasImageYes" className="form-check-label1">
                  Yes
                </label>
              </div>
              <div className="form-check1 form-check-inline">
                <input
                  type="radio"
                  name="hasImage"
                  id="hasImageNo"
                  className="form-check-input display1"
                  value="no"
                  checked={formData.hasImage === 'no'}
                  onChange={handleInputChange}
                  required
                />
                <label htmlFor="hasImageNo" className="form-check-label1">
                  No
                </label>
              </div>
            </div>
          </div>
        )}

{currentStep === 3 && formData.hasImage === 'yes' && (
  <div className="form-group">
    <p className="topHead">3</p>
    <label>Upload Image:</label>
    <br />
    <input
      type="file"
      name="image"
      id="image"
      className="form-control-file"
      onChange={handleFileUpload}
      required
    />
    {formData.image && (
      <div className="image-preview">
        <img src={URL.createObjectURL(formData.image)} alt="Uploaded" className="img-thumbnail" />
      </div>
    )}
  </div>
)}


        {currentStep === 3 && (
          <div className="form-group">
            
            <textarea
            placeholder='Any Other Remarks?'
              name="remarks"
              id="remarks"
              className="form-control"
              value={formData.remarks}
              onChange={handleInputChange}
              required
            ></textarea>
          </div>
        )}

        <div className="form-group">
          {currentStep > 1 && (
            <button
              type="button"
              className="btn btn-secondary mr-2"
              onClick={handlePreviousStep}
            >
              Previous
            </button>
          )}
          {currentStep < 3 ? (
            <button
              type="button"
              className="btn btn-primary"
              onClick={handleNextStep}
            >
              Next
            </button>
          ) : (
            <button type="submit" className="btn btn-success">
              Submit
            </button>
          )}
        </div>
      </form>
    </div>
  );
};

export default MultiStepForm;
