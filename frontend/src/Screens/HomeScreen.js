import React, { useEffect, useState } from 'react';
import {Link} from "react-router-dom";
import axios from 'axios';
import image from '../rating-image.jpg';


const LockerList = (props) => {
   
    const [query, setQuery] = useState('');
    const [list, setList] = useState([]); 


 
      
    const onSubmit = (e) => {
        e.preventDefault(); 
        props.history.push("/");      
             
               
    }

    useEffect(async () => {              
        const result = await axios.get(`http://localhost:8000/api/v1/locker?search=${query}`);      
        setList(result.data);
      }, [query]);

     
    return(
    <div>
        <section className="main-image">
            <div className="container">
            <div className="row">
                <div className="col-md-8 search">
                <h3>Find a Locker</h3>
                <form action="" onSubmit={onSubmit}>
                    <input type="search" name="" id="" placeholder="Enter city or state.." onChange={(e) => setQuery(e.target.value)} />
                <button type="submit"className="search-btn">Find Locker<br/><p className="btn-text">One Naira For First Rent</p></button>   
                </form>
                </div>
            </div>

            </div>
        </section>
        <section className="sort">
            <div className="container">
           
            <div className="row">                
                
                <div className="col-md-6">
                <p>{list.reduce((a,v) => a = a + v.quantity, 0)} Open Lockers Available</p>
                </div>
                <div className="col-md-6 sort">
                <div className="select-price-picker">
                    <label for="cars">Sort By:</label>
                    <select id="">
                    <option >Closest</option>
                    <option >Lowest Price</option>
                    
                    </select>
                </div>
                
                </div>
          
            </div>            
            </div>
        </section>


        <section>
            <div className="container">
            <div className="row">
                <div className="col-md-2">
                    <div className="review">
                       <img src={image} alt="Hub Locker" className="logo" />
                        <p className="address">22A Adeola Odeku Street, VI,<br/>
                        Lagos</p> 
                        <div className="checked">
                            <span className="fa fa-star checked"></span>
                            <span className="fa fa-star checked"></span>
                            <span className="fa fa-star checked"></span>
                            <span className="fa fa-star"></span>
                            <span className="fa fa-star"></span>  
                        </div> 
                        <p className="address">0.3 miles away</p>                   

                    </div>
                

                </div>
                <div className="col-md-10">
                    <div className="row">
                        <div className="col-md-12">
                            <div className="select-box-picker">
                                <select name="" id="myFeature" >
                                <option selected hidden>Featured</option>
                                    <option value="Small">Small</option>
                                    <option value="Medium">Medium</option>
                                    <option value="Large">Large</option>
                                </select>
                            </div>
                
                        
                        </div>
                    
                    </div>
                    <div className="table-responsive">
                        <table className="table  main-table" id="myTable">
                            {list.map(item=>(
                        <tbody>
                            <tr>
                            <th scope="row">{item.specification}</th>
                            <td>{item.price}</td>
                            <td>{item.first_price}</td>
                            <td>{item.quantity} available</td>
                            <td className="table_button"><Link to="/rent" className="btn-rent">Rent Now</Link></td>
                            </tr>
                        
                      
                        </tbody>
                        ))}
                        </table>
                    </div>

                </div>
            </div>
        </div>
        </section>

    </div>

    

    );
}

export default  LockerList;