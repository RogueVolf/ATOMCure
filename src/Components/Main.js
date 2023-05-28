import React from 'react'


export default function Main() {

    return (
        <>
            <div className="container atomHeading">
                <div className="row">
                    <h1 className='homeText'>ATOMCure</h1>
                    <p>Revolutionizing Conquering Challenges & Cancer's Hold</p>
                    <div className='mt-3'>
                       
                    <a href="/doctor">
                        <button type="button" className="btn btn-primary mx-3" >Doctor</button></a>
                       <a href="/patient">
                        <button type="button" className="btn btn-primary mx-3" >Patient</button>
                        </a> 
                    </div>
                </div>
            </div>
        </>

    )
}
