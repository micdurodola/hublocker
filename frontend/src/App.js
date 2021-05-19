import './App.css';
import {BrowserRouter as Router, Route} from "react-router-dom"
import Header from "./Screens/Header";
import LockerList from "./Screens/HomeScreen";
import LockerRent from "./Screens/RentScreen";
import Footer from './Screens/Footer';


function App() {
  return (
    <Router>
      <Header/>     
      <Route path="/" exact component={LockerList} />
      <Route path="/rent" exact component={LockerRent} />        
      <Footer/>

    </Router>
   
  );
}

export default App;
