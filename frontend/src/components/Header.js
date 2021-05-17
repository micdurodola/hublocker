import React, {Component} from "react";
import Link from "react-router-dom";


const header = () => {
    return(
        <div>
            <header>
                <nav className="navbar myNav">
                <div className="container-fluid">
                    <div className="navbar-header">
                    <button type="button" className="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
                        <span className="icon-bar"></span>
                        <span className="icon-bar"></span>
                        <span className="icon-bar"></span>
                    </button>
                    <a className="navbar-brand my_brand" href="#"><img src="#" alt="Hub Locker" className="logo" /></a>
                    </div>
                    <div className="collapse navbar-collapse myMenu" id="myNavbar">
                    <ul className="nav navbar-nav">
                        <li className="active"><a href="#">Home</a></li>
                        <li><a href="#">Find a Locker</a></li>
                        <li><a href="#">Size Guide</a></li>
                        <li><a href="#">Locations</a></li>
                        <li><a href="#">Help Center</a></li>
                    </ul>
                    <ul className="nav navbar-nav navbar-right">
                        <li><a href="#">My Account</a></li>
                        <li><a href="#">080-188-0872</a></li>
                        <li><a href="#" className="btn">PAY YOUR BILL</a></li>
                    
                    </ul>
                    </div>
                </div>
                </nav>
            </header>
    
  </div>

    );
}

export default header;